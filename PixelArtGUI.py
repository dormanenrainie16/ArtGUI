'''
Created by: Betty Tannuzzo
Version 1
'''

import create
import pic

from download_images import *
import tkinter as tk
from tkinter import *
from tkinter import font
import os
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from browse import *

web = tk.Tk()
web.configure(background='Black')
web.geometry("600x600")

# title-label
web.title("Pixel Art Generator")
w = Label(web, text="Welcome to Pixel Art", font=("Ink Free", 36))
w.pack()

class Browse(Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes

class Example(Browse):
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)
        Browse.__init__(self, master, initialdir='', filetypes=())

        self.image = Image.open("pixels.jpg")
        self.img_copy = self.image.copy()
        self.blended_entry = Entry()
        self.random_entry = Entry()
        self.image_entry = Entry()
        self.intensity_entry = Entry()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack()
        self.background.bind('<Configure>', self._resize_image)

        # Buttons
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        self.search_word_button = Button(frame, text="Search word", command=self.search_word)
        self.search_word_button.pack(side=TOP, fill=X)
        self.search_word_button = Button(frame, text="Search Image(s)", command=self.search_image)
        self.search_word_button.pack(side=TOP, fill=X)
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=BOTTOM, fill=X)

    # resize background image on main window
    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    # opens new window to search for a word
    def search_word(self):
        try:
            win1 = tk.Toplevel()
            win1.geometry("600x600")
            win1["bg"] = "black"
            lb1 = Label(win1, text="Image Search By Word", fg='red', font=("Ink Free", 26))
            lb1.pack()

            ''' WORD SEARCH - NORMAL'''
            lb2 = Label(win1, text="Enter a word below to search for an image via Google", fg='red',
                        font=("Ink Free", 14))
            lb2.pack(side=TOP)
            frame = Frame(win1)
            frame.pack(side=TOP)
            self.image_entry = Entry(frame, bd=5, width=20)
            self.image_entry.grid(row=0, column=1, columnspan=3, padx=1, pady=1)
            image_button = Button(frame, text="Enter word for Regular Image", font=("Times New Roman", 10),
                                  command=self.image_entry_res)
            image_button.grid(row=0, column=20, columnspan=3, padx=1, pady=1)

            '''WORD SEARCH - COMPOSITE/BLENDED'''
            lb3 = Label(win1, text="Enter a word below to search for a composite image of many results", fg='red',
                        font=("Ink Free", 14))
            lb3.pack(side=TOP)
            frame1 = Frame(win1)
            frame1.pack(side=TOP)
            self.blended_entry = Entry(frame1, bd=5, width=20)
            self.blended_entry.grid(row=4, column=1, columnspan=3, padx=1, pady=1)
            blended_button = Button(frame1, text="Enter word for Blended Image", font=("Times New Roman", 10),
                                    command=self.blended_entry_res)
            blended_button.grid(row=4, column=20, columnspan=3, padx=1, pady=1)

            '''RANDOM IMAGE'''
            lb4 = Label(win1, text="Enter a string to seed a random picture, or leave blank for random seed", fg='red',
                        font=("Ink Free", 14))
            lb4.pack(side=TOP)
            frame2 = Frame(win1)
            frame2.pack(side=TOP)

            self.random_entry = Entry(frame2, bd=5)
            self.random_entry.pack(side=LEFT, fill=X)
            random_seed_button = Button(frame2, text="Enter word for a Random image", font=("Times New Roman", 10),
                                        command=self.random_entry_res)
            random_seed_button.pack(side=RIGHT, fill=X)

            lb5 = Label(win1, text="Enter an \"intensity\" value, or pixel density (larger = less dense)", fg='red',
                        font=("Ink Free", 14))
            lb5.pack(side=TOP)
            frame3 = Frame(win1)
            frame3.pack(side=TOP)
            self.intensity_entry = Entry(frame3, bd=2, width=10)
            self.intensity_entry.pack(side=LEFT, fill=X)
            intenstiy_label = Label(frame3, text="Intensity Level (random image)", font=("Times New Roman", 10))
            intenstiy_label.pack(side=RIGHT, fill=X)
        except NameError as e:
            print(e)
            win1 = tk.Toplevel()

    # Stores the results of the entry box (user input) and clears the entry box after
    # Probably should do the algorithm in this function as well
    def blended_entry_res(self):
        user_input = ""
        user_input = self.blended_entry.get()
        print(user_input)
        self.blended_entry.delete(0, END)

        master = Image.Image()
        counter = 1
        array = []
        # Uses google chrome
        array = download_google_staticimages(user_input)
        for i in range(1, len(array)):
            master = create.blender(array[i], master, counter)
            counter += 1
        res_fig = pic.view_pic(master)
        res_fig.show()
        # res.show()

    def image_entry_res(self):
        user_input = ""
        user_input = self.image_entry.get()
        print(user_input)
        self.image_entry.delete(0, END)

        master = Image.Image()
        counter = 1
        array = []
        # Uses google chrome
        array = download_google_staticimages(user_input)
        for i in range(1, 2):
            master = create.blender(array[i], master, counter)
            counter += 1
        res_fig = pic.view_pic(master)
        res_fig.show()
        # res.show()

    def random_entry_res(self):
        user_input = ""
        user_input = self.random_entry.get()
        print(user_input)
        self.random_entry.delete(0, END)

        if not self.intensity_entry:
            master = create.rand_seed(user_input)
            res_fig = pic.view_pic(master)
            res_fig.show()
        else:
            master = create.rand_seed(user_input, intensity=int(self.intensity_entry.get()))
            res_fig = pic.view_pic(master)
            self.intensity_entry.delete(0,END)
            res_fig.show()

    # opens a new window to search for image(s)
    # by Rainie Dormanen
    def search_image(self):
        try:
            if win2.state() == "normal": win2.focus()
        except NameError as e:
            print(e)
            win2 = tk.Toplevel()
            win2.geometry("600x600")
            win2["bg"] = "black"
            lb = Label(win2, text="Enter an image or images to get word", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win2)
            frame.pack(side=TOP)
            self.entry = Entry(frame, bd=5)
            self.entry.pack(side=TOP, fill=X)
            browse_button = Button(frame, text="Browse...", font=("Times New Roman", 10), command=self.browse)
            browse_button.pack(side=BOTTOM, fill=X, expand = True)
            file_browser = Browse(web, initialdir=r"C:\Users",
                                  filetypes=(('jpg files', '*.jpg',),
                                             ("All files", "*.*")))
            file_browser.pack(fill='x', expand=True)

    def browse(self):
        """ Browses a .jpg or .jpeg file or all files and then puts it on the entry.
        """
        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                                filetypes=self._filetypes))


# background image
e = Example(web)
e.pack()

# show Window
web.mainloop()

