import os
import json
import math
import re
import subprocess
import sys
from PIL import Image

_TILE_STEM = re.compile(r"^(\d+)_(\d+)$")


def pack_images(input_dir, output_dir, max_size=4096, spacing=1, tile_range=None):
    """
    Packs small jpg tiles into multiple large png atlases using shelf packing.
    spacing: gap in pixels between adjacent tiles horizontally and between shelf rows.
    tile_range: optional (min_x, max_x, min_y, max_y) inclusive; only names like "12_3.jpg" are included.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Collect and sort files
    files = []
    for f in os.listdir(input_dir):
        if not f.lower().endswith(".jpg"):
            continue
        name_part = os.path.splitext(f)[0]
        if tile_range is not None:
            m = _TILE_STEM.match(name_part)
            if not m:
                continue
            coord = (int(m.group(1)), int(m.group(2)))
            min_x, max_x, min_y, max_y = tile_range
            if not (min_x <= coord[0] <= max_x and min_y <= coord[1] <= max_y):
                continue
        else:
            try:
                parts = name_part.split("_")
                if len(parts) == 2:
                    coord = (int(parts[0]), int(parts[1]))
                else:
                    coord = (0, 0)
            except ValueError:
                coord = (0, 0)

        img_path = os.path.join(input_dir, f)
        files.append({"path": img_path, "name": f, "coord": coord})

    if not files:
        print(f"No JPG files found in {input_dir}")
        return

    # 2. Load images to get sizes
    images_data = []
    for f in files:
        try:
            with Image.open(f["path"]) as img:
                images_data.append(
                    {
                        "name": f["name"],
                        "coord": f["coord"],
                        "size": img.size,
                        "path": f["path"],
                    }
                )
        except Exception as e:
            print(f"Failed to load {f['path']}: {e}")

    # Sort by height descending for better shelf packing
    images_data.sort(key=lambda x: x["size"][1], reverse=True)

    atlases = []

    def create_new_atlas():
        return {
            "image": Image.new("RGBA", (max_size, max_size), (0, 0, 0, 0)),
            "used_size": [0, 0],
            "shelf_y": 0,
            "shelf_height": 0,
            "shelf_x": 0,
            "items": [],
        }

    atlases.append(create_new_atlas())

    for item in images_data:
        w, h = item["size"]

        # Check if image itself is bigger than max_size
        if w > max_size or h > max_size:
            print(
                f"Warning: Image {item['name']} is larger than max_size {max_size}. Skipping."
            )
            continue

        # Check if it fits in current atlas shelf
        if atlases[-1]["shelf_x"] + w > max_size:
            # Move to next shelf
            atlases[-1]["shelf_y"] += atlases[-1]["shelf_height"] + spacing
            atlases[-1]["shelf_x"] = 0
            atlases[-1]["shelf_height"] = 0

        # Check if it fits in current atlas height
        if atlases[-1]["shelf_y"] + h > max_size:
            # Need new atlas
            atlases.append(create_new_atlas())

        # Pack it
        target_atlas = atlases[-1]
        pos_x = target_atlas["shelf_x"]
        pos_y = target_atlas["shelf_y"]

        try:
            with Image.open(item["path"]) as img:
                target_atlas["image"].paste(img.convert("RGBA"), (pos_x, pos_y))
        except Exception as e:
            print(f"Failed to paste {item['name']}: {e}")
            continue

        target_atlas["items"].append(
            {
                "name": item["name"],
                "coord": item["coord"],
                "frame": {"x": pos_x, "y": pos_y, "w": w, "h": h},
            }
        )

        target_atlas["shelf_x"] += w + spacing
        target_atlas["shelf_height"] = max(target_atlas["shelf_height"], h)
        target_atlas["used_size"][0] = max(target_atlas["used_size"][0], pos_x + w)
        target_atlas["used_size"][1] = max(
            target_atlas["used_size"][1],
            target_atlas["shelf_y"] + target_atlas["shelf_height"],
        )

    # 3. Finalize and Save
    atlas_mapping = {}  # original_filename -> {atlas_name, frame}

    for idx, atlas in enumerate(atlases):
        used_w, used_h = atlas["used_size"]
        if used_w > 0 and used_h > 0:
            # Crop atlas to used size to save space
            final_img = atlas["image"].crop((0, 0, used_w, used_h))
            atlas_name = f"atlas_{idx}.png"
            final_img.save(os.path.join(output_dir, atlas_name))

            for item in atlas["items"]:
                atlas_mapping[item["name"]] = {
                    "atlas": atlas_name,
                    "frame": item["frame"],
                }

    # Save JSON metadata
    with open(os.path.join(output_dir, "atlas_map.json"), "w") as f:
        json.dump(atlas_mapping, f, indent=4)

    print(
        f"Successfully packed {len(images_data)} images into {len(atlases)} atlas(es)."
    )
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", required=True, help="Input directory containing JPGs"
    )
    parser.add_argument("--output", required=True, help="Output directory for atlases")
    parser.add_argument(
        "--size", type=int, default=4096, help="Max size of atlas (e.g. 4096)"
    )
    parser.add_argument(
        "--spacing",
        type=int,
        default=1,
        help="Pixels between tiles horizontally and between shelf rows (default: 1)",
    )
    parser.add_argument(
        "--tile-range",
        type=str,
        default=None,
        help="Inclusive min_x,max_x,min_y,max_y e.g. 0,35,0,23; only digit_digit.jpg names",
    )
    args = parser.parse_args()

    tile_range = None
    if args.tile_range:
        parts = [int(x.strip()) for x in args.tile_range.split(",")]
        if len(parts) != 4:
            raise SystemExit("--tile-range requires four integers: min_x,max_x,min_y,max_y")
        tile_range = tuple(parts)

    try:
        pack_images(args.input, args.output, args.size, args.spacing, tile_range)
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback

        traceback.print_exc()
