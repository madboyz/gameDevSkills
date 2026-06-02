import subprocess
import os
import sys


def run_atlas_pack(input_dir, output_dir, max_size="4096", spacing="2"):
    """
    Wrapper to run the atlas packer python script.
    Default spacing 2px between tiles (see packer_engine.pack_images).
    """
    # Find the script path relative to this file
    script_path = os.path.join(os.path.dirname(__file__), "packer_engine.py")

    if not os.path.exists(script_path):
        print(f"Error: Packer engine script not found at {script_path}")
        return

    command = [
        sys.executable,
        script_path,
        "--input",
        input_dir,
        "--output",
        output_dir,
        "--size",
        max_size,
        "--spacing",
        spacing,
    ]

    print(f"Executing: {' '.join(command)}")

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during packing:\n{e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="Input directory containing JPGs")
    parser.add_argument("output_dir", help="Output directory for atlases")
    parser.add_argument(
        "max_size", nargs="?", default="4096", help="Max size of atlas (default: 4096)"
    )
    parser.add_argument(
        "--spacing",
        default="2",
        help="Pixels between tiles (default: 2)",
    )
    args = parser.parse_args()

    run_atlas_pack(args.input_dir, args.output_dir, args.max_size, args.spacing)
