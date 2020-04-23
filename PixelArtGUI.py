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

        self.image = Image.open("/Users/jbujarski/PycharmProjects/proj/pixels.jpg")
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
        self.search_word_button = Button(frame, text="Search Word", command=self.search_word)
        self.search_word_button.pack(side=TOP, fill=X)
        self.search_word_button = Button(frame, text="Edit Image", command=self.search_image)
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
            lb1 = Label(win1, text="Image Search By Word", fg='#00ff00', bg='black', font=("Courier", 26))
            lb1.pack()

            ''' WORD SEARCH - NORMAL'''
            lb2 = Label(win1, text="Enter a word below to search for an image via Google", fg='#00ff00', bg='black',
                        font=("Courier", 14))
            lb2.pack(side=TOP)
            frame = Frame(win1)
            frame.pack(side=TOP)
            self.image_entry = Entry(frame, bd=5, width=20)
            self.image_entry.grid(row=0, column=1, columnspan=3, padx=1, pady=1)
            image_button = Button(frame, text="Enter word for Regular Image", font=("Times New Roman", 10),
                                  command=self.image_entry_res)
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
                                    command=self.blended_entry_res)
            blended_button.grid(row=4, column=20, columnspan=3, padx=1, pady=1)

            '''RANDOM IMAGE'''
            lb4 = Label(win1, text="Enter a string to seed a random picture, or leave blank for random seed",
                        fg='#00ff00', bg='black', font=("Courier", 14))
            lb4.pack(side=TOP)
            frame2 = Frame(win1)
            frame2.pack(side=TOP)

            self.random_entry = Entry(frame2, bd=5)
            self.random_entry.pack(side=LEFT, fill=X)
            random_seed_button = Button(frame2, text="Enter word for a Random image", font=("Times New Roman", 10),
                                        command=self.random_entry_res)
            random_seed_button.pack(side=RIGHT, fill=X)

            lb5 = Label(win1, text="Enter an \"intensity\" value, or pixel density (larger = less dense)", fg='#00ff00',
                        bg='black', font=("Courier", 14))
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

    def random_entry_res(self):
        user_input = self.random_entry.get()
        print(user_input)
        self.random_entry.delete(0, END)

        if not self.intensity_entry.get():
            master = create.rand_seed(user_input)
            res_fig = pic.view_pic(master)
            res_fig.show()
        else:
            master = create.rand_seed(user_input, intensity=int(self.intensity_entry.get()))
            res_fig = pic.view_pic(master)
            self.intensity_entry.delete(0, END)
            res_fig.show()

        # opens a new window to search for image(s)
        # by Rainie Dormanen
    def search_image(self):
        try:
            win2 = tk.Toplevel()
            win2.geometry("600x600")
            win2["bg"] = "black"
            lb = Label(win2, text="Upload Image to Edit", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win2)
            frame.pack(side=TOP)

            filename = fd.askopenfilename(initialdir=r"C:\Users", title="Browse Images",
                                          filetypes=(('jpg files', '*.jpg',),
                                                     ('png files', '*.png'),
                                                     ('jpeg files', '*.jpeg')))

            photo = Image.open(filename)
            photo = photo.resize((400, 500), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)  # saves copy of image
            label = Label(win2, image=photo)
            label.image = photo
            label.pack(side=BOTTOM)

            negative_button = Button(frame, text="Negative Image", font=("Times New Roman", 15),
                                          command=lambda: self.add_negative(photo))
            negative_button.pack(pady=10, side=LEFT)

            hue_button = Button(frame, text="Change Image Hue", font=("Times New Roman", 15),
                                     command=lambda: self.add_hue(photo))
            hue_button.pack(pady=10, side=RIGHT)

            ascii_button = Button(frame, text="Convert Image to Ascii", font=("Times New Roman", 15),
                                       command=lambda: self.add_ascii(photo))
            ascii_button.pack(pady=10, side=RIGHT)
        except NameError as e:
            if win2.state() == "normal": win2.focus()

    def add_negative(self, img):
        try:
            win3 = tk.Toplevel()
            win3.geometry("600x600")
            win3["bg"] = "black"
            lb = Label(win3, text="Here is your negative image!", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win3)
            frame.pack(side=TOP)
        except NameError as e:
            if win3.state() == "normal": win3.focus()

    def add_hue(self, img):
        try:
            win4 = tk.Toplevel()
            win4.geometry("600x600")
            win4["bg"] = "black"
            lb = Label(win4, text="Select Hue", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win4)
            frame.pack(side=TOP)

            # add buttons so user can enter hue
            warm_button = Button(frame, text="Add Warm Hue", font=("Times New Roman", 15), 
                                 command =lambda : self.warm(img) )
            warm_button.pack(pady=10, side=TOP)

            verdant_button = Button(frame, text="Add Verdant Hue", font=("Times New Roman", 15), 
                                    command =lambda : self.verdant(img) )
            verdant_button.pack(pady=10, side=BOTTOM)

            cool_button = Button(frame, text="Add Cool Hue", font=("Times New Roman", 15), 
                                 command =lambda : self.cool(img))
            cool_button.pack(pady=10, side=BOTTOM)
        except NameError as e:
            if win4.state() == "normal": win4.focus()


    def add_ascii(self, img):
        try:
            win5 = tk.Toplevel()
            win5.geometry("600x600")
            win5["bg"] = "black"
            lb = Label(win5, text="Here is your ascii image!", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win5)
            frame.pack(side=TOP)

            self.intensity_entry = Entry(frame, bd=5, width=20)
            self.intensity_entry.grid(row=4, column=1, columnspan=3, padx=1, pady=1)
            intensity_button = Button(frame, text="Enter Intensity for Added Fun! (Ex: 100)",
                                      font=("Times New Roman", 10))
            intensity_button.grid(row=4, column=20, columnspan=3, padx=1, pady=1)
        except NameError as e:
            if win5.state() == "normal": win5.focus()
                
    def warm(self, img):
        try:
            if win4.state() == "normal": win4.focus()
        except NameError as e:
            print(e)
            win4 = tk.Toplevel()
            win4.geometry("600x600")
            win4["bg"] = "black"
            lb = Label(win4, text="Here is your WARM image!", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win4)
            frame.pack(side=TOP)
    def verdant(self, img):
        try:
            if win6.state() == "normal": win6.focus()
        except NameError as e:
            print(e)
            win6 = tk.Toplevel()
            win6.geometry("600x600")
            win6["bg"] = "black"
            lb = Label(win6, text="Here is your VERDANT image!", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win6)
            frame.pack(side=TOP)
    def cool(self, img):
        try:
            if win7.state() == "normal": win7.focus()
        except NameError as e:
            print(e)
            win7 = tk.Toplevel()
            win7.geometry("600x600")
            win7["bg"] = "black"
            lb = Label(win7, text="Here is your COOL image!", fg='red', font=("Ink Free", 25))
            lb.pack()
            frame = Frame(win7)
            frame.pack(side=TOP)

                
                


# background image
e = Example(web)
e.pack()

# show Window
web.mainloop()
