# File created by J Bujarski
# pic.py contains functions necessary for picture loading and viewing
# load_pic:
#   Returns picture as a 2d array of RGB values, as per the w/h values passed in.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.figure import Figure
import matplotlib

load_pic = lambda name: np.array(Image.open(name))


def view_pic(name):
    plt.figure()
    plt.imshow(name)
    plt.axis('off')
    plt.tight_layout()
    #plt.show()
    return plt
