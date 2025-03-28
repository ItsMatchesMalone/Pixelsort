from PIL import Image
import numpy as np
import tifffile as tiff
import os

# === CONFIGURATION ===
input_path = "Aphelion/lady.tif"               # Input TIFF image
output_path = "Aphelion/ladysorted.TIF"        # Output TIFF image
mode = "bright"                                # Options: 'bright' or 'dark'
threshold = 127                                # Brightness threshold (0–255)
loops = 1                                      # Number of times to apply sorting

# === HELPER FUNCTIONS ===
def brightness(pixel):
    return 0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2]

def sort_line(line, mode, threshold):
    start = 0
    sorted_line = line.copy()

    while start < len(line):
        while start < len(line):
            b = brightness(line[start])
            if ((mode == 'bright' and b > threshold) or
                (mode == 'dark' and b < threshold)):
                break
            start += 1

        end = start
        while end < len(line):
            b = brightness(line[end])
            if not ((mode == 'bright' and b > threshold) or
                    (mode == 'dark' and b < threshold)):
                break
            end += 1

        if end - start > 1:
            region = line[start:end]
            sorted_region = sorted(region, key=brightness)
            sorted_line[start:end] = sorted_region

        start = end + 1

    return sorted_line

def pixel_sort(image_array, mode, threshold, loops=1):
    arr = image_array.copy()
    for _ in range(loops):
        for y in range(arr.shape[0]):
            arr[y] = sort_line(arr[y], mode, threshold)

        arr = arr.transpose((1, 0, 2))
        for y in range(arr.shape[0]):
            arr[y] = sort_line(arr[y], mode, threshold)
        arr = arr.transpose((1, 0, 2))
    return arr

# === LOAD IMAGE AND PROCESS ===
img = Image.open(input_path).convert("RGB")
img_array = np.array(img)
sorted_array = pixel_sort(img_array, mode, threshold, loops=loops)

# === SAVE RESULT ===
tiff.imwrite(output_path, sorted_array.astype(np.uint8))
print("Saved sorted image to", output_path)

