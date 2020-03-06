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
        self.window = Frame(master, bg = self._darkGrey)
        self.window.place(x = 0, y = 150, height = 600, width = 800)

        # Year label
        yearLabel = Label(self.window, text='Select the Year')
        yearLabel.place(x=100,y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.yearVal = StringVar(self.window)
        #TODO: Just for testing, need to get from DB
        yearChoices = sorted({'2016', '2017', '2018', '2019', '2020'})
        self.yearVal.set('2019')  # Default value
        yearMenu = OptionMenu(self.window, self.yearVal, *yearChoices)
        yearMenu.place(x=100, y=185, width=150, height=30)
        yearMenu.config(bg=self._darkGrey)
        self.yearVal.trace('u', yearMenu)

        # Subject label
        subjectLabel = Label(self.window, text='Select the Subject')
        subjectLabel.place(x=285,y=150, height=30, width=170)
        subjectLabel.config(font=("Arial Bold", 18))
        subjectLabel.config(bg=self._darkGrey, fg="Grey")

        self.subjectVal = StringVar(self.window)
        #TODO: Just for testing, need to get from DB
        subjectChoices = sorted({'CIS', 'AAP', 'MATH', 'PHY'})
        self.subjectVal.set('CIS')
        subjectMenu = OptionMenu(self.window, self.subjectVal, *subjectChoices)
        subjectMenu.config(bg=self._darkGrey)
        subjectMenu.place(x = 290, y = 185, width = 150, height = 30)
        self.subjectVal.trace('u', subjectMenu)

        # Term label
        yearLabel = Label(self.window, text='Select the Term')
        yearLabel.place(x=485,y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.termVal = StringVar(self.window)
        termChoices = sorted({'Spring', 'Summer', 'Fall', 'Winter'})
        self.termVal.set('Spring')
        termMenu = OptionMenu(self.window, self.termVal, *termChoices)
        termMenu.config(bg=self._darkGrey)
        termMenu.place (x = 490, y = 185, width = 150, height = 30)
        self.termVal.trace('u', termMenu)



        # Button to trigger the data collection
        collectData = Label(self.window, text='Collect Data')
        collectData.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        collectData.place(x=225, y= 340, height=30, width=140)
        collectData.bind(self._button, self.dataCollectClick)

        # Button to close the "Select Data" window and go back to main menu
        exitName = Label(self.window, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        exitName.place(x=410, y= 340, height=30, width=140)
        exitName.bind(self._button, self.exitWindow)

    def exitWindow(self, event):
        #TODO: Fix this bug " TypeError: 'OptionMenu' object is not callable "
        self.window.destroy()

    def dataCollectClick(self, event):
        print ("Collect data from DB given termVal, subjectVal, yearVal")