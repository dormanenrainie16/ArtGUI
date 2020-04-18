# File created by J Bujarski
# create.py contains functions to blend pictures appropriately.
#
#

from pic import *


def blender(first, master, count):
    _w = 1024
    _h = 768
    a = 1 / count

    one = Image.fromarray(load_pic(first, _w, _h))
    two = master

    if master.size == (0, 0):
        two = Image.fromarray(load_pic(first, _w, _h))

    three = Image.blend(two, one, a)

    return three
