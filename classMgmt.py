import tkinter as tk
from tkinter import *
from tkinter import font
from jsonPythonParser import * 

class classMgmt(tk.Tk):
    def __init__(self, master):
        self.newWindow = Frame(master, bg = "#003011", height = 400, width = 810)
        self.newWindow.place(x = 0, y = 200)
        subfont= font.Font(family="Helvetica", size=26)
        courseFont = font.Font(family = "Helvetica", size = 16)
        self.courseSubjects = Listbox(self.newWindow, selectmode="browse", bg="#ffcc00", width = 6, borderwidth=2, font = subfont)
        self.courseSubjects.insert(0, "CIS")
        self.courseSubjects.insert(1, "MATH")
        self.courseSubjects.insert(2, "ENG")
        self.courseSubjects.bind("<Double-Button-1>", self.subjectClick)
        self.offeredCourses = Listbox(self.newWindow, selectmode = "browse", bg = "#ffcc00", width = 35, borderwidth = 2, font = courseFont)
        self.offeredCourses.bind("<Double-Button-1>", self.courseClick)
        self.courseBio = Listbox(self.newWindow, selectmode = "browse", bg = "#ffcc00", width = 40, borderwidth = 2)
        #self.courseSubjects.pack(side = "left", fill = NONE, expand = FALSE, padx = 10, pady = 10)
        self.courseSubjects.place(x = 10, y = 0, height = 325)
        #self.offeredCourses.pack(side = "left", fill = NONE, expand = FALSE, padx = 15, pady = 10)
        self.offeredCourses.place(x = 100, y = 0, height = 325)
        #self.courseBio.pack(side = "left", fill = NONE, expand = FALSE, padx = 10, pady = 10)
        self.courseBio.place(x = 390, y = 0, height = 325)
        self.goHome = Button(self.newWindow, text='Go Home', command=self.goHomeClick)
        self.goHome.place(x = 475, y = 330, height = 15)
        #self.goHome.pack(side = "top")

    def goHomeClick(self):
        #mainMenu(self.master)
        self.newWindow.destroy()

    def subjectClick(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        currentSubject = value
        keys = get_keys()
        self.offeredCourses.delete(0, END)
        i = 0
        for key in keys:
            if currentSubject == get_subject(key):
                self.offeredCourses.insert(i, key)
                i += 1
            else:
                continue

    def courseClick(self, event):
        courseData = []
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        currentCourse = value
        self.courseBio.delete(0, END)
        courseData.append("Instructor: " + get_sec_instructor(currentCourse, 0))
        courseData.append("Room: " + get_sec_location(currentCourse, 0))
        courseData.append("Schedule: " + get_sec_days(currentCourse, 0) + " - " + get_sec_times(currentCourse, 0))
        courseData.append("Credits: " + get_credits(currentCourse))
        courseData.append("Grading: " + get_grading(currentCourse))
        courseData.append("Notes: " + get_sec_notes(currentCourse, 0))
        for i in range(len(courseData)):
            self.courseBio.insert(i, courseData[i])