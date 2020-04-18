# File created by J Bujarski
# sample.py contains a simple main to test merging pictures en masse

import os

from create import *


def main():
    master = Image.Image()
    counter = 1


# If you choose to use this sample file, you may want to change the path to a folder on your computer with 
# pictures so you can see the result.
    for filename in os.listdir("/Users/jbujarski/Desktop/Everything/Pictures"):
        if filename.endswith(".jpg"):
            name = os.path.join('/Users/jbujarski/Desktop/Everything/Pictures/', filename)
            print(name)
            master = blender(name, master, counter)
            counter += 1
    view_pic(master)


if __name__ == "__main__":
    main()
