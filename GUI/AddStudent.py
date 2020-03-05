import tkinter as tk
import csv
from tkinter import *
from tkinter import messagebox
import StudentModel

class AddStudent(tk.Tk):
    def __init__(self, master, db_file, lb):
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
        self.window = Frame(master, bg = self._darkGrey)
        self.window.place(x = 0, y = 150, height = 600, width = 800)

        newName = Label(self.window, text='Enter a new name:')
        newName.place(x=190,y=120, height=30, width=160)
        newName.config(font=("Arial Bold", 16), bg=self._yellow, fg="Black")

        # Adds text entry box to enter the student's name
        self.nameVar = StringVar()
        searchbox = Entry(self.window, textvariable=self.nameVar)
        searchbox.place(x=350,y=120, height=30, width=200)

        # Button to close the "Add Student" window and go back to main menu
        exitName = Label(self.window, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        exitName.place(x=315, y= 340, height=30, width=140)
        exitName.bind(self._button, self.exitWindow)

        # Button to add the student's name to the csv file
        addName = Button(self.window, text='Add', width=25, command=self.addStudentClick)
        addName.place(x=535,y= 120, height=30, width=70)
        addName.config(font=("Arial Bold", 16))

    def exitWindow(self, event):
        self.window.destroy()

    def addStudentClick(self):
        name = self.nameVar.get()
        if name == '':
            messagebox.showwarning("Invalid Name", 'Please enter a valid name.')
            return

        # Writes student name to the csv file and overrides existing one
        sm = StudentModel.StudentModel(self.db)
        sm.insert(name)
        self.lb.insert(END, name)
        self.window.destroy()
