"""

AddStudent.py is the graphics modules dedicated to the setup and display of
the add student window. It also handles user interaction with the window.

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

import StudentModel


class AddStudent(tk.Tk):
    def __init__(self, master, db_file, lb):
        """
        Initializer for the AddStudent window. This function requires the name
        of the database to connect and interact with, the master window from
        tkinter to interface with, and also the Listbox that contains the names
        of the students in the database.

        :param
        master :tkinter.Tk
        db_file :str
        lb :Listbox

        Example Usage:
        //Called from MainMenu.py
        AddStudent(self.master, self.db, self.lb)
        """
        self.db = db_file
        self.master = master
        self.lb = lb

        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"

        # Creates a frame to add to the master window
        self.master = master
        self.window = Frame(master, bg=self._darkGrey)
        self.window.place(x=0, y=150, height=600, width=800)

        newName = Label(self.window, text='Enter a new name:')
        newName.place(x=190, y=120, height=30, width=160)
        newName.config(font=("Arial Bold", 16), bg=self._yellow, fg="Black")

        # Adds text entry box to enter the student's name
        self.nameVar = StringVar()
        searchbox = Entry(self.window, textvariable=self.nameVar)
        searchbox.place(x=350, y=120, height=30, width=200)

        # Button to close the "Add Student" window and go back to main menu
        exitName = Label(self.window, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        exitName.place(x=315, y=340, height=30, width=140)
        exitName.bind(self._button, self.exitWindow)

        # # Button to add the student's name to the csv file
        # addName = Button(self.window, text='Add', width=25, fg='red', command=self.addStudentClick)
        addName = Label(self.window, text='Add', width=25, fg='black')
        addName.place(x=535, y=120, height=30, width=70)
        addName.config(font=("Arial Bold", 16))
        addName.bind(self._button, self.addStudentClick)

    def exitWindow(self, event):
        """
        Function used to exit the AddStudent window and return to MainMenu
        when an event occurs. This function should be bound to an onclick event
        on the exitName button.

        :param
        event :the event type of an item bound to this function

        Example Usage:
        //Binds left mouse click on 'exitName' button to this function
        exitName.bind("<Button-1>", self.exitWindow)
        """
        self.window.destroy()

    def addStudentClick(self, event):
        """
        Function used to add a student to the database when an event occurs.
        This function should be bound to an onclick event on the addName button.

        :param
        event :the event type of an item bound to this function

        Example Usage:
        //Binds left mouse click on 'addName' button to this function
        addName.bind(self._button, self.addStudentClick)
        """
        name = self.nameVar.get()
        if name == '':
            messagebox.showwarning("Invalid Name", 'Please enter a valid name.')
            return

        sm = StudentModel.StudentModel(self.db)
        if len(sm.find(name)) > 0:
            messagebox.showwarning("Name already used", 'Please enter a new name.')
            return

        # Writes student name to the csv file and overrides existing one
        sm.insert(name)
        self.lb.insert(END, name)
        self.window.destroy()
