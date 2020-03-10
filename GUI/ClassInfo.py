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

import json
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Notebook, Entry

import ClassModel


class classInfo(tk.Tk):
    def __init__(self, master, db_file, className, class_id):
        """
        Initializer for the MainMenu window. This function requires the name
        of the database to connect and interact with. It also requires the
        master window from tkinter to interface with. It also needs the class
        name so that it can get info on that class from the database.

        :param
        master :tkinter.Tk
        db_file :str
        className :str
        class_id :str

        Example Usage:

        """
        print("|--------------------------------|")
        print("|- warning there may be a font -|")
        print("|-    error that shows below    -|")
        print("|-   there is nothing to worry  -|")
        print("|- about just a macOS coretext  -|")
        print("|-             error            -|")
        print("|-        NO ACTION NEEDED      -|")
        print("|--------------------------------|")

        self.db = db_file
        self.master = master

        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._grey = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"

        self.window = Frame(master, bg=self._darkGrey, height=800, width=800)
        self.window.place(x=0, y=0)

        self.windowTop = Frame(self.window, bg="#323232", height=125, width=800)
        self.windowTop.place(x=0, y=0)
        # Display class name on top
        labelWidth = 200
        if len(className) > 12:
            labelWidth = 500

        cm = ClassModel.ClassModel(self.db)
        self.classRecord = cm.find_by('id', class_id)[0]
        self.sections = json.loads(self.classRecord[11])

        roadMapLabel = Label(self.windowTop, text=className, background="#323232",
                             fg="#ffcc00")
        roadMapLabel.place(x=0, y=5, height=115, width=labelWidth)
        roadMapLabel.config(font=("Helvetica", 44))

        # UO Logo
        logoUO = PhotoImage(file="./img/UOicon.gif")
        labelUO = Label(self.windowTop, image=logoUO, borderwidth=0)
        labelUO.image = logoUO
        labelUO.place(x=670, y=4)

        # Grey Lines that hide the white lines on the logo
        greyLine = Label(self.windowTop, text="", background=self._grey)
        greyLine.place(x=0, y=110, height=8, width=800)
        greyLineTop = Label(self.windowTop, text="", background=self._grey)
        greyLineTop.place(x=0, y=3, height=8, width=800)
        greyLineLeft = Label(self.windowTop, text="", background=self._grey)
        greyLineLeft.place(x=665, y=0, height=120, width=8)
        greyLineRight = Label(self.windowTop, text="", background=self._grey)
        greyLineRight.place(x=785, y=0, height=120, width=8)

        greenLine = Label(self.windowTop, text="", background=self._green)
        greenLine.place(x=0, y=120, height=8, width=800)

        # details box is where all of the statistics information will go
        detailsBox = Text(self.window, wrap=WORD, background=self._grey, selectbackground=self._green, fg="#e6e6e6")
        detailsBox.place(x=20, y=195, height=285, width=760)
        detailsBox.config(font=("Arial", 12))

        # get the description
        description = []
        prereqs = []
        locations = []
        for item in self.sections:
            if item['description'] != "" and (item['type'] == "" or item['type'] == "Lecture"):
                description.append(item['description'])
            if item['prereqs'] != "":
                prereqs.append(item['prereqs'])
            if item['location'] != "":
                locations.append(item['location'])

        # insert the description, prereqs, and locations
        detailsBox.insert("1.0", "Description: \n" + "\n".join(description) + "\n")
        detailsBox.insert("20.0", "Prerequisites: \n" + "\n".join(prereqs) + "\n")
        detailsBox.insert("30.0", "Locations: \n" + "\n".join(locations) + "\n")
        detailsBox.insert("40.0", "Previous Section Distribution: \n")

        # get section distribution
        cm1 = ClassModel.ClassModel(self.db)
        counts = cm1.count(self.classRecord[3], self.classRecord[4])
        totalDict = {}
        lecDict = {}
        labDict = {}
        disDict = {}
        othDict = {}
        for c in counts:
            item = c[0]
            year = str(item)[:4]
            t = int(str(item)[5:])
            term = None
            if t == 1:
                term = "Fall"
            elif t == 2:
                term = "Winter"
                year = str(int(year) + 1)
            elif t == 3:
                term = "Spring"
                year = str(int(year) + 1)
            elif t == 4:
                term = "Summer"
                year = str(int(year) + 1)
            total = c[3]
            lecture = c[4]
            lab = c[5]
            disc = c[6]
            other = c[7]
            if totalDict.get(t):
                totalDict.update({year + " " + term: totalDict[term]+total})
            else:
                totalDict.update({year + " " + term: total})

            if lecDict.get(t):
                lecDict.update({year + " " + term: lecDict[term]+lecture})
            else:
                lecDict.update({year + " " + term: lecture})

            if labDict.get(t):
                labDict.update({year + " " + term: labDict[term]+lab})
            else:
                labDict.update({year + " " + term: lab})

            if disDict.get(t):
                disDict.update({year + " " + term: disDict[term]+disc})
            else:
                disDict.update({year + " " + term: disc})

            if othDict.get(t):
                othDict.update({year + " " + term: othDict[term]+other})
            else:
                othDict.update({year + " " + term: other})

            it = 50.0
            for v in totalDict:
                concat = "(Total: {}, Lecture: {}, Lab: {}, Discussions: {}, Other: {})".format(totalDict[v], lecDict[v], labDict[v], disDict[v], othDict[v])
                detailsBox.insert(it, v + ": " + concat + "\n")
                it += 10.0

        returnButton = Label(self.window, text='Return')
        returnButton.config(font=("Arial Bold", 18), bg=self._green, fg=self._yellow)
        returnButton.place(x=600, y=540, height=30, width=140)
        returnButton.bind(self._button, self.returnClick)

    def returnClick(self, event):
        """
        This function will exit from the class info display and take us back to the roadmap

        event :param

        Example Usage:
        self.returnClick(None)
        """
        self.windowTop.destroy()
        self.window.destroy()
