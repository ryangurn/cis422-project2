from tkinter import *
from tkinter import messagebox
from GUI.ClassManagement import *
from GUI.AddStudent import *
import csv
import os
import sys
import StudentModel
import sqlite3


class MainMenu(tk.Tk):
    def __init__(self, master, db_file):
        self.db = db_file
        self.master = master
        master.geometry("810x600")
        master.title("RegTools")
        master.configure(background="#323232")
        self.nameList = []
        self.numberOfNames = 0
        grayBoxFrame = Frame(master, width=810, height=390, bg="#262929")
        grayBoxFrame.place(x=0, y=150)
        fr = Frame(master, width=200, height=200, bg="#369148")
        fr.place(x=310, y=280)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        addStudentButton = Label(master, text='Add Student')
        addStudentButton.config(font=("Arial Bold", 13), bg="#369148", fg="#ffcc00")
        addStudentButton.place(x=358, y=495, height=27, width=106)

        # button1.bind()
        addStudentButton.bind("<Double-Button-1>", self.addStudentButtonClick)

        logo = PhotoImage(file="./img/RegToolsLogo.gif")
        label = Label(image=logo, borderwidth=0)
        label.image = logo
        label.place(x=100, y=40)

        # Makes the really cool RegTool title
        oolsLabel = Label(master, text='')
        oolsLabel.place(x=95, y=40, height=5, width=620)
        oolsLabel.config(font=("Mincho Bold", 60))
        oolsLabel.config(bg="#323232", fg="#323232")

        oolsLabel = Label(master, text='')
        oolsLabel.place(x=98, y=40, height=90, width=5)
        oolsLabel.config(font=("Mincho Bold", 60))
        oolsLabel.config(bg="#323232", fg="#323232")

        oolsLabel = Label(master, text='')
        oolsLabel.place(x=701, y=40, height=90, width=5)
        oolsLabel.config(font=("Mincho Bold", 60))
        oolsLabel.config(bg="#323232", fg="#323232")

        oolsLabel = Label(master, text='')
        oolsLabel.place(x=95, y=121, height=5, width=620)
        oolsLabel.config(font=("Mincho Bold", 60))
        oolsLabel.config(bg="#323232", fg="#323232")

        # "Search" Label
        self.lb = Listbox(fr, selectmode="browse", bg="#323232", selectbackground="#05761B")
        self.loadLB()
        self.lb.config(font=("Mincho Bold", 16), fg="#e6e6e6")
        self.lb.place(x=5, y=5, height=190, width=190)
        self.lb.bind("<Double-Button-1>", self.onClick)
        self.lb.bind("d", self.deleteName)

        searchLabel = Label(master, text='Search:')
        searchLabel.place(x=290, y=205, height=40, width=80)
        searchLabel.config(font=("Arial Bold", 16))
        searchLabel.config(bg="#262929", fg="#ffcc00")

        # Creates the search textbox/entrybox
        self.nameVar = StringVar()
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)
        searchbox = Entry(master, textvariable=self.search_var, bg="#b8b8b8")
        searchbox.config(highlightthickness=0)
        searchbox.place(x=360, y=215, height=20, width=145)

        dKeyLabel = Label(master, text='= Deletes Name')
        dKeyLabel.place(x=547, y=550, height=30, width=200)
        dKeyLabel.config(font=("Arial Bold", 18))
        dKeyLabel.config(bg="#323232", fg="Grey")

        dKey = Label(master, text="'D'")
        dKey.place(x=543, y=550, height=30, width=30)
        dKey.config(font=("Arial Bold", 20))
        dKey.config(bg="Grey", fg="#323232")

    def loadLB(self):
        self.numberOfNames = 0
        self.nameList = []

        sm = StudentModel.StudentModel(self.db)
        for item in sm.all():
            self.lb.insert(END, item[1])
            self.nameList.append(item[1])
            self.numberOfNames += 1

    def update_listbox(self, *args):
        self.loadLB()
        search_term = self.search_var.get()
        self.lb.delete(0, END)
        for item in self.nameList:
            if search_term.lower() in item.lower():
                self.lb.insert(END, item)

    def onClick(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        selectedStudent = w.get(index)
        ClassManagement(self.master, selectedStudent, self.db)

    def deleteName(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        selectedStudent = w.get(index)
        MsgBox = tk.messagebox.askquestion('Delete Confirmation',
                                           'Are you sure you would like to delete this student %s, deleting all of '
                                           'their saved data?' % selectedStudent,
                                           icon='warning')
        sm = StudentModel.StudentModel(self.db)
        stu = sm.find(selectedStudent)
        stu_id = stu[0][0]

        if MsgBox == 'yes':
            self.lb.delete(index)
            sm = StudentModel.StudentModel(self.db)
            sm.delete(stu_id)

    def addStudentButtonClick(self, event):
        AddStudent(self.master, self.db, self.lb)
