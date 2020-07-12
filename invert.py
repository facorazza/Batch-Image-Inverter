from os import listdir
from os.path import isfile, join

import click

from PIL import Image, ImageOps


@click.command()
@click.option(
    '-q',
    '--quality',
    type=int,
    default=100,
    help='Quality of the inverted image. [1-100]'
)
@click.argument(
    'paths',
    nargs=-1,
    type=click.Path()
)
def invert(quality, paths):
    for path in paths:
        if isfile(path):
            _invert(quality, path)
        else:
            files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
            for filename in files:
                _invert(quality, filename)


def _invert(quality, filename):
    if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
        print(f'Inverting {filename}')
        image = Image.open(filename)
        image_invert = ImageOps.invert(image.convert('RGB'))
        image_invert.save(filename, quality=quality)


if __name__ == '__main__':
    invert()
