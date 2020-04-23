# File created by J Bujarski
# create.py contains functions to blend pictures appropriately.
#
#
import os
import random

from pic import *


# blender:
#   first = the picture to be added
#   master = the aggregated photo
#   count = tracker used for the weight of the photo, keep balance
#   _w & _h = width/height, allow user input.
# FUTURE: make user options for width & height
def blender(added, master, count, _w=1024, _h=768):
    a = 1 / count
    saved = master

    if master.size == (0, 0):
        saved = added

    added = added.convert(mode='RGBA')
    saved = saved.convert(mode='RGBA')
    added = added.resize((_w, _h))
    saved = saved.resize((_w, _h))

    return Image.blend(saved, added, a)


'''
# merger:
# takes a directory of Images and uses Image.blend to combine.
# Note: count is used for alpha values, as count increases, the prevalence of new images decreases
# MUST BE UPDATED ONCE IMAGE[] IS COMPLETE
def merger():
    master = Image.Image()
    counter = 1

    for filename in os.listdir("/Users/jbujarski/Desktop/Everything/Pictures"):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            f_name = os.path.join('/Users/jbujarski/Desktop/Everything/Pictures/', filename)
            print(f_name)
            master = blender(Image.fromarray(load_pic(f_name)), master, counter)
            counter += 1
    view_pic(master)
'''


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
    resized = Image.fromarray(load_pic(pic))
    resized = resized.resize((int(_w / intensity), int(_h / intensity)))
    return Image.blend(resized, hue_pic, 0.5)


# negative:
# convert a picture to the photo-negative version
#   ALL VARIABLES REDUNDANT TO hue; SAME FUNCTIONALITY UNDER DIFFERENT PARAM.
def negative(pic):
    pict = load_pic(pic)
    neg_pic = np.ndarray((pict.shape[0], pict.shape[1], 3))
    for i in range(0, pict.shape[0]):
        for j in range(0, pict.shape[1]):
            neg_pic[i, j] = pict[i, j]
    return Image.fromarray((neg_pic * 255).astype(np.uint8))


# ascii:
# convert a picture to a rudimentary ASCII translation
def ascii_pic(pic, intensity=1):
    asc = Image.fromarray(load_pic(pic)).convert("L")
    asc = np.array(asc.resize((int(asc.width * 2 / intensity), int(asc.height / intensity))))

    p_name = str.split(pic, ".")
    line = ""
    pic_txt = open(p_name[0] + ".txt", "w")
    for i in range(asc.shape[0]):
        for j in range(asc.shape[1]):
            line = line.__add__(chr(switcher(int(asc[i, j] / 32))))  # print(line)
        pic_txt.write(line + "\n")
        line = ""
    return asc


# switcher: required for unicode conversion
def switcher(choice):
    switch = {
        0: 32,  # space
        1: 9624,  # "▘"
        2: 9626,  # "▚"
        3: 9625,  # "▙"
        4: 9617,  # "░"
        5: 9618,  # "▒"
        6: 9619,  # "▓"
        7: 9608  # "█"
    }
    return switch.get(choice)


# asc_cond: ascii_condensed
# produces a more condensed version of the Ascii picture
# INCOMPLETE: MIRRORS ascii_pic AS OF NOW.
def asc_cond(pic, intensity=1):
    asc = Image.fromarray(load_pic(pic)).convert("L")
    asc = asc.resize((int(asc.width * 2 / intensity), int(asc.height / intensity)))
    while asc.width % 2: asc = asc.resize(((asc.width - 1), asc.height))
    while asc.height % 2: asc = asc.resize((asc.width, (asc.height - 1)))
    asc = np.array(asc)

    p_name = str.split(pic, ".")
    line = ""
    pic_txt = open(p_name[0] + ".txt", "w")
    for i in range(asc.shape[0]):
        for j in range(asc.shape[1]):
            line = line.__add__(chr(switcher(int(asc[i, j] / 32))))  # print(line)
        pic_txt.write(line + "\n")
        line = ""
    return asc

# Other fun ideas:
# replace instances of a single color for another (i.e. every red becomes blue)
