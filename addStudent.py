import tkinter as tk
import csv
from tkinter import *
from tkinter import messagebox

class addStudent(tk.Tk):
    def __init__(self, master):
        self.newWindow = Frame(master,  bg = "#003011", height = 400, width = 810)
        self.newWindow.place(x = 0, y = 200)
        self.nameVar = StringVar()
       
        newName = Label(self.newWindow, text='Enter a new name:')
        newName.place(x=170,y=120, height=30, width=220)
        newName.config(bg="#ffcc00", fg="Black")
        newName.config(font=("Arial Bold", 16))

        # Adds text entry box to enter the student's name
        searchbox = Entry(self.newWindow, textvariable=self.nameVar)
        searchbox.place(x=350,y=120, height=30, width=200)

        # Button to close the "Add Student" window and go back to main menu
        exitName = Button(self.newWindow, text='<-- Back', width=25, command=self.exitWindow)
        exitName.config(font=("Arial Bold", 20))
        exitName.place(x=300, y= 300, height=30, width=140)

        # Button to add the student's name to the csv file
        addName = Button(self.newWindow, text='Add', width=25, command=self.addStudentClick)
        addName.place(x=535,y= 120, height=30, width=70)
        addName.config(font=("Arial Bold", 16))
    
    def exitWindow(self):
        self.newWindow.destroy()
    
    def addStudentClick(self):
        name = self.nameVar.get()
        if(name == ''):
            messagebox.showwarning("Invalid Name",'Please enter a valid name.')
            return

        # Writes student name to the csv file and overrides existing one
        with open('names.csv', 'a+') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow([name])
        return 1