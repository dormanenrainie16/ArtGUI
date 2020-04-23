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
    pict = Image.fromarray(load_pic(pic))
    hue_pic = np.ndarray((int(pict.width), int(pict.height), 3))
    for i in range(0, int(pict.width)):
        for j in range(0, int(pict.height)):
            hue_pic[i, j] = color
    hue_pic = Image.fromarray((hue_pic * 255).astype(np.uint8))
    resized = Image.fromarray(load_pic(pic))
    resized = resized.resize((int(pict.height), int(pict.width)))

    return Image.blend(resized, hue_pic, 0.5)


# negative:
# convert a picture to the photo-negative version
#   ALL VARIABLES REDUNDANT TO hue; SAME FUNCTIONALITY UNDER DIFFERENT PARAM.
def negative(pic):
    pict = Image.fromarray(load_pic(pic))
    pict = np.array(pict.convert(mode='RGB'))

    neg_pic = np.ndarray((pict.shape[0], pict.shape[1], 3))
    for i in range(0, pict.shape[0]):
        for j in range(0, pict.shape[1]):
            neg_pic[i, j] = pict[i, j]

    return Image.fromarray((neg_pic * 255).astype(np.uint8))


# ascii:
# convert a picture to a rudimentary ASCII translation
def ascii_pic(pic, intensity=10):

    asc = Image.fromarray(load_pic(pic)).convert("L")
    asc = np.array(asc.resize((int(asc.width * 2 / intensity), int(asc.height / intensity))))
    p_name = str.split(pic, ".")
    line = ""
    pic_txt = open(p_name[0] + "_ascii.txt", "w")

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
def asc_cond(pic, intensity=1):
    asc = Image.fromarray(load_pic(pic)).convert("L")
    asc = asc.resize((int(asc.width * 2 / intensity), int(asc.height / intensity)))
    while asc.width % 2: asc = asc.resize(((asc.width - 1), asc.height))
    while asc.height % 2: asc = asc.resize((asc.width, (asc.height - 1)))
    asc = np.array(asc)
    p_name = str.split(pic, ".")
    line = ""
    pic_txt = open(p_name[0] + "_condensed.txt", "w")

    for i in range(0, asc.shape[0], 2):
        for j in range(0, asc.shape[1], 2):
            line = line.__add__(chr(adv_swtch(int(asc[i, j]),
                                              int(asc[i, j + 1]),
                                              int(asc[i + 1, j]),
                                              int(asc[i + 1, j + 1]))))
        pic_txt.write(line + "\n")
        line = ""

    return asc
    # line = line.__add__(chr(switcher(int(asc[i, j] / 32))))  # print(line)


def adv_swtch(on, tw, th, fr):
    one = int(on / 32)
    two = int(tw / 32)
    three = int(th / 32)
    four = int(fr / 32)

    same = set()
    if one == two:
        same.add(1)
        same.add(2)
    if one == three:
        same.add(1)
        same.add(3)
    if one == four:
        same.add(1)
        same.add(4)
    if two == three:
        same.add(2)
        same.add(3)
    if two == four:
        same.add(2)
        same.add(4)
    if three == four:
        same.add(3)
        same.add(4)

    prominent = max(one, two, three, four)

    # All unique, determine which is strongest value.
    if same.__len__() == 0:
        e_zero = {
            1: 9624,  # Block up l
            2: 9629,  # Block up r
            3: 9622,  # Block low l
            4: 9621,  # Block low r
            5: 39,  # apostrophe
            6: 39,  # apostrophe
            7: 46,  # period
            8: 46  # period
        }
        if prominent > 3:
            if one > two and one > three and one > four:
                return e_zero.get(1)
            elif two > one and two > three and two > four:
                return e_zero.get(2)
            elif three > one and three > two and three > four:
                return e_zero.get(3)
            else:
                return e_zero.get(4)
        else:
            if one > two and one > three and one > four:
                return e_zero.get(5)
            elif two > one and two > three and two > four:
                return e_zero.get(6)
            elif three > one and three > two and three > four:
                return e_zero.get(7)
            else:
                return e_zero.get(8)

    # 2 are equal, determine which and their intensity
    elif same.__len__() == 2:
        e_one = {
            1: 9600,  # Upper half block
            2: 9612,  # Left Half block
            3: 9626,  # TL-BR block
            4: 9630,  # TR-BL block
            5: 9616,  # Right half block
            6: 9604,  # Lower half block
            7: 9620,  # Upper eighth block
            8: 9614,  # Left quarter block
            9: 92,  # \
            10: 47,  # /
            11: 9621,  # Right eighth block
            12: 9602,  # Lower eighth block
        }
        if prominent > 3:
            if same.__contains__(1):
                if same.__contains__(2):
                    return e_one.get(1)
                elif same.__contains__(3):
                    return e_one.get(2)
                elif same.__contains__(4):
                    return e_one.get(3)
            elif same.__contains__(2):
                if same.__contains__(3):
                    return e_one.get(4)
                else:
                    return e_one.get(5)
            else:
                return e_one.get(6)
        else:
            if same.__contains__(1):
                if same.__contains__(2):
                    return e_one.get(7)
                elif same.__contains__(3):
                    return e_one.get(8)
                elif same.__contains__(4):
                    return e_one.get(9)
            elif same.__contains__(2):
                if same.__contains__(3):
                    return e_one.get(10)
                else:
                    return e_one.get(11)
            else:
                return e_one.get(12)

    # 3 are equal, determine intensity and formation
    elif same.__len__() == 3:
        e_two = {
            1: 9631,  # J block
            2: 9625,  # L block
            3: 9628,  # 7 block
            4: 9627,  # F block
            5: 74,  # J
            6: 76,  # L
            7: 55,  # 7
            8: 70,  # F
        }
        if prominent > 3:
            if not same.__contains__(1):
                return e_two.get(1)
            elif not same.__contains__(2):
                return e_two.get(2)
            elif not same.__contains__(3):
                return e_two.get(3)
            else:
                return e_two.get(4)
        else:
            if not same.__contains__(1):
                return e_two.get(5)
            elif not same.__contains__(2):
                return e_two.get(6)
            elif not same.__contains__(3):
                return e_two.get(7)
            else:
                return e_two.get(8)

    # All 4 equal, determine value of one and return
    elif same.__len__() == 4:
        e_three = {
            0: 32,  # space
            1: 9617,  # "░"
            2: 9617,  # "░"
            3: 9618,  # "░"
            4: 9618,  # "▒"
            5: 9619,  # "░"
            6: 9619,  # "▓"
            7: 9608  # "█"
        }
        return e_three.get(one)
