import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font

class ClassMgmt(tk.Tk):
    def __init__(self, master, studentName):

        self._lightGrey = "#b8b8b8"
        self._grey = "#323232"
        self._darkGrey = "#282929"
        self._yellow = "#ffcc00"
        self._green = "#369148"
        self._button = "<Double-Button-1>"
        self._buttonHeight = 30
        self._buttonWidth = 60
        self._buttonText = ("Arial Bold", 16)

        self.master = master
        self.window = Frame(master, bg = self._darkGrey, height = 800, width = 800)
        self.window.place(x = 0, y = 125)

        self.windowTop = Frame(master, bg =self._grey, height = 125, width = 800)
        self.windowTop.place(x = 0, y = 0)

        # UO Logo
        logoUO = PhotoImage(file="UOicon.gif")
        labelUO = Label(self.windowTop, image = logoUO, borderwidth = 0)
        labelUO.image = logoUO
        labelUO.place(x=670,y=5)

        # Title of the window (Not top menu)
        title = Label(self.windowTop, text='CLASS SELECTION', borderwidth = 0)
        title.config(font=("Arial", 50), bg=self._grey, fg=self._yellow)
        title.place(x=10, y=22, width=500, height=80)
        
        # Green line
        labelNext=Label(self.windowTop, text="", background=self._green)
        labelNext.place(x=0,y=120, height=8, width=800)

        # Grey Lines that hide the white lines on the logo
        greyLine=Label(self.windowTop, text="", background=self._grey)
        greyLine.place(x=0,y=110, height=8, width=800)
        greyLineTop=Label(self.windowTop, text="", background=self._grey)
        greyLineTop.place(x=0,y=3, height=8, width=800)
        greyLineLeft=Label(self.windowTop, text="", background=self._grey)
        greyLineLeft.place(x=665,y=0, height=120, width=8)
        greyLineRight=Label(self.windowTop, text="", background=self._grey)
        greyLineRight.place(x=785,y=0, height=120, width=8)

        # Taken classes label
        taken=Label(self.window, text="Taken Classes", background=self._green, font=self._buttonText, fg=self._darkGrey)
        taken.place(x=486,y=50, height=self._buttonHeight, width=278)

        # Delete Info Label
        info=Label(self.window, text="Click on a class to delete it", background=self._darkGrey, font=self._buttonText, fg=self._lightGrey)
        info.place(x=486,y=345, height=self._buttonHeight, width=278)

        # Category classes label
        category=Label(self.window, text="Category", background=self._green, font=self._buttonText, fg=self._darkGrey)
        category.place(x=31,y=50, height=self._buttonHeight, width=90)

        # Course classes label
        course=Label(self.window, text="Course", background=self._green, font=self._buttonText, fg=self._darkGrey)
        course.place(x=131,y=50, height=self._buttonHeight, width=315)

        subfont = font.Font(family="Helvetica", size=26)
        courseFont = font.Font(family = "Helvetica", size = 16)
        self.courseSubjects = Listbox(self.window, selectmode="browse", bg=self._yellow, fg= self._darkGrey, selectbackground=self._green, width = 6, font = subfont)
        self.courseSubjects.place(x = 30, y = 80, height = 295)
        self.courseSubjects.bind(self._button, self.subjectClick)

        #TODO: Iterate through SQL subjects, insert into this listbox accordingly
        # Inserts listbox 1 data 
        self.courseSubjects.insert(0, "CIS")
        self.courseSubjects.insert(1, "MATH")
        self.courseSubjects.insert(2, "ENG")

        # "Student" Label
        student = Label(self.window, text='Student:')
        student.place(x=35,y=10, height=40, width=80)
        student.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # Student Name Label (Updates)
        labl = Label(self.window, text= studentName)
        labl.place(x=120,y=15, height=30, width=200)
        labl.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # Offered Classes listbox
        self.offeredCourses = Listbox(self.window, selectmode = "browse", bg = self._lightGrey, fg= self._darkGrey, selectbackground=self._yellow, width = 35, font = courseFont)
        self.offeredCourses.place(x = 130, y = 80, height = 255)
        self.offeredCourses.bind(self._button, self.courseClick)

        # Taken Classes listbox
        self.takenClasses = Listbox(self.window, selectmode = "browse", bg = self._lightGrey, fg= self._darkGrey, selectbackground=self._yellow)
        self.takenClasses.place(x = 485, y = 80, height = 205, width = 280)
        self.takenClasses.bind(self._button, self.removeClass)

        # Button Home
        goHome = Label(self.window, text='Home')
        goHome.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        goHome.bind("<Button-1>", self.goHomeClick)
        goHome.place(x = 485, y = 292, height = self._buttonHeight, width=self._buttonWidth)

        # Button Save
        saveData = Label(self.window, text='Save')
        saveData.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        saveData.bind("<Button-1>", self.saveDataClick)
        saveData.place(x = 555, y = 292, height = self._buttonHeight, width=self._buttonWidth)

        # Button Roadmap
        roadmap = Label(self.window, text='Class Roadmap')
        roadmap.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        roadmap.bind("<Button-1>", self.classRoadmap)
        roadmap.place(x = 625, y = 292, height = self._buttonHeight, width=138)

        # Dropdown Menu for years
        self.strObj1 = StringVar(self.window)
        yearChoices = sorted({'2019', '2018', '2017', '2016', '2015'}, reverse=True)
        self.strObj1.set('2019') # Default value
        dropMenuYear = OptionMenu(self.window, self.strObj1, *yearChoices)
        dropMenuYear.place(x=297, y=345, width=150, height=30)
        dropMenuYear.config(bg = self._darkGrey)
        self.strObj1.trace('w', self.year_dropdown)

        # Dropdown Menu for quarters
        self.strObj2 = StringVar(self.window)
        quarterChoices = sorted({'Fall', 'Winter', 'Spring', 'Summer'})
        self.strObj2.set('Fall') # Default value
        dropMenuQuarter = OptionMenu(self.window, self.strObj2, *quarterChoices)
        dropMenuQuarter.place(x=131, y=345, width=150, height=30)
        dropMenuQuarter.config(bg = self._darkGrey)
        self.strObj2.trace('w', self.quarter_dropdown)


    def year_dropdown(self, *args):
        global dropdown
        dropdown = str(self.strObj1.get())
        print(dropdown)

    def quarter_dropdown(self, *args):
        global dropdown
        dropdown = str(self.strObj2.get())
        print(dropdown)

    def goHomeClick(self, event):
        #mainMenu(self.master)
        self.window.destroy()
        self.windowTop.destroy()
    
    def saveDataClick(self, event):
        print("Send data to SQL")

    def classRoadmap(self, event):
        print("Send data to SQL")
        ClassRoadmap(self.master, studentName)

    def subjectClick(self, event):
        #TODO: will likely have to modify this as we will be importing from a sql database
        
        # Index of the listbox selection
        w = event.widget
        index = int(w.curselection()[0])

        # Value of the listbox selection (Class name)
        value = w.get(index)

        # Erases all classes so they aren't re-added in 2nd menu
        self.offeredCourses.delete(0, END)

        # If the value is "CIS", populate
        if value == "CIS":
            self.offeredCourses.insert(END, "CIS DATA 1")
            self.offeredCourses.insert(END, "CIS DATA 2")
            self.offeredCourses.insert(END, "CIS DATA 3")


    def courseClick(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        currentCourse = w.get(index)

        self.takenClasses.insert(END, currentCourse)
        
    def removeClass(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        MsgBox = tk.messagebox.askquestion ('Delete Confirmation','Are you sure you would like to delete this class', icon = 'warning')
        if MsgBox == 'yes':
            self.takenClasses.delete(index)
        
