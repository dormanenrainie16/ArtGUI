# File created by J Bujarski
# sample.py contains a simple main to test merging pictures en masse

import os

from create import *


def main():
    # Pass in a string to rand_seed
    # master = hue("verdant", "pixels.jpg", intensity=1)
    # master = negative("Me&Cleo.jpg")
    # master = ascii_pic("Me&Pops.jpg", intensity=15)
    master = asc_cond("Me&Pops.jpg", intensity=10)
    # merger()
    # view_pic(master)


if __name__ == "__main__":
    main()
