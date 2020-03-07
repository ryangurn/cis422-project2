"""

ClassInfo.py is is the graphics modules dedicated to the setup and display of
the class information window. It also handles user interaction with the window.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Created:

"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import Notebook, Entry
import StudentModel
import StudentClassModel
import ClassModel

class classInfo(tk.Tk):
    def __init__(self, master, db_file, className):
        """
        Initializer for the MainMenu window. This function requires the name
        of the database to connect and interact with. It also requires the
        master window from tkinter to interface with. It also needs the class
        name so that it can get info on that class from the database.

        :param
        master: tkinter.Tk
        db_file: str
        className: str

        Example Usage:

        """
        self.db = db_file
        self.master = master

        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"

        self.window = Frame(master, bg=self._darkGrey, height=800, width=800)
        self.window.place(x=0, y=0)

        self.windowTop = Frame(self.window, bg = "#323232", height = 125, width = 800)
        self.windowTop.place(x = 0, y= 0)
        # Display class name on top
        labelWidth = 200
        if len(className) > 12:
            labelWidth = 500

        roadMapLabel = Label(self.windowTop, text=className, background="#323232", fg="#ffcc00")
        roadMapLabel.place(x=0, y=5, height=115, width=labelWidth)
        roadMapLabel.config(font=("Helvetica", 44))

        # UO Logo
        logoUO = PhotoImage(file="./img/UOicon.gif")
        labelUO = Label(self.windowTop, image=logoUO, borderwidth = 0)
        labelUO.image = logoUO
        labelUO.place(x=670, y=4)

        greenLine = Label(self.windowTop, text="", background=self._green)
        greenLine.place(x=0, y=120, height=8, width=800)

        instructorLabel = Label(self.window, text = "Instructor: ", bg = self._darkGrey, fg = self._yellow)
        instructorLabel.place(x = 21, y = 175, height = 25, width = 250)
        instructorLabel.config(font = ("Helvetica", 28))

        prereqLabel = Label(self.window, text = "Prerequisites: ", bg = self._darkGrey, fg = self._yellow)
        prereqLabel.place(x = 20, y = 215, height = 25, width = 300)
        prereqLabel.config(font = ("Helvetica", 28))

        termsOffered = Label(self.window, text = "Terms Offered: ", bg = self._darkGrey, fg = self._yellow)
        termsOffered.place(x = 20, y = 255, height = 25, width = 315)
        termsOffered.config(font = ("Helvetica", 28))

        returnButton = Label(self.window, text='Return')
        returnButton.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        returnButton.place(x=600, y= 540, height=30, width=140)
        returnButton.bind(self._button, self.returnClick)

    def returnClick(self, event):
        """
        DESC

        :param

        Example Usage:

        """
        self.windowTop.destroy()
        self.window.destroy()
