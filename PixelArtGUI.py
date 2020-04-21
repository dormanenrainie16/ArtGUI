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
            lb = Label(win1, text="Enter a word to get pixel image", fg='red', font=("Ink Free", 26))
            lb.pack()
            frame = Frame(win1)
            frame.pack(side=TOP)
            self.entry = Entry(frame, bd=5)
            self.entry.pack(side=TOP, fill=X)
            Enter_button = Button(frame, text="Enter", font=("Times New Roman", 10), command=self.entry_res)
            Enter_button.pack(side=BOTTOM, fill=X)

    # Stores the results of the entry box (user input) and clears the entry box after
    # Probably should do the algorithm in this function as well
    def entry_res(self):
        user_input = ""
        user_input = self.entry.get()
        #print(user_input)
        self.entry.delete(0, END)

    # opens a new window to search for image(s)
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
            frame.pack(side=BOTTOM)


# background image
e = Example(web)
e.pack()

# show Window
web.mainloop()
