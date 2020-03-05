import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
import ClassModel
import StudentClassModel
import StudentModel


# import GUI.classRoadmap


class ClassManagement(tk.Tk):
    def __init__(self, master, studentName, db_file):
        self.db = db_file
        self.master = master
        self.currentSubject = None

        sm = StudentModel.StudentModel(self.db)
        self.student_id = sm.find(studentName)[0][0]

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
        self.window = Frame(master, bg=self._darkGrey, height=800, width=800)
        self.window.place(x=0, y=125)

        self.windowTop = Frame(master, bg=self._grey, height=125, width=800)
        self.windowTop.place(x=0, y=0)

        # UO Logo
        logoUO = PhotoImage(file="./img/UOicon.gif")
        labelUO = Label(self.windowTop, image=logoUO, borderwidth=0)
        labelUO.image = logoUO
        labelUO.place(x=670, y=5)

        # Title of the window (Not top menu)
        title = Label(self.windowTop, text='CLASS SELECTION', borderwidth=0)
        title.config(font=("Arial", 50), bg=self._grey, fg=self._yellow)
        title.place(x=10, y=22, width=500, height=80)

        # Green line
        labelNext = Label(self.windowTop, text="", background=self._green)
        labelNext.place(x=0, y=120, height=8, width=800)

        # Grey Lines that hide the white lines on the logo
        greyLine = Label(self.windowTop, text="", background=self._grey)
        greyLine.place(x=0, y=110, height=8, width=800)
        greyLineTop = Label(self.windowTop, text="", background=self._grey)
        greyLineTop.place(x=0, y=3, height=8, width=800)
        greyLineLeft = Label(self.windowTop, text="", background=self._grey)
        greyLineLeft.place(x=665, y=0, height=120, width=8)
        greyLineRight = Label(self.windowTop, text="", background=self._grey)
        greyLineRight.place(x=785, y=0, height=120, width=8)

        # Taken classes label
        taken = Label(self.window, text="Taken Classes", background=self._green, font=self._buttonText,
                      fg=self._darkGrey)
        taken.place(x=486, y=50, height=self._buttonHeight, width=278)

        # Delete Info Label
        info = Label(self.window, text="Click on a class to delete it", background=self._darkGrey,
                     font=self._buttonText, fg=self._lightGrey)
        info.place(x=486, y=345, height=self._buttonHeight, width=278)

        # Category classes label
        category = Label(self.window, text="Category", background=self._green, font=self._buttonText, fg=self._darkGrey)
        category.place(x=31, y=50, height=self._buttonHeight, width=90)

        # Course classes label
        course = Label(self.window, text="Course", background=self._green, font=self._buttonText, fg=self._darkGrey)
        course.place(x=131, y=50, height=self._buttonHeight, width=315)

        subfont = font.Font(family="Helvetica", size=26)
        courseFont = font.Font(family="Helvetica", size=16)
        self.courseSubjects = Listbox(self.window, selectmode="browse", bg=self._yellow, fg=self._darkGrey,
                                      selectbackground=self._green, font=subfont)
        self.courseSubjects.place(x=30, y=80, height=295, width=92)
        self.courseSubjects.bind(self._button, self.subjectClick)

        cm = ClassModel.ClassModel(self.db)
        subject = cm.distinct('subject')
        for k, v in enumerate(subject):
            self.courseSubjects.insert(k, v[0])

        # "Student" Label
        student = Label(self.window, text='Student:')
        student.place(x=35, y=10, height=40, width=80)
        student.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # Student Name Label (Updates)
        labl = Label(self.window, text=studentName)
        labl.place(x=120, y=15, height=30, width=200)
        labl.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # Offered Classes listbox
        self.offeredCourses = Listbox(self.window, selectmode="browse", bg=self._lightGrey, fg=self._darkGrey,
                                      selectbackground=self._yellow, font=courseFont)
        self.offeredCourses.place(x=130, y=80, height=255, width=317)
        self.offeredCourses.bind(self._button, self.courseClick)

        # Taken Classes listbox
        self.takenClasses = Listbox(self.window, selectmode="browse", bg=self._lightGrey, fg=self._darkGrey,
                                    selectbackground=self._yellow)
        self.takenClasses.place(x=485, y=80, height=205, width=280)
        self.takenClasses.bind(self._button, self.removeClass)

        # add in previously taken classes
        scm = StudentClassModel.StudentClassModel(self.db)
        prev = scm.find('students_id', self.student_id)
        for i in prev:
            class_id = i[2]

            cm = ClassModel.ClassModel(self.db)
            clas = cm.find_by('id', class_id)
            self.takenClasses.insert(END, self._compose(clas))

        # Button Home
        goHome = Label(self.window, text='Home')
        goHome.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        goHome.bind("<Button-1>", self.goHomeClick)
        goHome.place(x=485, y=292, height=self._buttonHeight, width=self._buttonWidth)

        # Button Save
        saveData = Label(self.window, text='Save')
        saveData.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        saveData.bind("<Button-1>", self.saveDataClick)
        saveData.place(x=555, y=292, height=self._buttonHeight, width=self._buttonWidth)

        # Button Roadmap
        roadmap = Label(self.window, text='Class Roadmap')
        roadmap.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        roadmap.bind("<Button-1>", self.classRoadmap)
        roadmap.place(x=625, y=292, height=self._buttonHeight, width=138)

        # Dropdown Menu for years
        self.strObj1 = StringVar(self.window)
        yearChoices = sorted({'2019', '2018', '2017', '2016', '2015'}, reverse=True)
        self.strObj1.set('2019')  # Default value
        dropMenuYear = OptionMenu(self.window, self.strObj1, *yearChoices)
        dropMenuYear.place(x=297, y=345, width=150, height=30)
        dropMenuYear.config(bg=self._darkGrey)
        self.strObj1.trace('w', self.year_dropdown)

        # Dropdown Menu for quarters
        self.strObj2 = StringVar(self.window)
        quarterChoices = sorted({'Fall', 'Winter', 'Spring', 'Summer'})
        self.strObj2.set('Spring')  # Default value
        dropMenuQuarter = OptionMenu(self.window, self.strObj2, *quarterChoices)
        dropMenuQuarter.place(x=131, y=345, width=150, height=30)
        dropMenuQuarter.config(bg=self._darkGrey)
        self.strObj2.trace('w', self.quarter_dropdown)

    def year_dropdown(self, *args):
        self.updateList()

    def quarter_dropdown(self, *args):
        self.updateList()

    def goHomeClick(self, event):
        # mainMenu(self.master)
        self.window.destroy()
        self.windowTop.destroy()

    def saveDataClick(self, event):
        print("Send data to SQL")

    def classRoadmap(self, event):
        print("Send data to SQL")
        ClassRoadmap(self.master, studentName)

    def subjectClick(self, event):
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            value = w.get(index)
            self.currentSubject = value
            self.updateList()

    def updateList(self):
        self.offeredCourses.delete(0, END)  # delete all items
        year = str(self.strObj1.get())
        term = str(self.strObj2.get())

        t = None
        if term == "Fall":
            t = 1
        elif term == "Winter":
            t = 2
        elif term == "Spring":
            t = 3
        elif term == "Summer":
            t = 4

        cm = ClassModel.ClassModel(self.db)
        items = cm.find_by_term(self.currentSubject, year, t)
        for key, value in enumerate(items):
            insertLine = value[3] + " " + value[4] + " - [" + value[2] + "]"
            self.offeredCourses.insert(key, insertLine)

    def courseClick(self, event):
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            currentCourse = w.get(index)
            if not self._contain(currentCourse, self.takenClasses):
                # locate class record
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1])
                class_id = clas[0][0]

                # associate the item
                scm = StudentClassModel.StudentClassModel(self.db)
                scm.associate(self.student_id, class_id)

                # insert item into the list
                self.takenClasses.insert(END, currentCourse)

    def removeClass(self, event):
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            currentCourse = w.get(index)
            MsgBox = tk.messagebox.askquestion('Delete Confirmation',
                                               'Are you sure you would like to delete this class',
                                               icon='warning')
            if MsgBox == 'yes':
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1])
                class_id = clas[0][0]

                scm = StudentClassModel.StudentClassModel(self.db)
                scm.disassociate(self.student_id, class_id)

                self.takenClasses.delete(index)

    def _decompose(self, str):
        split = str.split(" ")
        subject = split[0]
        code = split[1]
        course = " ".join(str.split(" ")[2:]).replace("[", "").replace("]", "")[2:]

        return subject, code, course

    def _compose(self, value):
        v = value[0]
        return v[3] + " " + v[4] + " - [" + v[2] + "]"

    def _contain(self, item, box):
        return item in box.get(0, "end")
