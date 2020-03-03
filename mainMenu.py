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
        master.configure(background="#003011")
        self.nameList = []
        self.numberOfNames = 0
        self.fr = Frame(master, width=200, height=200,bg="#ffcc00")
        self.fr.place(x=300,y=300)
        # Creates listbox
        self.lb=Listbox(self.fr, selectmode="browse",bg="white", selectbackground="Yellow")

        # Calls function that populates listbox
        # Opens name addition menu
        addStudentButton = Button(master, text='Add Student', width=25, command=self.addStuentButtonClick)
        addStudentButton.place(x=350,y=500, height=20, width=100)

        # Makes the really cool RegTool title
        rLabel = Label(master, text='R', name = "rLabel")
        rLabel.place(x=190,y=15, height=100, width=100)
        rLabel.config(font=("Mincho Bold", 90), bg = "white", fg = "#003011")
        egLabel = Label(master, text='EG', name = "egLabel")
        egLabel.place(x=270,y=28, height=100, width=80)
        egLabel.config(font=("Mincho Bold", 60), bg="#ffcc00", fg="#003011")
        tLabel = Label(master, text='T', name = "tLabel")
        tLabel.place(x=370,y=15, height=100, width=100)
        tLabel.config(font=("Mincho Bold", 90), bg="White", fg="#003011")
        oolsLabel = Label(master, text='OOLS', name = "oolsLabel")
        oolsLabel.place(x=450,y=28, height=100, width=170)
        oolsLabel.config(font=("Mincho Bold", 60), bg="#ffcc00", fg="#003011")

        self.permanentLabels = [".rLabel", ".egLabel", ".tLabel", ".oolsLabel", ".studentName"]
        # "Search" Label
        
        searchLabel = Label(master, text='Search:')
        searchLabel.place(x=290,y=260, height=40, width=80)
        searchLabel.config(font=("Arial Bold", 16))
        searchLabel.config(bg="#003011", fg="White")

        # "Student" Label
        studentLabel = Label(master, text='Student:')
        studentLabel.place(x=260,y=160, height=40, width=80)
        studentLabel.config(font=("Arial Bold", 20))
        studentLabel.config(bg="#003011", fg="White")

        # Student Name Label (Updates)
        self.labl = Label(master, text=' ', name = "studentName")
        self.labl.place(x=370,y=160, height=40, width=220)
        self.labl.config(font=("Arial Bold", 20))
        self.labl.config(bg="#003011", fg="White")

        # Creates the search textbox/entrybox
        self.nameVar = StringVar()
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)
        searchbox = Entry(master, textvariable=self.search_var)
        searchbox.place(x=360,y=267, height=26, width=145)

        # List box geometry
        self.lb.grid(row=1, rowspan=10, column=0,columnspan=5, sticky='W', padx=5, pady=5,ipadx=5, ipady=5)
        self.lb.bind("<Double-Button-1>", self.onClick)

        # All items in the listbox get stored in "all_items"

    def loadLB(self):
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
        search_term = self.search_var.get()
        self.lb.delete(0, END)
        for item in self.nameList:
            if search_term.lower() in item.lower():
                self.lb.insert(END, item)

    def onClick(self, event):
        w=event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.labl['text'] = self.lb.get(self.lb.curselection())
        classMgmt(self.master)

    def addStuentButtonClick(self):
        addStudent(self.master)


root = tk.Tk()
myGUI = mainMenu(root)
myGUI.loadLB()
root.mainloop()