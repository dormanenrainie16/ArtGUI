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
    pic = Image.fromarray((pic * 255).astype(np.uint8))
    return pic


# Generator for rand_seed function
def rng():
    while True:
        yield np.array([random.random(), random.random(), random.random()])


# hue:
# add a hue of color to the added picture
#   var: the color word to be passed in. See if statements. Other hues may be added?
#       Consider: Any RGB combo can be used, but R G and B are defaults.
#   pic: pass in an Image for best use!
#   w/h: standard parameters for width/height
#   intensity: the intensity of the pixels' sizes, default to 1
# Example call in main: hue("cool", rand_seed("J_BUJARSKI", intensity=10), intensity=10)
def hue(var, pic, _w=1024, _h=768, intensity=1):
    color = [0, 0, 0]
    if var == "warm":
        color = [0.5, 0, 0]
    elif var == "verdant":
        color = [0, 0.5, 0]
    elif var == "cool":
        color = [0, 0, 0.5]
    else:
        color = color  # Yeah do nothing.

    hue_pic = np.ndarray((int(_h / intensity), int(_w / intensity), 3))
    for i in range(0, int(_h / intensity)):
        for j in range(0, int(_w / intensity)):
            hue_pic[i, j] = color
    hue_pic = Image.fromarray((hue_pic * 255).astype(np.uint8))
    return Image.blend(pic, hue_pic, 0.5)
