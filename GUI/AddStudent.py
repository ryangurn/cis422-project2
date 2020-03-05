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
        self.newWindow = Frame(master, bg="#262929", height=400, width=810)
        self.newWindow.place(x=0, y=150)
        self.nameVar = StringVar()

        newName = Label(self.newWindow, text='Enter a new name:')
        newName.place(x=190, y=120, height=30, width=160)
        newName.config(bg="#ffcc00", fg="Black")
        newName.config(font=("Arial Bold", 16))

        # Adds text entry box to enter the student's name
        searchbox = Entry(self.newWindow, textvariable=self.nameVar)
        searchbox.place(x=350, y=120, height=30, width=200)

        # Button to close the "Add Student" window and go back to main menu
        exitName = Label(self.newWindow, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg="#ffcc00")
        exitName.place(x=315, y=340, height=30, width=140)
        exitName.bind("<Double-Button-1>", self.exitWindow)

        # Button to add the student's name to the csv file
        addName = Button(self.newWindow, text='Add', width=25, command=self.addStudentClick)
        addName.place(x=535, y=120, height=30, width=70)
        addName.config(font=("Arial Bold", 16))

    def exitWindow(self, event):
        self.newWindow.destroy()

    def addStudentClick(self):
        name = self.nameVar.get()
        if name == '':
            messagebox.showwarning("Invalid Name", 'Please enter a valid name.')
            return

        # Writes student name to the csv file and overrides existing one
        sm = StudentModel.StudentModel(self.db)
        sm.insert(name)
        self.lb.insert(END, name)
        self.newWindow.destroy()
