'''
Created by: Betty Tannuzzo
Version 1
'''

import tkinter as tk
from tkinter import *
from tkinter import font
import os
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

web = tk.Tk()
web.configure(background='Black')
web.geometry("600x600")
# title-label
w = Label(web, text="Welcome to Pixel Art", font=("Ink Free", 36))
w.pack()

class Example(Frame):
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)

        self.image = Image.open("pixels.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack()
        self.background.bind('<Configure>', self._resize_image)

        # Buttons
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        self.search_word_button = Button(frame, text="Search word")
        self.search_word_button.pack(side=TOP,fill=X)
        self.search_word_button = Button(frame, text="Search Image(s)")
        self.search_word_button.pack(side=TOP,fill=X)
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=BOTTOM, fill=X)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# background image
e = Example(web)
e.pack()

# show Window
web.mainloop()
