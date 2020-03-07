"""

CollectData.py is the graphics modules dedicated to the setup and display of
the data collection window. It also handles user interaction with the window.

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
import ClassParser
import ClassModel


class collectData(tk.Tk):
    def __init__(self, master, db_file):
        """
        Initializer for the CollectData window. This function requires the name
        of the database to connect and interact with, the master window from
        tkinter to interface with, and also the Listbox that contains the names
        of the students in the database.

        :param
        master: tkinter.Tk
        db_file: str

        Example Usage:
        //Called from MainMenu.py
        collectData(self.master, self.db)
        """
        self.db = db_file
        self.master = master

        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"
        self.cm = ClassModel.ClassModel(self.db)
        # Creates a frame to add to the master window
        self.master = master
        self.newWindow = Frame(master, bg=self._darkGrey)
        self.newWindow.place(x=0, y=150, height=600, width=800)

        # Year label
        yearLabel = Label(self.newWindow, text='Select the Year')
        yearLabel.place(x=100, y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.yearVal = StringVar(self.newWindow)
        yearChoices = sorted({'2015', '2016', '2017', '2018', '2019', '2020'})
        self.yearVal.set('2020')  # Default value
        yearMenu = OptionMenu(self.newWindow, self.yearVal, *yearChoices)
        yearMenu.place(x=100, y=185, width=150, height=30)
        yearMenu.config(bg=self._darkGrey)

        # Subject label
        subjectLabel = Label(self.newWindow, text='Select the Subject')
        subjectLabel.place(x=285, y=150, height=30, width=170)
        subjectLabel.config(font=("Arial Bold", 18))
        subjectLabel.config(bg=self._darkGrey, fg="Grey")

        self.subjectVal = StringVar(self.newWindow)
        subjectChoices = ["AAAP", "AAD", "ACTG", "AEIS", "AFR", "AIM", "ANTH", "ANTM", "ARB", "ARCH", "ARH", "ART",
                          "ARTC",
                          "ARTD", "ARTF", "ARTM", "ARTO", "ARTP", "ARTR", "ARTS", "ASIA", "ASL", "ASTR", "BA", "BI",
                          "BIKC",
                          "BIOE", "BLST", "CARC", "CAS", "CDS", "CFT", "CH", "CHKC", "CHN", "CHNF", "CINE", "CIS",
                          "CIT", "CLAS",
                          "COLT", "CPSY", "CRDG", "CRES", "CRWR", "CSCH", "DAN", "DANC", "DANE", "DIST", "DSGN", "EALL",
                          "EC",
                          "ECE", "EDLD", "EDST", "EDUC", "ENG", "ENVS", "ERTH", "ES", "ESC", "EURO", "FHS", "FIN",
                          "FINN", "FLR",
                          "FR", "GEOG", "GEOL", "GER", "GRK", "GRST", "GSAE", "GSCL", "GSGE", "GSST", "HBRW", "HC",
                          "HIST",
                          "HPHY", "HUM", "IARC", "ICH", "INTL", "IST", "ITAL", "J", "JDST", "JGS", "JPN", "KC", "KRN",
                          "LA",
                          "LAS", "LAT", "LAW", "LEAD", "LERC", "LIB", "LING", "LT", "MATH", "MDVL", "MENA", "MGMT",
                          "MIL",
                          "MKTG", "MUE", "MUJ", "MUP", "MUS", "NAS", "NORW", "OBA", "OIMB", "OLIS", "PD", "PDX", "PE",
                          "PEAQ",
                          "PEAS", "PEC", "PEF", "PEI", "PEIA", "PEL", "PEMA", "PEMB", "PEO", "PERS", "PERU", "PETS",
                          "PEW",
                          "PHIL", "PHKC", "PHYS", "PORT", "PPPM", "PREV", "PS", "PSY", "QST", "REES", "REL", "RL",
                          "RUSS",
                          "SBUS", "SCAN", "SCYP", "SERV", "SLP", "SOC", "SPAN", "SPD", "SPED", "SPM", "SPSY", "SWAH",
                          "SWED",
                          "TA", "TLC", "UGST", "WGS", "WR"]

        self.subjectVal.set('CIS')
        subjectMenu = OptionMenu(self.newWindow, self.subjectVal, *subjectChoices)
        subjectMenu.config(bg=self._darkGrey)
        subjectMenu.place(x=290, y=185, width=150, height=30)

        # Term label
        yearLabel = Label(self.newWindow, text='Select the Term')
        yearLabel.place(x=485, y=150, height=30, width=150)
        yearLabel.config(font=("Arial Bold", 18))
        yearLabel.config(bg=self._darkGrey, fg="Grey")

        self.termVal = StringVar(self.newWindow)
        termChoices = sorted({'Spring', 'Summer', 'Fall', 'Winter'})
        self.termVal.set('Spring')
        termMenu = OptionMenu(self.newWindow, self.termVal, *termChoices)
        termMenu.config(bg=self._darkGrey)
        termMenu.place(x=490, y=185, width=150, height=30)

        # Button to trigger the data collection
        collectData = Label(self.newWindow, text='Collect Data')
        collectData.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        collectData.place(x=225, y=340, height=30, width=140)
        collectData.bind(self._button, self.dataCollectClick)

        # Button to close the "Select Data" window and go back to main menu
        exitName = Label(self.newWindow, text='Return Home')
        exitName.config(font=("Arial Bold", 18), bg="#369148", fg=self._yellow)
        exitName.place(x=410, y=340, height=30, width=140)
        exitName.bind(self._button, self.exitWindow)

    def exitWindow(self, event):
        """
        Function used to exit the CollectData window and return to MainMenu
        when an event occurs. This function should be bound to an onclick event
        on the exitName button.

        :param
        event: the event type of an item bound to this function

        Example Usage:
        //Binds left mouse click on 'exitName' button to this function
        exitName.bind("<Button-1>", self.exitWindow)
        """
        self.newWindow.destroy()

    def dataCollectClick(self, event):
        """
        This function is used to update course data for a specific subject and
        term. It parses data from classes.uoregon.edu and updates the database
        with the latest course information. This function will be called when
        a bound event occurs.

        :param
        event: the event type of an item bound to this function

        Example Usage:
        //Binds left mouse click on collectData button to this function
        collectData.bind("<Button-1>", self.dataCollectClick)
        """
        term = self.termVal.get()
        year = self.yearVal.get()
        t = None
        y = int(year)
        if term == "Fall":
            t = 1
        elif term == "Winter":
            y -= 1
            t = 2
        elif term == "Spring":
            y -= 1
            t = 3
        elif term == "Summer":
            y -= 1
            t = 4

        ye = str(y)
        s = ye + "0" + str(t)
        currentClasses = self.cm.find_by_term(self.subjectVal.get(), y, t)
        if len(currentClasses):
            self.cm.delete_sub_term(self.subjectVal.get(), s)

        p = ClassParser.ClassParser(s, self.subjectVal.get())
        p.deleteFormatting()
        p.parseData()
