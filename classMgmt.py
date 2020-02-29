import tkinter as tk
from tkinter import *
from tkinter import font
from jsonPythonParser import * 


class classMgmt(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.geometry("800x450")
        self.title = "RegTools"
        subfont= font.Font(family="Helvetica", size=26)
        courseFont = font.Font(family = "Helvetica", size = 16)
        self.courseSubjects = Listbox(master, selectmode="browse", bg="red", width = 6, height = 11, borderwidth=2, font = subfont)
        self.courseSubjects.insert(0, "CIS")
        self.courseSubjects.insert(1, "MATH")
        self.courseSubjects.insert(2, "ENG")
        self.courseSubjects.bind("<Double-Button-1>", self.subjectClick)
        self.offeredCourses = Listbox(master, selectmode = "browse", bg = "red", width = 35, height = 17, borderwidth = 2, font = courseFont)
        self.offeredCourses.bind("<Double-Button-1>", self.courseClick)
        self.courseBio = Listbox(master, selectmode = "browse", bg = "red", width = 40, height = 20, borderwidth = 2)
        self.courseBio.pack(side = "right", fill = NONE, expand = FALSE, padx = 10, pady = 10)
        self.courseSubjects.pack(side = "left", fill = NONE, expand = FALSE, padx = 10, pady = 10)
        self.offeredCourses.pack(side = "left", fill = NONE, expand = FALSE, padx = 15, pady = 10)

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
        for i in range(len(courseData)):
            self.courseBio.insert(i, courseData[i])

def main():
    root = tk.Tk()
    myGUI = classMgmt(root)
    root.mainloop()

main()
