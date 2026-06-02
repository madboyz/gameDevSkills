# AtlasPacker Skill

## Description
Automatically packs a directory of small `.jpg` tiles into one or more large `.png` atlases using a shelf-packing algorithm. It generates a `atlas_map.json` mapping original filenames to their position and atlas name.

## Usage
Use the command: `/atlas-pack <<inputinput_dir> <<outputoutput_dir> [max_size]`

### Arguments
- `input_dir`: The directory containing the source `.jpg` files.
- `output_dir`: The directory where the generated atlases and JSON will be saved.
- `max_size`: (Optional) The maximum width/height of the generated atlas. **Note: For optimal mobile compatibility, it is recommended to use 2048.** (default: 4096).

### Packing spacing
- Tiles are laid out with a **1-pixel gap** between neighbors on the same row and between rows (shelf packing). This reduces bleeding when sampling adjacent sprites. Override via `packer_engine.py --spacing N` if needed.

### Example
`/atlas-pack assets/scripts/logic/map/2001 output/map_atlases 2048`

## Workflow
1. Scans `input_dir` for `.jpg` files.
2. Sorts images by height to optimize packing.
3. Distributes images into one or more "shelves" within the `max_size` limit, with 2px spacing between tiles.
4. If a shelf or atlas is full, it automatically starts a new atlas.
5. Saves the packed `.png` files and an `atlas_map.json` metadata file.

## Requirements
- Python 3.x
- `Pillow` library (`pip install Pillow`)
