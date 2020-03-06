import tkinter as tk
from tkinter import *
from tkinter import messagebox
import StudentModel

class collectData(tk.Tk):
    def __init__(self, master, db_file):
        self.db = db_file
        self.master = master

        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"

        # Creates a frame to add to the master window
        self.master = master
        self.newWindow = Frame(master, bg = self._darkGrey)
        self.newWindow.place(x = 0, y = 150, height = 600, width = 800)

        # Year label
        yearLabel = Label(self.newWindow, text='Select the Year')
        yearLabel.place(x=100,y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.yearVal = StringVar(self.newWindow)
        #TODO: Just for testing, need to get from DB
        yearChoices = sorted({'2016', '2017', '2018', '2019', '2020'})
        self.yearVal.set('2019')  # Default value
        yearMenu = OptionMenu(self.newWindow, self.yearVal, *yearChoices)
        yearMenu.place(x=100, y=185, width=150, height=30)
        yearMenu.config(bg=self._darkGrey)

        # Subject label
        subjectLabel = Label(self.newWindow, text='Select the Subject')
        subjectLabel.place(x=285,y=150, height=30, width=170)
        subjectLabel.config(font=("Arial Bold", 18))
        subjectLabel.config(bg=self._darkGrey, fg="Grey")

        self.subjectVal = StringVar(self.newWindow)
        #TODO: Just for testing, need to get from DB
        subjectChoices = sorted({'CIS', 'AAP', 'MATH', 'PHY'})
        self.subjectVal.set('CIS')
        subjectMenu = OptionMenu(self.newWindow, self.subjectVal, *subjectChoices)
        subjectMenu.config(bg=self._darkGrey)
        subjectMenu.place(x = 290, y = 185, width = 150, height = 30)

        # Term label
        yearLabel = Label(self.newWindow, text='Select the Term')
        yearLabel.place(x=485,y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.termVal = StringVar(self.newWindow)
        termChoices = sorted({'Spring', 'Summer', 'Fall', 'Winter'})
        self.termVal.set('Spring')
        termMenu = OptionMenu(self.newWindow, self.termVal, *termChoices)
        termMenu.config(bg=self._darkGrey)
        termMenu.place (x = 490, y = 185, width = 150, height = 30)



        # Button to trigger the data collection
        collectData = Label(self.newWindow, text='Collect Data')
        collectData.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        collectData.place(x=225, y= 340, height=30, width=140)
        collectData.bind("<Double-Button-1>", self.dataCollectClick)

        # Button to close the "Select Data" window and go back to main menu
        exitName = Label(self.newWindow, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        exitName.place(x=410, y= 340, height=30, width=140)
        exitName.bind("<Double-Button-1>", self.exitWindow)

    def exitWindow(self, event):
        self.newWindow.destroy()

    def dataCollectClick(self, event):
        print(self.termVal.get())
        print(self.yearVal.get())
        print(self.subjectVal.get())