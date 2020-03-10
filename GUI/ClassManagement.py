"""

ClassManagement.py is is the graphics modules dedicated to the setup and display of
the class roadmap and class selection window. It also handles user interaction with
the window.

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
from datetime import date, datetime
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Notebook, Entry

import ClassModel
import RequirementModel
import StudentClassModel
import StudentModel
import TogglesModel
from GUI.ClassInfo import *


class ClassManagement(tk.Tk):
    def __init__(self, master, studentName, db_file):
        """
        Initializer for the ClassManagement window. This function requires  the master window from
        tkinter to interface with, the name of the database to connect and interact with,
        and also the name of the selected student.

        :param
        master :tkinter.Tk
        studentName :str
        db_file :str

        Example Usage:
        //Called from MainMenu.py
        ClassManagement(self.master, self.db, "Steve Smith")
        """
        self.db = db_file
        self.master = master
        self.currentSubject = None

        # Interact with database and find students ID
        sm = StudentModel.StudentModel(self.db)
        self.student_id = sm.find(studentName)[0][0]

        self._lightGrey = "#b8b8b8"
        self._grey = "#323232"
        self._darkGrey = "#282929"
        self._yellow = "#ffcc00"
        self._green = "#369148"
        self._button = "<Button-1>"
        self._buttonHeight = 30
        self._buttonWidth = 150
        self._buttonText = ("Arial Bold", 16)
        self._offeredCoursesDefault = "Please select a subject to display courses."

        # Create the main frame
        self.studentName = studentName
        self.master = master
        self.window = Frame(master, bg=self._darkGrey, height=800, width=800)
        self.window.place(x=0, y=125)

        # Create the top frame for Title & UO logo
        self.windowTop = Frame(master, bg=self._grey, height=125, width=800)
        self.windowTop.place(x=0, y=0)

        # UO Logo
        logoUO = PhotoImage(file="./img/UOicon.gif")
        labelUO = Label(self.windowTop, image=logoUO, borderwidth=0)
        labelUO.image = logoUO
        labelUO.place(x=670, y=4)

        # Title of the window (Not top menu)
        title = Label(self.windowTop, text='CLASS SELECTION', borderwidth=0, anchor='w')
        title.config(font=("Arial", 44), bg=self._grey, fg=self._yellow)
        title.place(x=40, y=22, width=500, height=80)

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
        taken.place(x=468, y=50, height=self._buttonHeight, width=310)

        # Delete Info Label
        info = Label(self.window, text="Double Click on a class to delete it", background=self._darkGrey,
                     font=self._buttonText, fg=self._lightGrey)
        info.place(x=468, y=345, height=self._buttonHeight, width=310)

        # Category classes label
        category = Label(self.window, text="Subject", background=self._green, font=self._buttonText, fg=self._darkGrey)
        category.place(x=22, y=50, height=self._buttonHeight, width=100)

        # Course classes label
        course = Label(self.window, text="Course", background=self._green, font=self._buttonText, fg=self._darkGrey)
        course.place(x=130, y=50, height=self._buttonHeight, width=316)

        subfont = font.Font(family="Helvetica", size=26)
        courseFont = font.Font(family="Helvetica", size=16)

        # Listbox for the subjects offered at the UO
        self.courseSubjects = Listbox(self.window, selectmode="browse", bg=self._yellow, fg=self._darkGrey,
                                      selectbackground=self._green, width=6, font=subfont)
        self.courseSubjects.place(x=22, y=80, height=295, width=100)
        self.courseSubjects.bind(self._button, self.subjectClick)

        # Interact with the database, then insert every subject into courseSubjects
        cm = ClassModel.ClassModel(self.db)
        subject = cm.distinct('subject')
        for k, v in enumerate(subject):
            self.courseSubjects.insert(k, v[0])

        # "Student" Label
        studentName = "Student: " + studentName
        student = Label(self.window, text=studentName, anchor='w')
        student.place(x=22, y=10, height=40, width=500)
        student.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # Offered Classes listbox
        self.offeredCourses = Listbox(self.window, selectmode="browse", bg=self._lightGrey, fg=self._darkGrey,
                                      selectbackground=self._yellow, width=35, font=courseFont)
        self.offeredCourses.insert(END, self._offeredCoursesDefault)
        self.offeredCourses.place(x=130, y=80, height=255, width=316)
        self.offeredCourses.bind(self._button, self.courseClick)

        # Taken Classes listbox
        self.takenClasses = Listbox(self.window, selectmode="browse", bg=self._lightGrey, fg=self._darkGrey,
                                    selectbackground=self._yellow)
        self.takenClasses.place(x=468, y=80, height=215, width=310)
        self.takenClasses.bind(self._button, self.removeClass)

        # Interact with database then fill takenClasses box in with previously taken classes
        scm = StudentClassModel.StudentClassModel(self.db)
        prev = scm.find('students_id', self.student_id)
        for i in prev:
            class_id = i[2]

            cm = ClassModel.ClassModel(self.db)
            # Find class based off of class id
            clas = cm.find_by('id', class_id)
            year = str(clas[0][1])[:4]
            term = str(clas[0][1])[4:]

            # Determine term and year class was taken
            y = int(year)
            t = None
            if term == "01":
                t = "Fall"
            elif term == "02":
                t = "Winter"
                y += 1
            elif term == "03":
                t = "Spring"
                y += 1
            elif term == "04":
                t = "Summer"
                y += 1

            self.takenClasses.insert(END, "(" + t + " " + str(y) + ") " + self._compose(clas))

        # Button Home
        goHome = Label(self.window, text='Home')
        goHome.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        goHome.bind(self._button, self.goHomeClick)
        goHome.place(x=468, y=305, height=self._buttonHeight, width=self._buttonWidth)

        # Button Roadmap
        roadmap = Label(self.window, text='Class Roadmap')
        roadmap.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        roadmap.bind(self._button, self.classRoadmap)
        roadmap.place(x=628, y=305, height=self._buttonHeight, width=self._buttonWidth)

        # Dropdown Menu for years
        self.strObj1 = StringVar(self.window)
        yearChoices = sorted({'2020', '2019', '2018', '2017', '2016', '2015'}, reverse=True)
        self.strObj1.set('2020')  # Default value
        dropMenuYear = OptionMenu(self.window, self.strObj1, *yearChoices)
        dropMenuYear.place(x=290, y=345, width=155, height=30)
        dropMenuYear.config(bg=self._darkGrey)
        self.strObj1.trace('w', self.year_dropdown)

        # Dropdown Menu for quarters
        self.strObj2 = StringVar(self.window)
        quarterChoices = sorted({'Fall', 'Winter', 'Spring', 'Summer'})
        self.strObj2.set('Winter')  # Default value
        dropMenuQuarter = OptionMenu(self.window, self.strObj2, *quarterChoices)
        dropMenuQuarter.place(x=130, y=345, width=155, height=30)
        dropMenuQuarter.config(bg=self._darkGrey)
        self.strObj2.trace('w', self.quarter_dropdown)

        # Drop down menu for the student's major
        self.majorChoice = StringVar(self.window)
        majorChoices = sorted({"BS-Computer & Information Science", "BA-Computer & Information Science"})
        self.majorChoice.set("BS-Computer & Information Science")
        majorMenu = OptionMenu(self.window, self.majorChoice, *majorChoices)
        majorMenu.config(bg=self._darkGrey)
        majorMenu.place(x=130, y=385, width=315, height=30)

    def year_dropdown(self, *args):
        """
        Update the OfferedClasses list each time a new year is selected
        :param args:
        :return:
        """
        self.updateList()

    def quarter_dropdown(self, *args):
        """
        Update the OfferedClasses list each time a new term is selected
        :param args:
        :return:
        """
        self.updateList()

    def goHomeClick(self, event):
        """
        Return to the main menu
        :param event:
        :return:
        """
        self.window.destroy()
        self.windowTop.destroy()

    def classRoadmap(self, event):
        """
        Initializer for the classRoadMap window. The purpose of this window is to display
        a student's progress of their major's requirements.
        :param event:
        :return:
        """
        self.idx = 0
        # An array which will store the student's completed classes
        self.comparisonArray = []

        # Determine the student's id
        scm = StudentClassModel.StudentClassModel(self.db)
        iters = scm.find('students_id', self.student_id)
        for i in iters:
            cm = ClassModel.ClassModel(self.db)
            asdf = cm.find_by('id', i[2])[0]
            # Add each class the student has taken to the comparison array
            self.comparisonArray.append(asdf[3] + " " + asdf[4])

        self.toggleArray = {}
        tm = TogglesModel.TogglesModel(self.db)
        tIters = tm.find(self.student_id)
        for t in tIters:
            rm = RequirementModel.RequirementModel(self.db)
            req = rm.find_by('id', t[1])
            term = req[0][1]
            self.toggleArray.update({term: t[3]})

        def box1_update():
            """
            Updates listbox 1 with class data given the key
            :return:
            """
            self.listBx1
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx]]))):
                self.listBx1.insert(0, classMap[self.classMapKeys[self.idx]][i])

            # add coloring to the listboxes
            for i, v in enumerate(self.listBx1.get(0, END)):
                if '\n' in v:
                    box = len(v.split('\n')[1:]) - 1
                    if self.toggleArray.get(box) != None and self.toggleArray.get(box) in v:
                        self.listBx1.itemconfig(i, bg=self._green)
                for c in self.comparisonArray:
                    if c in v:
                        self.listBx1.itemconfig(i, bg=self._green)
                        # print(0, i, v)
                # pass

        def box2_update():
            """
            Updates listbox 2 with class data given the key
            :return:
            """
            self.listBx2
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 1]]))):
                self.listBx2.insert(0, classMap[self.classMapKeys[self.idx + 1]][i])

            # add coloring to the listboxes
            for i, v in enumerate(self.listBx2.get(0, END)):
                if '\n' in v:
                    box = len(v.split('\n')[1:]) - 1
                    if self.toggleArray.get(box) != None and self.toggleArray.get(box) in v:
                        self.listBx2.itemconfig(i, bg=self._green)
                for c in self.comparisonArray:
                    if c in v:
                        self.listBx2.itemconfig(i, bg=self._green)
                pass

        def box3_update():
            """
            Updates listbox 3 with class data given the key
            :return:
            """
            self.listBx3
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 2]]))):
                self.listBx3.insert(0, classMap[self.classMapKeys[self.idx + 2]][i])
                # self.listBx3.itemconfig(0, {'bg': 'red'})

            # add coloring to the listboxes
            for i, v in enumerate(self.listBx3.get(0, END)):
                if '\n' in v:
                    box = len(v.split('\n')[1:]) - 1
                    if self.toggleArray.get(box) != None and self.toggleArray.get(box) in v:
                        self.listBx3.itemconfig(i, bg=self._green)
                for c in self.comparisonArray:
                    if c in v:
                        self.listBx3.itemconfig(i, bg=self._green)
                pass

        def box4_update():
            """
            Updates listbox 4 with class data given the key
            :return:
            """
            self.listBx4
            # if len(classMap[self.classMapKeys[self.idx + 3]]):
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 3]]))):
                self.listBx4.insert(0, classMap[self.classMapKeys[self.idx + 3]][i])

            # add coloring to the listboxes
            for i, v in enumerate(self.listBx4.get(0, END)):
                if '\n' in v:
                    box = len(v.split('\n')[1:]) - 1
                    if self.toggleArray.get(box) != None and self.toggleArray.get(box) in v:
                        self.listBx4.itemconfig(i, bg=self._green)
                for c in self.comparisonArray:
                    if c in v:
                        self.listBx4.itemconfig(i, bg=self._green)
                pass

        def selectedClass(event):
            """
            This is the event handler for the double click action on the class roadmap page.
            This will handle the calling of the ClassInfo class and the creation of the
            roadmaps_toggles when a general course is double clicked.
            :param event:
            :return:
            """
            w = event.widget
            if not w.curselection() == ():
                index = int(w.curselection()[0])
                selectedCourse = w.get(index).split(" ")
                boxindex = len(w.get(index).split('\n')[1:]) - 1
                if boxindex >= 0:
                    tm = TogglesModel.TogglesModel(self.db)
                    rm = RequirementModel.RequirementModel(self.db)
                    # Determine the requirements for the student's selected major
                    splitMajor = self.majorChoice.get().split("-")
                    req = rm.find_by_term(splitMajor[1], splitMajor[0], boxindex)
                    requirements_id = req[0][0]
                    exists = len(
                        tm.find_using(requirements_id, self.student_id, " ".join(w.get(index).split('\n')[:1])))
                    if exists > 0:
                        tm.delete(requirements_id, self.student_id, " ".join(w.get(index).split('\n')[:1]))

                    else:
                        tm.insert(requirements_id, self.student_id, " ".join(w.get(index).split('\n')[:1]))
                if "-" in selectedCourse:
                    del selectedCourse[0]
                cm = ClassModel.ClassModel(self.db)
                try:
                    idx = cm.predict_future_class_id(selectedCourse[0], selectedCourse[1])
                    # Display class info of the selected class
                    classInfo(self.master, self.db, selectedCourse, idx[0][1])
                except IndexError:
                    pass

        def update_next(event):
            """
            Function for the "Next" button
            :param event:
            :return:
            """
            self.idx
            # Checks to see if end has been reached
            if (self.idx >= (len(classMap) - 4)):
                return
            else:
                # Sets button to green
                buttonPrev.config(background="#369148", fg="#e6e6e6")

                if ((self.idx >= len(classMap) - 5)):
                    # Sets button to grey
                    buttonNext.config(background="#808080", fg="#e6e6e6")

                self.idx += 1
                # Erases listboxes
                self.listBx1.delete(0, END)
                self.listBx2.delete(0, END)
                self.listBx3.delete(0, END)
                self.listBx4.delete(0, END)

                # Updates listboxes
                box1_update()
                box2_update()
                box3_update()
                box4_update()

                # Modifies the listbox text titles with quarter info
                self.classMapKeys
                label1['text'] = self.classMapKeys[self.idx]
                label2['text'] = self.classMapKeys[self.idx + 1]
                label3['text'] = self.classMapKeys[self.idx + 2]
                label4['text'] = self.classMapKeys[self.idx + 3]

        def update_prev(event):
            """
            Function for the "Prev" button
            :param event:
            :return:
            """
            self.idx
            # Checks to see if beginning has been reached
            if (self.idx == 0):
                return
            else:
                # Sets button to green
                buttonNext.config(background="#369148", fg="#e6e6e6")

                if (self.idx - 1 == 0):
                    # Sets button to grey
                    buttonPrev.config(background="#808080", fg="#e6e6e6")

                self.idx -= 1
                # Erases listboxes
                self.listBx1.delete(0, END)
                self.listBx2.delete(0, END)
                self.listBx3.delete(0, END)
                self.listBx4.delete(0, END)

                # Updates listboxes
                box1_update()
                box2_update()
                box3_update()
                box4_update()

                # Modifies the listbox text titles with quarter info
                self.classMapKeys
                label1['text'] = self.classMapKeys[self.idx]
                label2['text'] = self.classMapKeys[self.idx + 1]
                label3['text'] = self.classMapKeys[self.idx + 2]
                label4['text'] = self.classMapKeys[self.idx + 3]

        def backToClassMenu(event):
            """
            Function to go back to the classes menu
            :param event:
            :return:
            """
            roadMapWindow.destroy()

        def getFirstTerm():
            """
            Determines which term to start on when the student has not taken any classes
            :return:
            """
            currentMonth = datetime.now().month
            if (currentMonth > 9):
                term = "Winter"
            elif (6 < currentMonth < 9):
                term = "Fall"
            elif (4 <= currentMonth <= 6):
                term = "Summer"
            else:
                term = "Spring"
            return term

        # Empty list that will store the class keys in same order as dictionary
        self.classMapKeys = []
        termsNormal = ["Fall", "Winter", "Spring", "Summer"]
        classDict = {}

        scm = StudentClassModel.StudentClassModel(self.db)
        recents = scm.find('students_id', self.student_id)
        min_year = datetime.now().year
        check = 1
        # Look through the classes the student has taken and determine which one was the earliest
        for recent in recents:
            class_id = recent[2]
            cm = ClassModel.ClassModel(self.db)
            clas = cm.find_by('id', class_id)
            for c in clas:
                item = str(c[1])
                year = int(item[:4])
                term = int(item[4:])
                if year <= min_year:
                    # Update the term and year
                    curTerm = termsNormal[term - 1]
                    check = 0
                    if term == 1:
                        min_year = year
                    else:
                        min_year = year + 1
        if check:
            # If the student hasn't taken any classes, get the current term
            curTerm = getFirstTerm()

        rm = RequirementModel.RequirementModel(self.db)
        cm = ClassModel.ClassModel(self.db)
        # A variable used to iterate through the termsNormal list
        termTracker = termsNormal.index(curTerm)
        # get the dropdown information
        splitMajor = self.majorChoice.get().split("-")[0]
        find = rm.find_by('type', splitMajor)
        le = len(find)
        accumulatorDict = {}
        for t in range(le // 4):
            term1, term2, term3, term4 = [], [], [], []
            # Don't add "Required" to the summer term
            if termsNormal[termTracker] != "Summer":
                term1.append("Required")
            if termsNormal[(termTracker + 1) % 4] != "Summer":
                term2.append("Required")
            if termsNormal[(termTracker + 2) % 4] != "Summer":
                term3.append("Required")
            if termsNormal[(termTracker + 3) % 4] != "Summer":
                term4.append("Required")

            # Reads through the requirements for term 1
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    # If this is a summer term, break
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s1 = desc['course'].split(" ")
                        course = s1[0]
                        classes = s1[1]
                        if "/" in classes:
                            # Case where there are multiple options e.g: Math 251/261
                            sqlTerm = str(min_year) + "0" + str(termsNormal.index(curTerm) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                # Ensure that the class exists for the given term
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term1.append(theClass)
                                else:
                                    # If the class data is not there, find the most recent occurrence of the class
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term1.append(theClass)
                                    else:
                                        term1.append("- " + desc["description"])

                        else:
                            # If there's just one required class, add it
                            theClass = "- " + desc["course"]
                            term1.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term1.append(desc["description"])

                        elif (desc["course"][1] == "2"):
                            term1.append(desc["description"])
                        elif (desc["course"][1] == "3"):
                            term1.append(desc["description"])

                        priorYear = int(datetime.now().year) - 1
                        # Variable that matches with the term column in the SQL table
                        sqlTerm = str(priorYear) + "0" + str((termsNormal.index(curTerm) % 4) + 1)
                        # Gets every class that has a ">X" in it, where X is 1, 2, or 3
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            # Only add the class if it is offered in the appropriate term
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term1.append(theClass)
                            else:
                                pass
                else:
                    # If there is no course, just add the description of what must be taken
                    # '\n' is appended so that we may determine which term it is in
                    secretKey = desc["description"] + "".join(["\n" for i in range(0, ((4 * t) + termTracker) + 1)])
                    term1.append(secretKey)

            termTracker = (termTracker + 1) % 4

            # Reads through the requirements for term 2
            for desc in json.loads(find[((4 * t) + termTracker)][4]):
                if (((4 * t) + termTracker) % 4 == 3):
                    # If this is a summer term, break
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s2 = desc['course'].split(" ")
                        course = s2[0]
                        classes = s2[1]
                        if "/" in classes:
                            # Case where there are multiple options e.g: Math 251/261
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 1) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                # Ensure that the class exists for the given term
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term2.append(theClass)
                                else:
                                    # If the class data is not there, find the most recent occurrence of the class
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term2.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]

                        else:
                            # If there's just one required class, add it
                            theClass = "- " + desc["course"]
                            term2.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term2.append(desc["description"])

                        elif (desc["course"][1] == "2"):
                            term2.append(desc["description"])
                        elif (desc["course"][1] == "3"):
                            term2.append(desc["description"])

                        priorYear = int(datetime.now().year) - 1
                        # Variable that matches with the term column in the SQL table
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 1) % 4) + 1)
                        # Gets every class that has a ">X" in it, where X is 1, 2, or 3
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            # Only add the class if it is offered in the appropriate term
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term2.append(theClass)
                            else:
                                pass
                else:
                    # If there is no course, just add the description of what must be taken
                    # '\n' is appended so that we may determine which term it is in
                    secretKey = desc["description"] + "".join(["\n" for i in range(0, ((4 * t) + termTracker) + 1)])
                    term2.append(secretKey)

            termTracker = (termTracker + 1) % 4

            # Reads through the requirements for term 3
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    # If this is a summer term, break
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s3 = desc['course'].split(" ")
                        course = s3[0]
                        classes = s3[1]
                        if "/" in classes:
                            # Case where there are multiple options e.g: Math 251/261
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 2) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                # Ensure that the class exists for the given term
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term3.append(theClass)
                                else:
                                    # If the class data is not there, find the most recent occurrence of the class
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term3.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]

                        else:
                            # If there's just one required class, add it
                            theClass = "- " + desc["course"]
                            term3.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term3.append(desc["description"])

                        elif (desc["course"][1] == "2"):
                            term3.append(desc["description"])
                        elif (desc["course"][1] == "3"):
                            term3.append(desc["description"])

                        priorYear = int(datetime.now().year) - 1
                        # Variable that matches with the term column in the SQL table
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 2) % 4) + 1)
                        # Gets every class that has a ">X" in it, where X is 1, 2, or 3
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            # Only add the class if it is offered in the appropriate term
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term3.append(theClass)
                            else:
                                pass
                else:
                    # If there is no course, just add the description of what must be taken
                    # '\n' is appended so that we may determine which term it is in
                    secretKey = desc["description"] + "".join(["\n" for i in range(0, ((4 * t) + termTracker) + 1)])
                    term3.append(secretKey)

            termTracker = (termTracker + 1) % 4

            # Reads through the requirements for term 4
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    # If this is a summer term, break
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s4 = desc['course'].split(" ")
                        course = s4[0]
                        classes = s4[1]
                        if "/" in classes:
                            # Case where there are multiple options e.g: Math 251/261
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 3) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                # Ensure that the class exists for the given term
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term4.append(theClass)
                                else:
                                    # If the class data is not there, find the most recent occurrence of the class
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term4.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]

                        else:
                            # If there's just one required class, add it
                            theClass = "- " + desc["course"]
                            term4.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term4.append(desc["description"])

                        elif (desc["course"][1] == "2"):
                            term4.append(desc["description"])
                        elif (desc["course"][1] == "3"):
                            term4.append(desc["description"])

                        priorYear = int(datetime.now().year) - 1
                        # Variable that matches with the term column in the SQL table
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 3) % 4) + 1)
                        # Gets every class that has a ">X" in it, where X is 1, 2, or 3
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            # Only add the class if it is offered in the appropriate term
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term4.append(theClass)
                            else:
                                pass
                else:
                    # If there is no course, just add the description of what must be taken
                    # '\n' is appended so that we may determine which term it is in
                    secretKey = desc["description"] + "".join(["\n" for i in range(0, ((4 * t) + termTracker) + 1)])
                    term4.append(secretKey)

            termTracker = (termTracker + 1) % 4

            # Update the classDicts with the relevant term data
            classDict.update({termsNormal[termsNormal.index(curTerm) % 4] + " " + str(min_year): term1})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 1) % 4] + " " + str(min_year): term2})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 2) % 4] + " " + str(min_year): term3})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 3) % 4] + " " + str(min_year): term4})
            min_year += 1
        min_year -= le // 4

        classMap = classDict

        """ Below is the widgets relevant to the classRoadmap Window"""
        # Populates a list of keys (in order) from the classMap data
        for i in range(len(classMap)):
            self.classMapKeys.append([key for key in classMap.keys()][i])

        # Creates Window
        roadMapWindow = Frame(self.master, bg=self._darkGrey, height=800, width=800)
        roadMapWindow.place(x=0, y=0)
        # Creates the title you want to have on the window
        roadMapWindow.configure(background="#323232")

        # UO Logo
        logoUO = PhotoImage(file="./img/UOicon.gif")
        labelUO = Label(roadMapWindow, image=logoUO, borderwidth=0)
        labelUO.image = logoUO
        labelUO.place(x=670, y=4)

        # Grey Lines that hide the white lines on the logo
        greyLine = Label(roadMapWindow, text="", background=self._grey)
        greyLine.place(x=0, y=110, height=8, width=800)
        greyLineTop = Label(roadMapWindow, text="", background=self._grey)
        greyLineTop.place(x=0, y=3, height=8, width=800)
        greyLineLeft = Label(roadMapWindow, text="", background=self._grey)
        greyLineLeft.place(x=665, y=0, height=120, width=8)
        greyLineRight = Label(roadMapWindow, text="", background=self._grey)
        greyLineRight.place(x=785, y=0, height=120, width=8)

        # Lower (dark) half of the window
        labelNext = Label(roadMapWindow, text="", background="#282929", fg="#e6e6e6")
        labelNext.place(x=0, y=125, height=475, width=800)

        # Green Stripe
        labelNext = Label(roadMapWindow, text="", background="#369148", fg="#e6e6e6")
        labelNext.place(x=0, y=120, height=5, width=800)

        # RoadMap Text
        roadMapLabel = Label(roadMapWindow, text="ROADMAP", anchor='w')
        roadMapLabel.config(font=("Arial", 44), bg=self._grey, fg=self._yellow)
        roadMapLabel.place(x=40, y=5, height=115, width=600)

        # Initializes listboxes 1
        self.listBx1 = Listbox(roadMapWindow, background="#323232", selectbackground="#369148", fg="#e6e6e6")
        self.listBx1.place(x=60, y=195, height=285, width=155)
        self.listBx1.bind(self._button, selectedClass)

        # Initializes listboxes 2
        self.listBx2 = Listbox(roadMapWindow, background="#323232", selectbackground="#369148", fg="#e6e6e6")
        self.listBx2.place(x=235, y=195, height=285, width=155)
        self.listBx2.bind(self._button, selectedClass)

        # Initializes listboxes 3
        self.listBx3 = Listbox(roadMapWindow, background="#323232", selectbackground="#369148", fg="#e6e6e6")
        self.listBx3.place(x=410, y=195, height=285, width=155)
        self.listBx3.bind(self._button, selectedClass)
        # Initializes listboxes 4
        self.listBx4 = Listbox(roadMapWindow, background="#323232", selectbackground="#369148", fg="#e6e6e6")
        self.listBx4.place(x=585, y=195, height=285, width=155)
        self.listBx4.bind(self._button, selectedClass)

        # Populates all the listboxes
        box1_update()
        box2_update()
        box3_update()
        box4_update()

        # "Next" Button
        labelNext = Label(roadMapWindow, text="NEXT", background="#282929", fg="#e6e6e6")
        labelNext.config(font=("Arial", 12))
        labelNext.place(x=750, y=280, height=20, width=40)

        # "Prev" Button
        labelPrev = Label(roadMapWindow, text="PREV", background="#282929", fg="#e6e6e6")
        labelPrev.config(font=("Arial", 12))
        labelPrev.place(x=10, y=280, height=20, width=40)

        # if the data doesn't have at least 4 quarters of data, grey out "Next" button
        if (len(self.classMapKeys) <= 4):
            buttonNext = Label(roadMapWindow, text=">", background="#808080", fg="#e6e6e6")
            buttonNext.config(font=("Arial Bold", 22))
            buttonNext.place(x=750, y=300, height=40, width=40)
            buttonNext.bind(self._button, update_next)
        else:
            # Set to green if it doesn't
            buttonNext = Label(roadMapWindow, text=">", background="#369148", fg="#e6e6e6")
            buttonNext.config(font=("Arial Bold", 22))
            buttonNext.place(x=750, y=300, height=40, width=40)
            buttonNext.bind(self._button, update_next)

        # If the index is 0, grey out the "Prev" button
        if (self.idx == 0):
            buttonPrev = Label(roadMapWindow, text="<", background="#808080", fg="#e6e6e6")
            buttonPrev.config(font=("Arial Bold", 22))
            buttonPrev.place(x=10, y=300, height=40, width=40)
            buttonPrev.bind(self._button, update_prev)
        else:
            # Set to green if it doesn't
            buttonPrev = Label(roadMapWindow, text="<", background="#369148", fg="#e6e6e6")
            buttonPrev.config(font=("Arial Bold", 22))
            buttonPrev.place(x=10, y=300, height=40, width=40)
            buttonPrev.bind(self._button, update_prev)

        # Title the titles for each listbox 1
        label1 = Label(roadMapWindow, text=self.classMapKeys[self.idx], background="#282929", fg="#e6e6e6")
        label1.config(font=("Arial Bold", 16))
        label1.place(x=60, y=160, height=30, width=155)

        # Optional text to be implemented for listbox 1
        label1a = Label(roadMapWindow, text="", background="#282929", fg="Green")
        label1a.config(font=("Helvetica", 16))
        label1a.place(x=60, y=480, height=30, width=155)

        # Title the titles for each listbox 2
        label2 = Label(roadMapWindow, text=self.classMapKeys[self.idx + 1], background="#282929", fg="#e6e6e6")
        label2.config(font=("Arial Bold", 16))
        label2.place(x=235, y=160, height=30, width=155)

        # Optional text to be implemented for listbox 1
        label2a = Label(roadMapWindow, text="", background="#282929", fg="#e6e6e6")
        label2a.config(font=("Helvetica", 16))
        label2a.place(x=235, y=480, height=30, width=155)

        # Title for each listbox 3
        label3 = Label(roadMapWindow, text=self.classMapKeys[self.idx + 2], background="#282929", fg="#e6e6e6")
        label3.config(font=("Arial Bold", 16))
        label3.place(x=410, y=160, height=30, width=155)

        # Optional text to be implemented for listbox 1
        label3a = Label(roadMapWindow, text="", background="#282929", fg="white")
        label3a.config(font=("Helvetica", 16))
        label3a.place(x=410, y=480, height=30, width=155)

        # Title the titles for each listbox 4
        label4 = Label(roadMapWindow, text=self.classMapKeys[self.idx + 3], background="#282929", fg="#e6e6e6")
        label4.place(x=585, y=160, height=30, width=155)
        label4.config(font=("Arial Bold", 16))

        # Optional text to be implemented for listbox 1
        label4a = Label(roadMapWindow, text="", background="#282929", fg="#e6e6e6")
        label4a.config(font=("Helvetica", 16))
        label4a.place(x=585, y=480, height=30, width=155)

        # Classes "Button"
        backToClassesButton = Label(roadMapWindow, text="CLASSES", background="#ffcc00", fg="#282929")
        backToClassesButton.config(font=("Arial", 22))
        backToClassesButton.place(x=330, y=510, height=40, width=140)
        backToClassesButton.bind(self._button, backToClassMenu)

    def subjectClick(self, event):
        """
        Updates the OfferedCourses list to match the selected subject
        :param event:
        :return:
        """
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            value = w.get(index)
            self.currentSubject = value
            self.updateList()

    def updateList(self):
        """
        This function updates the OfferedCourses list
        :return:
        """
        self.offeredCourses.delete(0, END)
        year = str(self.strObj1.get())
        term = str(self.strObj2.get())
        # Determine the year and term of the classes to be added
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
        cm = ClassModel.ClassModel(self.db)
        # Finds all the classes for the selected subject, given the year and term
        items = cm.find_by_term(self.currentSubject, ye, t)
        if self.currentSubject is not None:
            if len(items) > 0:
                for key, value in enumerate(items):
                    insertLine = self._compose([value])
                    self.offeredCourses.insert(key, "(" + term + " " + year + ") " + insertLine)
            else:
                # If there are no classes for the given term/year
                self.offeredCourses.insert(END, "None found for " + self.currentSubject + " " + term + " " + year)
        else:
            # The base case, when no subject has been selected
            self.offeredCourses.insert(END, "Please select a subject (on the left)")
            self.offeredCourses.insert(END, "and a term (below)")

    def courseClick(self, event):
        """
        When a course in OfferedCourses is selected
        :param event:
        :return:
        """
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            cc = w.get(index)
            if not self._contain(cc,
                                 self.takenClasses) and cc != self._offeredCoursesDefault and "None" not in cc and "subject" not in cc and "term" not in cc:
                # If it is not already in the takenClasses list
                half = cc.split(")")[0].replace("(", "")
                currentCourse = cc.split(")")[1:][0][1:]
                # locate class record
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1], half.split(" ")[0], half.split(" ")[1])
                class_id = clas[0][0]

                # associate the item - add it to the StudentClass table
                scm = StudentClassModel.StudentClassModel(self.db)
                scm.associate(self.student_id, class_id)

                # insert item into the takenClasses list
                self.takenClasses.insert(END,
                                         "(" + half.split(" ")[0] + " " + half.split(" ")[1] + ") " + currentCourse)

    def removeClass(self, event):
        """
        When a class in TakenClasses is selected
        :param event:
        :return:
        """
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            cc = w.get(index)
            half = cc.split(")")[0].replace("(", "")
            currentCourse = cc.split(")")[1:][0][1:]
            # Ask for confirmation before deleting the class
            MsgBox = tk.messagebox.askquestion('Delete Confirmation',
                                               'Are you sure you would like to delete this class',
                                               icon='warning')
            if MsgBox == 'yes':
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1], half.split(" ")[0], half.split(" ")[1])
                class_id = clas[0][0]

                scm = StudentClassModel.StudentClassModel(self.db)
                # Removes the class from the StudentClass tabel
                scm.disassociate(self.student_id, class_id)
                # Removes the class from the takenClasses listbox
                self.takenClasses.delete(index)

    def _decompose(self, str):
        """
        Acquires relevant course information from string which can then be processed by the database
        :param str:
        :return:
        """
        split = str.split(" ")
        subject = split[0]
        code = split[1]
        course = " ".join(str.split(" ")[2:]).replace("[", "").replace("]", "")[2:]

        return subject, code, course

    def _compose(self, value):
        """
        Puts a class in the appropriate format
        :param value:
        :return:
        """
        v = value[0]
        return v[3] + " " + v[4] + " - [" + v[2] + "]"

    def _contain(self, item, box):
        """
        Determines if a class is in a given listbox
        :param item:
        :param box:
        :return:
        """
        return item in box.get(0, "end")
