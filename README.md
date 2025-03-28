# Pixel Sorting Art

This Python script applies artistic pixel sorting to `.tiff` images based on brightness thresholds. Inspired by glitch aesthetics similar to Kim Asendorf's work.

## Features

- Brightness-based pixel sorting (modes: bright or dark)
- Works with `.tiff` images
- Horizontal and vertical sorting
- Simple and extensible design
- Uses Pillow, NumPy, and tifffile

## Example Results

### Mountains (before and after)

**Input**  
![Before](Aphelion/before.tif)

**Output**  
![After](Aphelion/after.tif)

---

### Lady (before and after)

**Input**  
![Lady Original](Aphelion/lady.tif)

**Output**  
![Lady Sorted](Aphelion/ladysorted.TIF)

---

## How to Use

1. Place your `.tiff` images inside the `Aphelion/` folder.
2. Adjust parameters in `pixel_sort.py` to set:
   - Input and output filenames
   - Sorting mode (`bright` or `dark`)
   - Brightness threshold
3. Install requirements and run the script:

```bash
pip install -r requirements.txt
python pixel_sort.py
