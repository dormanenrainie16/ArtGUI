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
        self.entry = Entry()
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
            if win1.state() == "normal": win1.focus()
        except NameError as e:
            print(e)
            win1 = tk.Toplevel()
            win1.geometry("600x600")
            win1["bg"] = "black"
            lb = Label(win1, text="Enter a word to get an image", fg='red', font=("Ink Free", 26))
            lb.pack()
            frame = Frame(win1)
            frame.pack(side=TOP)
            frame2 = Frame(win1)
            frame2.pack(side=TOP)
            self.entry = Entry(frame, bd=5)
            self.entry.pack(side=LEFT, fill=X)
            blended_button = Button(frame,  text="Enter word for a random image", font=("Times New Roman", 10))
            blended_button.pack(side=RIGHT, fill=X)
            self.entry = Entry(frame2, bd=5)
            self.entry.pack(side=LEFT, fill=X)
            random_seed_button = Button(frame2, text = "Enter word for Blended Image", font = ("Times New Roman", 10), command = self.entry_res)
            random_seed_button.pack(side=RIGHT, fill=X)

    # Stores the results of the entry box (user input) and clears the entry box after
    # Probably should do the algorithm in this function as well
    def entry_res(self):
        user_input = ""
        user_input = self.entry.get()
        print(user_input)
        self.entry.delete(0, END)

        master = Image.Image()
        counter = 1
        array = []
        # Uses google chrome
        array = download_google_staticimages(user_input)
        for i in range(1, len(array)):
            master = create.blender(array[i], master, counter)
            counter += 1
        pic.view_pic(master)


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
