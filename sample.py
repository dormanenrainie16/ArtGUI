# File created by J Bujarski
# sample.py contains a simple main to test merging pictures en masse

import os

from create import *


def main():
    # Pass in a string to rand_seed
    master = rand_seed("J_BUJARSKI", intensity=100)
    view_pic(master)


def merger():
    master = Image.Image()
    counter = 1

    for filename in os.listdir("/Users/jbujarski/Desktop/Everything/Pictures"):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            name = os.path.join('/Users/jbujarski/Desktop/Everything/Pictures/', filename)
            print(name)
            master = blender(name, master, counter)
            counter += 1
    view_pic(master)


if __name__ == "__main__":
    main()
