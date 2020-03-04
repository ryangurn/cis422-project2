from tkinter import *
from tkinter import messagebox
from classMgmt import *
from addStudent import *
import csv
import os
import sys


class mainMenu(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.geometry("810x600")
        master.title("List Box Test")
        master.configure(background="#323232")
        self.nameList = []
        self.numberOfNames = 0
        grayBoxFrame = Frame(master, width = 810, height = 400, bg="#262929")
        grayBoxFrame.place(x = 0, y = 150)
        fr = Frame(master, width=200, height=200, bg="#369148")
        fr.place(x=310,y=280)

        addStudentButton = Label(master, text='Add Student')
        addStudentButton.config(font=("Arial Bold", 13), bg="#369148", fg="#ffcc00")
        addStudentButton.place(x=358,y=500, height=27, width=106)

        #button1.bind()
        addStudentButton.bind("<Double-Button-1>", self.addStudentButtonClick)

        logo = PhotoImage(file="RegToolsLogo.gif")
        label = Label(image = logo, borderwidth = 0)
        label.image = logo
        label.place(x=100,y=40)
        # "Search" Label

        self.lb = Listbox(fr,selectmode="browse",bg="#323232", selectbackground="#05761B")
        self.lb.config(font=("Mincho Bold", 16),fg="#e6e6e6")
        self.lb.place(x = 5, y = 5, height = 190, width = 190)
        self.lb.bind("<Double-Button-1>", self.onClick)
        self.lb.bind("d", self.deleteName)
        self.loadLB()

        searchLabel = Label(master, text='Search:')
        searchLabel.place(x=290,y=205, height=40, width=80)
        searchLabel.config(font=("Arial Bold", 16))
        searchLabel.config(bg="#262929", fg="#ffcc00")


        # Creates the search textbox/entrybox
        self.nameVar = StringVar()
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)
        searchbox = Entry(master, textvariable=self.search_var, bg="#b8b8b8")
        searchbox.config(highlightthickness=0)
        searchbox.place(x=360,y=215, height=20, width=145)

        # List box geometry
       # self.lb.grid(row=1, rowspan=10, column=0,columnspan=5, sticky='W', padx=5, pady=5,ipadx=5, ipady=5)
        

        # All items in the listbox get stored in "all_items"

    def loadLB(self):
        self.numberOfNames = 0
        self.nameList = []
        with open('names.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                # Adds each name to list
                self.nameList.append(line[0])
                # Updates the number of students in list
                self.numberOfNames += 1
        for i in range(0, self.numberOfNames):
		    # Inserts name data into listbox
            self.lb.insert(i, self.nameList[i])

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
        classMgmt(self.master, selectedStudent)

    def deleteName(self, event):
        w=event.widget
        index = int(w.curselection()[0])
        selectedStudent = w.get(index)
        MsgBox = tk.messagebox.askquestion ('Delete Conifrmation','Are you sure you would like to delete this student %s' % selectedStudent, icon = 'warning')
        if MsgBox == 'yes':
            print("Will have to delete student from sql database")
            self.lb.delete(index)
        else:
            print("student was not deleted")

    def addStudentButtonClick(self, event):
        addStudent(self.master)


root = tk.Tk()
myGUI = mainMenu(root)
root.mainloop()