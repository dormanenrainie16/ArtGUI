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
w = Label(web, text="Welcome to the Pixel Art GUI", bg='black', fg='#00ff00', font=("Courier", 32))
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

        # image for main window background
        self.image = Image.open("pixels.jpg")

        self.img_copy = self.image.copy()
        self.blended_entry = Entry()
        self.random_entry = Entry()
        self.image_entry = Entry()
        self.intensity_entry = Entry()
        self.background_image = ImageTk.PhotoImage(self.image)

        # Needed to update images on window as buttons are clicked
        self.label = None
        self.img = None

        self.background = Label(self, image=self.background_image)
        self.background.pack()
        self.background.bind('<Configure>', self._resize_image)

        # Buttons for main window
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        self.search_word_button = Button(frame, text="Search word", highlightbackground='black', command=self.search_word)
        self.search_word_button.pack(side=TOP, fill=X)
        self.search_word_button = Button(frame, text="Search Image(s)", highlightbackground='black', command=self.search_image)
        self.search_word_button.pack(side=TOP, fill=X)
        self.button = Button(frame, text="QUIT", fg="red", highlightbackground='black', command=frame.quit)
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
            lb1 = Label(win1, text="Image Search By Word", fg='#00ff00', bg='black', font=("Courier", 26))
            lb1.pack()

            # This is the frame that keeps changing the photo whenever a word/button is searched/pressed
            img_frame = self.create_frame(win1)
            self.label = Label(img_frame)
            img_frame.pack(side=BOTTOM)

            '''WORD SEARCH - Search for an image '''
            lb2 = Label(win1, text="Enter a word below to search for an image via Google", fg='#00ff00', bg='black',
                        font=("Courier", 14))
            lb2.pack(side=TOP)
            frame = Frame(win1)
            frame.pack(side=TOP)
            self.image_entry = Entry(frame, bd=5, width=20)
            self.image_entry.grid(row=0, column=1, columnspan=3, padx=1, pady=1)
            image_button = Button(frame, text="Enter word for Regular Image", font=("Times New Roman", 10),
                                  command=lambda: self.image_entry_res(img_frame, win1, self.label))
            image_button.grid(row=0, column=20, columnspan=3, padx=1, pady=1)

            '''WORD SEARCH - COMPOSITE/BLENDED'''
            lb3 = Label(win1, text="Enter a word below to search for a composite image of many results", fg='#00ff00',
                        bg='black', font=("Courier", 14))
            lb3.pack(side=TOP)
            frame1 = Frame(win1)
            frame1.pack(side=TOP)
            self.blended_entry = Entry(frame1, bd=5, width=20)
            self.blended_entry.grid(row=4, column=1, columnspan=3, padx=1, pady=1)
            blended_button = Button(frame1, text="Enter word for Blended Image", font=("Times New Roman", 10),
                                    command=lambda: self.blended_entry_res(img_frame, win1, self.label))
            blended_button.grid(row=4, column=20, columnspan=3, padx=1, pady=1)

            '''RANDOM IMAGE - produces random pixels based on string'''
            lb4 = Label(win1, text="Enter a string to seed a random picture, or leave blank for random seed",
                        fg='#00ff00', bg='black', font=("Courier", 14))
            lb4.pack(side=TOP)
            frame2 = Frame(win1)
            frame2.pack(side=TOP)
            self.random_entry = Entry(frame2, bd=5)
            self.random_entry.pack(side=LEFT, fill=X)
            random_seed_button = Button(frame2, text="Enter word for a random image", font=("Times New Roman", 10),
                                        command=lambda: self.random_entry_res(img_frame, win1, self.label))
            random_seed_button.pack(side=RIGHT, fill=X)
            lb5 = Label(win1, text="Enter an \"intensity\" value, or pixel density (larger = less dense)", fg='#00ff00',
                        bg='black', font=("Courier", 14))
            lb5.pack(side=TOP)
            frame3 = Frame(win1)
            frame3.pack(side=TOP)
            self.intensity_entry = Entry(frame3, bd=5, width=10)
            self.intensity_entry.pack(side=LEFT, fill=X)
            intenstiy_label = Label(frame3, text="Intensity Level (random image)", font=("Times New Roman", 10))
            intenstiy_label.pack(side=RIGHT, fill=X)

        except NameError as e:
            print(e)
            win1 = tk.Toplevel()

    # Needed to create frame for img_frame above to keep changing pictures
    def create_frame(self, window):
        frame = Frame(window)
        # frame.pack(side=BOTTOM)
        return frame

    ''' Stores the results of the entry box (user input) and clears the entry box after.
        Takes user input and searches Google for 100 pictures and blends them together 
        using the blender function from create.py. It then displays the blended image
        in the window. '''
    def blended_entry_res(self, frame, window, label):
        user_input = "No results"
        user_input = self.blended_entry.get()
        print(user_input)
        self.blended_entry.delete(0, END)

        master = Image.Image()
        counter = 1
        array = []

        panel = label
        panel.pack()

        # Uses google chrome
        array = download_google_staticimages(user_input)
        master = create.blender(array[1], master, counter)
        master = master.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(master)

        for i in range(2, len(array)):
            master = create.blender(array[i], master, counter)
            counter += 1
            master = master.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(master)
            panel.config(image=img)
            panel.photo_ref = img
            window.update()
        # Get the image so it is ready to be displayed

        # Display image in label

        panel.image = img

    ''' Stores the results of the entry box (user input) and clears the entry box after.
        Takes user input and searches Google and gets the first image of the word 
        searched. It then displays it on the window. '''
    def image_entry_res(self, frame, window, label):
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

        # Get the image so it is ready to be displayed
        master = master.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(master)

        # Display image in label
        panel = label
        panel.image = img
        panel.config(image=img)
        panel.pack()
        panel.photo_ref = img
        window.update()

    ''' Stores the results of the entry box (user input) and clears the entry box after.
            Takes user input and sends it in as an argument to rand_seed() function in
             create.py. It displays a pixel image based on the string value and 
             has an optional argument for intensity.'''
    def random_entry_res(self, frame, window, label):
        user_input = ""
        user_input = self.random_entry.get()
        print(user_input)
        self.random_entry.delete(0, END)

        # Do this if there is no intensity level given
        if not self.intensity_entry.get():
            master = create.rand_seed(user_input)
            master = master.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(master)

            # Display image in label
            panel = label
            panel.image = img
            panel.config(image=img)
            panel.pack()
            panel.photo_ref = img
            window.update()
        # do this if intensity level was given
        else:
            master = create.rand_seed(user_input, intensity=int(self.intensity_entry.get()))
            self.intensity_entry.delete(0, END)
            master = master.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(master)

            # Display image in label
            panel = label
            panel.image = img
            panel.config(image=img)
            panel.pack()
            panel.photo_ref = img
            window.update()

    # opens a new window to search for image(s)
    # by Rainie Dormanen
    def search_image(self):
        win2 = tk.Toplevel()
        win2["bg"] = "black"
        lb = Label(win2, text="Edit Image", fg='#00ff00', bg='black', font=("Courier", 25))
        lb.pack()
        frame = Frame(win2, bg='black')
        frame.pack(side=TOP)

        filename = fd.askopenfilename(initialdir=r"C:\Users", title="Browse Images",
                                      filetypes=(('jpg files', '*.jpg',),
                                                 ('png files', '*.png'),
                                                 ('jpeg files', '*.jpeg')))

        fphoto = Image.open(filename)
        _w = min(1200, fphoto.width)
        _h = min(800, fphoto.height)
        fphoto = fphoto.resize((_w, _h), Image.ANTIALIAS)
        geo = str(str(_w) + "x" + str(_h + 100))

        win2.geometry(geo)

        tkphoto = ImageTk.PhotoImage(fphoto)  # saves copy of image
        label = Label(win2, image=tkphoto)
        label.image = tkphoto
        label.pack(side=BOTTOM)
        # ORIGINAL
        original_button = Button(frame, text="Original Image", highlightbackground='black', font=("Times New Roman", 15),
                                 command=lambda: revert(fphoto))
        original_button.pack(pady=10, side=LEFT)

        # NEGATIVE
        negative_button = Button(frame, text="Negative Image", highlightbackground='black', font=("Times New Roman", 15),
                                 command=lambda: add_neg(Image.open(filename)))
        negative_button.pack(pady=10, side=LEFT)

        # WARM
        warm_button = Button(frame, text="Add Warm Hues", highlightbackground='black', font=("Times New Roman", 15),
                             command=lambda: add_hue(Image.open(filename), "warm"))
        warm_button.pack(pady=10, side=LEFT)

        # VERDANT
        verdant_button = Button(frame, text="Add Verdant Hues", highlightbackground='black', font=("Times New Roman", 15),
                                command=lambda: add_hue(Image.open(filename), "verdant"))
        verdant_button.pack(pady=10, side=LEFT)

        # COOL
        cool_button = Button(frame, text="Add Cool Hues", highlightbackground='black', font=("Times New Roman", 15),
                             command=lambda: add_hue(Image.open(filename), "cool"))
        cool_button.pack(pady=10, side=LEFT)

        # ASCII
        ascii_button = Button(frame, text="Convert Image to Ascii", highlightbackground='black', font=("Times New Roman", 15),
                              command=lambda: add_ascii(Image.open(filename)))
        ascii_button.pack(pady=10, side=LEFT)

        # ASCII CONDENSED
        cond_ascii_button = Button(frame, text="Convert Image to Condensed Ascii", highlightbackground='black',
                                   font=("Times New Roman", 15),
                                   command=lambda: add_cond_ascii(Image.open(filename)))
        cond_ascii_button.pack(pady=10, side=LEFT)

        def revert(photo):
            fphoto = Image.open(filename)
            fphoto = fphoto.resize((_w, _h), Image.ANTIALIAS)
            tkphoto = ImageTk.PhotoImage(fphoto)
            label.configure(image=tkphoto)
            label.image = tkphoto

        def add_neg(photo):
            fphoto = create.negative(filename)
            fphoto = fphoto.resize((_w, _h), Image.ANTIALIAS)
            tkphoto = ImageTk.PhotoImage(fphoto)
            label.configure(image=tkphoto)
            label.image = tkphoto

        def add_hue(photo, str):
            fphoto = create.hue(str, filename)
            fphoto = fphoto.resize((_w, _h), Image.ANTIALIAS)
            tkphoto = ImageTk.PhotoImage(fphoto)
            label.configure(image=tkphoto)
            label.image = tkphoto

        def add_ascii(img):
            create.ascii_pic(filename, intensity=10)

        def add_cond_ascii(img):
            create.asc_cond(filename, intensity=5)


# background image
e = Example(web)
e.pack()

# show Window
web.mainloop()
