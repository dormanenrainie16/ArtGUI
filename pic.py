# File created by J Bujarski
# pic.py contains functions necessary for picture loading and viewing
# load_pic:
#   Returns picture as a 2d array of RGB values, as per the w/h values passed in.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def load_pic(name, wd, ht):
    img = Image.open(name)
    imgA = np.array(img.resize((wd, ht)))

    return imgA


def view_pic(name):
    plt.figure()
    plt.imshow(name)
    plt.show()
