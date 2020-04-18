# File created by J Bujarski
# create.py contains functions to blend pictures appropriately.
#
#
import random

from pic import *


# blender:
#   first = the picture to be added
#   master = the aggregated photo
#   count = tracker used for the weight of the photo, keep balance
#   _w & _h = width/height, allow user input.
# FUTURE: make user options for width & height
def blender(first, master, count, _w=1024, _h=768):
    a = 1 / count

    one = Image.fromarray(load_pic(first, _w, _h))
    two = master

    if master.size == (0, 0):
        two = Image.fromarray(load_pic(first, _w, _h))

    three = Image.blend(two, one, a)
    return three


# rand_seed:
# create a picture based on a random seed.
#   var = the "random" seed
#   _w = width, set to "typical" 1024
#   _h = height, set to "typical" 768
#   intensity = how dense the picture is. Pass in 10 to see effect.
def rand_seed(var, _w=1024, _h=768, intensity=1):
    seed = 0
    for i in list(var):
        seed += ord(i)
    random.seed(seed)
    pic = np.ndarray((int(_h / intensity), int(_w / intensity), 3))
    for i in range(0, int(_h / intensity)):
        for j in range(0, int(_w / intensity)):
            pic[i, j] = (next(rng()))
    print(pic)
    pic = Image.fromarray((pic * 255).astype(np.uint8))

    return pic

# Generator for rand_seed function
def rng():
    while True:
        yield np.array([random.random(), random.random(), random.random()])
