import os

import click

from PIL import Image, ImageOps


@click.command()
@click.option(
    '-p',
    '--path',
    default=".",
    help='Path of the folder where the images to be inverted is stored.'
)
@click.option(
    '-q',
    '--quality',
    type=int,
    default=100,
    help='Quality of the inverted image. [1-100]'
)
def invert(path, quality):
    for filename in os.listdir(path):
        print(filename)
        if filename.lower().endswith((".jpeg", ".jpg")):
            print(filename)
            image = Image.open(path+"/"+filename)
            image_invert = ImageOps.invert(image.convert('RGB'))
            image_invert.save(path+"/"+filename, quality=quality)


if __name__ == '__main__':
    invert()
