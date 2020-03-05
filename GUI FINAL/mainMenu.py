from tkinter import *
from tkinter import messagebox
from ClassMgmt import *
from AddStudent import *
import csv
import os
import sys


class mainMenu(tk.Tk):
    def __init__(self, master):
        self._lightGrey = "#b8b8b8"
        self._backgroundColor = "#323232"
        self._darkGrey = "#282929"
        self._green = "#369148"
        self._yellow = "#ffcc00"
        self._button = "<Button-1>"

        self.master = master
        master.geometry("800x600+120+120")
        master.title("RegTools")
        master.configure(background=self._backgroundColor)
        self.nameList = []
        self.numberOfNames = 0

        # Dark grey background box 
        grayBoxFrame = Frame(master, width = 800, height = 390, bg=self._darkGrey)
        grayBoxFrame.place(x = 0, y = 150)
        fr = Frame(master, width=200, height=200, bg=self._green)
        fr.place(x=300,y=252)

        # Creates Menu Bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # Add Student label
        studentBtn = Label(master, text='Add Student')
        studentBtn.config(font=("Arial Bold", 13), bg=self._green, fg=self._yellow)
        studentBtn.place(x=348,y=465, height=27, width=106)
        studentBtn.bind(self._button, self.addStudentButtonClick)

        logo = PhotoImage(file="RegToolsLogo.gif")
        label = Label(image = logo, borderwidth = 0)
        label.image = logo
        label.place(x=100,y=40)

        # Makes RegTool title
        logoPad = Label(root, text='')
        logoPad.place(x=95,y=40, height=5, width=620)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(root, text='')
        logoPad.place(x=98,y=40, height=90, width=5)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(root, text='')
        logoPad.place(x=701,y=40, height=90, width=5)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(root, text='')
        logoPad.place(x=95,y=121, height=5, width=620)
        logoPad.config(bg=self._backgroundColor)


        # Name listbox properties
        self.lb = Listbox(fr,selectmode="browse",bg=self._backgroundColor, selectbackground=self._green)
        self.lb.config(font=("Mincho Bold", 16),fg="#e6e6e6")
        self.lb.place(x = 5, y = 5, height = 190, width = 190)
        self.lb.bind('<Double-Button-1>', self.onClick)
        self.lb.bind("d", self.deleteName)
        self.loadLB()

        # "Search" Label
        searchLabel = Label(master, text='Search:')
        searchLabel.place(x=290,y=205, height=40, width=80)
        searchLabel.config(font=("Arial Bold", 16), bg=self._darkGrey, fg=self._yellow)


        self.nameVar = StringVar()
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)

        # Creates the search textbox/entrybox
        searchbox = Entry(master, textvariable=self.search_var, bg=self._lightGrey)
        searchbox.place(x=360,y=215, height=20, width=141)
        searchbox.config(highlightthickness=0)
        
        # 'D' Key label
        dKeyLabel = Label(master, text='= Deletes Name')
        dKeyLabel.place(x=547,y=550, height=30, width=200)
        dKeyLabel.config(font=("Arial Bold", 18))
        dKeyLabel.config(bg=self._backgroundColor, fg="Grey")

        # Key label
        dKey = Label(master, text="'D'")
        dKey.place(x=543,y=550, height=30, width=30)
        dKey.config(font=("Arial Bold", 20))
        dKey.config(bg="Grey", fg=self._backgroundColor)


    def loadLB(self):
        # Number of names to be loaded
        self.numberOfNames = 4

        # Inserts names into listbox
        for i in range(0, self.numberOfNames):
            self.lb.insert(i, "Load Name")

    def update_listbox(self, *args):
        self.loadLB()
        search_term = self.search_var.get()
        self.lb.delete(0, END)
        for item in self.nameList:
            if search_term.lower() in item.lower():
                self.lb.insert(END, item)

    def onClick(self, event):
        w=event.widget
        index = int(w.curselection()[0])
        selectedStudent = w.get(index)

        # Calls classMgmt class and opens classMgmt class window
        ClassMgmt(self.master, selectedStudent)

    def deleteName(self, event):
        w=event.widget
        index = int(w.curselection()[0])
        selectedStudent = w.get(index)
        MsgBox = tk.messagebox.askquestion ('Delete Confirmation','Are you sure you would like to delete %s, deleting all of their saved data?' % selectedStudent, icon = 'warning')
        if MsgBox == 'yes':
            print("Will have to delete student from sql database")
            self.lb.delete(index)
        else:
            print("Student was not deleted.")

    def addStudentButtonClick(self, event):
        AddStudent(self.master)

root = tk.Tk()
root.resizable(False, False)
myGUI = mainMenu(root)
root.mainloop()
