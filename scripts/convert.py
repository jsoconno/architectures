from pathlib import Path
import os
from PIL import Image

"""
Random collection of some things used to LightMode up file names and icons.
"""

path = str(Path(__file__).parent.absolute())


def rename_file(file_path):
    os.rename(f, f.lower().replace('-', ' ').replace('(', '').replace(')', ''))


def crop_png(png_path):
    im = Image.open(f)
    im.size  # (364, 471)
    im.getbbox()  # (64, 89, 278, 267)
    im2 = im.crop(im.getbbox())
    im2.size  # (214, 178)
    im2.save(png_path)


for file in os.listdir(path):
    f = f'{path}/{file}'
    if '.png' in f:
        crop_png(f)
