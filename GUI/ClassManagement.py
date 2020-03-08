import tkinter as tk
import json
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import Notebook, Entry
from GUI.ClassInfo import *
from datetime import date, datetime
import StudentModel
import StudentClassModel
import ClassModel
import RequirementModel


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
        self._buttonWidth = 150
        self._buttonText = ("Arial Bold", 16)
        self._offeredCoursesDefault = "Please select a subject to display courses."

        self.studentName = studentName
        self.master = master
        self.window = Frame(master, bg=self._darkGrey, height=800, width=800)
        self.window.place(x=0, y=125)

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
        self.courseSubjects = Listbox(self.window, selectmode="browse", bg=self._yellow, fg=self._darkGrey,
                                      selectbackground=self._green, width=6, font=subfont)
        self.courseSubjects.place(x=22, y=80, height=295, width=100)
        self.courseSubjects.bind(self._button, self.subjectClick)

        cm = ClassModel.ClassModel(self.db)
        subject = cm.distinct('subject')
        for k, v in enumerate(subject):
            self.courseSubjects.insert(k, v[0])

        # "Student" Label
        studentName = "Student: " + studentName
        student = Label(self.window, text=studentName, anchor='w')
        student.place(x=22, y=10, height=40, width=500)
        student.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

        # # Student Name Label (Updates)
        # labl = Label(self.window, text=studentName, anchor='w')
        # labl.place(x=120, y=15, height=30, width=200)
        # labl.config(font=("Arial", 20), bg=self._darkGrey, fg=self._yellow)

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

        # add in previously taken classes
        scm = StudentClassModel.StudentClassModel(self.db)
        prev = scm.find('students_id', self.student_id)
        for i in prev:
            class_id = i[2]

            cm = ClassModel.ClassModel(self.db)
            clas = cm.find_by('id', class_id)
            year = str(clas[0][1])[:4]
            term = str(clas[0][1])[4:]

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
        goHome.bind("<Button-1>", self.goHomeClick)
        goHome.place(x=468, y=305, height=self._buttonHeight, width=self._buttonWidth)

        # Button Roadmap
        roadmap = Label(self.window, text='Class Roadmap')
        roadmap.config(font=self._buttonText, bg=self._green, fg=self._darkGrey)
        roadmap.bind("<Button-1>", self.classRoadmap)
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

    def year_dropdown(self, *args):
        self.updateList()

    def quarter_dropdown(self, *args):
        self.updateList()

    def goHomeClick(self, event):
        # mainMenu(self.master)
        self.window.destroy()
        self.windowTop.destroy()

    def classRoadmap(self, event):
        self.idx = 0

        def box1_update():
            # Updates listbox 1 with class data given the key
            self.listBx1
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx]]))):
                self.listBx1.insert(0, classMap[self.classMapKeys[self.idx]][i])

        def box2_update():
            # Updates listbox 2 with class data given the key
            self.listBx2
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 1]]))):
                self.listBx2.insert(0, classMap[self.classMapKeys[self.idx + 1]][i])

        def box3_update():
            # Updates listbox 3 with class data given the key
            self.listBx3
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 2]]))):
                self.listBx3.insert(0, classMap[self.classMapKeys[self.idx + 2]][i])
                # self.listBx3.itemconfig(0, {'bg': 'red'})

        def box4_update():
            # Updates listbox 4 with class data given the key
            self.listBx4
            #if len(classMap[self.classMapKeys[self.idx + 3]]):
            for i in reversed(range(len(classMap[self.classMapKeys[self.idx + 3]]))):
                self.listBx4.insert(0, classMap[self.classMapKeys[self.idx + 3]][i])

        def selectedClass(event):
            w = event.widget
            if not w.curselection() == ():
                index = int(w.curselection()[0])
                selectedCourse = w.get(index).split(" ")
                if "-" in selectedCourse:
                    del selectedCourse[0]
                cm = ClassModel.ClassModel(self.db)
                try:
                    idx = cm.predict_future_class_id(selectedCourse[0], selectedCourse[1])
                    classInfo(self.master, self.db, selectedCourse, idx[0][1])
                except IndexError:
                    pass

        def update_next(event):
            # Function for the "Next" button
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
            # Function for the "Prev" button
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
            # Function to go back to the classes menu
            roadMapWindow.destroy()

        def getFirstTerm():
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
        for recent in recents:
            class_id = recent[2]
            cm = ClassModel.ClassModel(self.db)
            clas = cm.find_by('id', class_id)
            for c in clas:
                item = str(c[1])
                year = int(item[:4])
                term = int(item[4:])
                if year <= min_year:
                    curTerm = termsNormal[term - 1]
                    check = 0
                    if term == 1:
                        min_year = year
                    else:
                        min_year = year + 1
        if check:
            curTerm = getFirstTerm()

        rm = RequirementModel.RequirementModel(self.db)
        cm = ClassModel.ClassModel(self.db)
        termTracker = termsNormal.index(curTerm)
        find = rm.find_by('type', 'BS')
        le = len(find)
        accumulatorDict = {}
        for t in range(le // 4):
            term1, term2, term3, term4 = [], [], [], []
            if termsNormal[termTracker] != "Summer":
                term1.append("Required")
            if termsNormal[(termTracker + 1) % 4] != "Summer":
                term2.append("Required")
            if termsNormal[(termTracker + 2) % 4] != "Summer":
                term3.append("Required")
            if termsNormal[(termTracker + 3) % 4] != "Summer":
                term4.append("Required")  

            # spring
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s1 = desc['course'].split(" ")
                        course = s1[0]
                        classes = s1[1]
                        if "/" in classes:
                            sqlTerm = str(min_year) + "0" + str(termsNormal.index(curTerm) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term1.append(theClass)
                                else:
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss                                
                                        term1.append(theClass)
                                    else:
                                        term1.append("- " + desc["description"])
                                
                        else:
                            theClass = "- " + desc["course"]
                            term1.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term1.append("Arts & Letters")
                        
                        elif (desc["course"][1] == "2"):
                            term1.append("Social Sciences")
                        elif (desc["course"][1] == "3"):
                            term1.append("Science")
                        
                        priorYear = int(datetime.now().year) - 1
                        sqlTerm = str(priorYear) + "0" + str((termsNormal.index(curTerm) % 4) + 1)
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term1.append(theClass)
                            else:
                                pass
                else:
                    term1.append(desc["description"])
            termTracker = (termTracker + 1) % 4

            # summer
            for desc in json.loads(find[((4 * t) + termTracker)][4]):
                if (((4 * t) + termTracker) % 4 == 3):
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s2 = desc['course'].split(" ")
                        course = s2[0]
                        classes = s2[1]
                        if "/" in classes:
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 1) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term2.append(theClass)
                                else:
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term2.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]
                                
                        else:
                            theClass = "- " + desc["course"]
                            term2.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term2.append("Arts & Letters")
                        
                        elif (desc["course"][1] == "2"):
                            term2.append("Social Sciences")
                        elif (desc["course"][1] == "3"):
                            term2.append("Science")
                        
                        priorYear = int(datetime.now().year) - 1
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 1) % 4) + 1)
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term2.append(theClass)
                            else:
                                pass
                else:
                    term2.append(desc["description"])
            termTracker = (termTracker + 1) % 4

            # fall
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    break
                if desc['course'] != "":
                    if desc['course'][0] != ">":
                        s3 = desc['course'].split(" ")
                        course = s3[0]
                        classes = s3[1]
                        if "/" in classes:
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 2) % 4)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term3.append(theClass)
                                else:
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term3.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]
                        
                        else:
                            theClass = "- " + desc["course"]
                            term3.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term3.append("Arts & Letters")
                        
                        elif (desc["course"][1] == "2"):
                            term3.append("Social Sciences")
                        elif (desc["course"][1] == "3"):
                            term3.append("Science")
                        
                        priorYear = int(datetime.now().year) - 1
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 2) %4) + 1)
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term3.append(theClass)
                            else:
                                pass
                else:
                    term3.append(desc["description"])
            termTracker = (termTracker + 1) % 4

            #winter
            for desc in json.loads(find[(4 * t) + termTracker][4]):
                if ((4 * t) + termTracker) % 4 == 3:
                    break
                if desc['course'] != "":    
                    if desc['course'][0] != ">":
                        s4 = desc['course'].split(" ")
                        course = s4[0]
                        classes = s4[1]
                        if "/" in classes:
                            # query for course + each class in classes split
                            sqlTerm = str(min_year) + "0" + str((termsNormal.index(curTerm) + 3) % 4)
                            #print(sqlTerm)
                            classes_split = classes.split("/")
                            for clss in classes_split:
                                offeredClass = cm.find_class_id(course, clss, sqlTerm)
                                if len(offeredClass):
                                    theClass = "- " + course + " " + clss
                                    term4.append(theClass)
                                else:
                                    offeredClass = cm.predict_future_class_id(course, clss)
                                    if len(offeredClass):
                                        theClass = "- " + course + " " + clss
                                        term4.append(theClass)
                                    else:
                                        theClass = "- " + desc["description"]
                                    
                        else:
                            theClass = "- " + desc["course"]
                            term4.append(theClass)
                    else:
                        # query classes for with >
                        if (desc["course"][1] == "1"):
                            term4.append("Arts & Letters")
                        
                        elif (desc["course"][1] == "2"):
                            term4.append("Social Sciences")
                        elif (desc["course"][1] == "3"):
                            term4.append("Science")
                        
                        priorYear = int(datetime.now().year) - 1
                        sqlTerm = str(priorYear) + "0" + str(((termsNormal.index(curTerm) + 3) %4) + 1)
                        carrotClasses = cm.crt_class_search(desc["course"][1], priorYear)
                        for carrot in carrotClasses:
                            if int(sqlTerm) in carrot:
                                theClass = "- " + str(carrot[0]) + " " + str(carrot[2])
                                term4.append(theClass)
                            else:
                                pass
                else:
                    term4.append(desc["description"])

            termTracker = (termTracker + 1) % 4
            classDict.update({termsNormal[termsNormal.index(curTerm) % 4] + " " + str(min_year): term1})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 1) % 4] + " " + str(min_year): term2})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 2) % 4] + " " + str(min_year): term3})
            classDict.update({termsNormal[(termsNormal.index(curTerm) + 3) % 4] + " " + str(min_year): term4})
            min_year += 1
        min_year -= le // 4

        classMap = classDict

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
            buttonNext.bind("<Button-1>", update_next)
        else:
            # Set to green if it doesn't
            buttonNext = Label(roadMapWindow, text=">", background="#369148", fg="#e6e6e6")
            buttonNext.config(font=("Arial Bold", 22))
            buttonNext.place(x=750, y=300, height=40, width=40)
            buttonNext.bind("<Button-1>", update_next)

        # If the index is 0, grey out the "Prev" button
        if (self.idx == 0):
            buttonPrev = Label(roadMapWindow, text="<", background="#808080", fg="#e6e6e6")
            buttonPrev.config(font=("Arial Bold", 22))
            buttonPrev.place(x=10, y=300, height=40, width=40)
            buttonPrev.bind("<Button-1>", update_prev)
        else:
            # Set to green if it doesn't
            buttonPrev = Label(roadMapWindow, text="<", background="#369148", fg="#e6e6e6")
            buttonPrev.config(font=("Arial Bold", 22))
            buttonPrev.place(x=10, y=300, height=40, width=40)
            buttonPrev.bind("<Button-1>", update_prev)

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
        backToClassesButton.bind("<Button-1>", backToClassMenu)

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
        items = cm.find_by_term(self.currentSubject, ye, t)
        if self.currentSubject is not None:
            if len(items) > 0:
                for key, value in enumerate(items):
                    insertLine = self._compose([value])
                    self.offeredCourses.insert(key, "(" + term + " " + year + ") " + insertLine)
            else:
                self.offeredCourses.insert(END, "None found for " + self.currentSubject + " " + term + " " + year)
        else:
            self.offeredCourses.insert(END, "Please select a subject (on the left)")
            self.offeredCourses.insert(END, "and a term (below)")

    def courseClick(self, event):
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            cc = w.get(index)
            if not self._contain(cc, self.takenClasses) and cc != self._offeredCoursesDefault:
                half = cc.split(")")[0].replace("(", "")
                currentCourse = cc.split(")")[1:][0][1:]
                # locate class record
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1], half.split(" ")[0], half.split(" ")[1])
                class_id = clas[0][0]

                # associate the item
                scm = StudentClassModel.StudentClassModel(self.db)
                scm.associate(self.student_id, class_id)

                # insert item into the list
                self.takenClasses.insert(END,
                                         "(" + half.split(" ")[0] + " " + half.split(" ")[1] + ") " + currentCourse)

    def removeClass(self, event):
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            cc = w.get(index)
            half = cc.split(")")[0].replace("(", "")
            currentCourse = cc.split(")")[1:][0][1:]
            MsgBox = tk.messagebox.askquestion('Delete Confirmation',
                                               'Are you sure you would like to delete this class',
                                               icon='warning')
            if MsgBox == 'yes':
                cm = ClassModel.ClassModel(self.db)
                clas = cm.find_course(self._decompose(currentCourse)[2], self._decompose(currentCourse)[0],
                                      self._decompose(currentCourse)[1], half.split(" ")[0], half.split(" ")[1])
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
