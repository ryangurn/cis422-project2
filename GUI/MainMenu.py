"""

MainMenu.py is the main graphics module dedicated to the setup and display
of the initial viewport for the program. It also handles user interaction
with the window.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Created:

"""

import sqlite3
from tkinter import *
from tkinter import messagebox

import StudentModel
from GUI.AddStudent import *
from GUI.ClassManagement import *
from GUI.CollectData import *


class MainMenu(tk.Tk):
    def __init__(self, master, db_file):
        """
        Initializer for the MainMenu window. This function requires the name
        of the database to connect and interact with. It also requires the
        master window from tkinter to interface with.

        :param
        master :tkinter.Tk
        db_file :str

        Example Usage:
        root = tk.Tk()
        root.resizable(False, False)
        myGUI = MainMenu(root, 'test.db')
        """
        self.db = db_file
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
        grayBoxFrame = Frame(master, width=800, height=390, bg=self._darkGrey)
        grayBoxFrame.place(x=0, y=150)
        fr = Frame(master, width=200, height=200, bg=self._green)
        fr.place(x=300, y=252)

        # Creates Menu Bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # Add Student label
        studentBtn = Label(master, text='Add Student')
        studentBtn.config(font=("Arial Bold", 13), bg=self._green, fg=self._yellow)
        studentBtn.place(x=348, y=465, height=27, width=106)
        studentBtn.bind(self._button, self.addStudentButtonClick)

        # Select Data label
        collectBtn = Label(master, text='Collect Data')
        collectBtn.config(font=("Arial Bold", 13), bg=self._green, fg=self._yellow)
        collectBtn.place(x=348, y=500, height=27, width=106)
        collectBtn.bind(self._button, self.collectBtnClick)

        logo = PhotoImage(file="./img/RegToolsLogo.gif")
        label = Label(image=logo, borderwidth=0)
        label.image = logo
        label.place(x=100, y=40)

        # Makes RegTool title
        logoPad = Label(master, text='')
        logoPad.place(x=95, y=40, height=5, width=620)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(master, text='')
        logoPad.place(x=98, y=40, height=90, width=5)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(master, text='')
        logoPad.place(x=701, y=40, height=90, width=5)
        logoPad.config(bg=self._backgroundColor)
        logoPad = Label(master, text='')
        logoPad.place(x=95, y=121, height=5, width=620)
        logoPad.config(bg=self._backgroundColor)

        # Name listbox properties
        self.lb = Listbox(fr, selectmode="browse", bg=self._backgroundColor, selectbackground=self._green)
        self.loadLB()
        self.lb.config(font=("Mincho Bold", 16), fg="#e6e6e6")
        self.lb.place(x=5, y=5, height=190, width=190)
        self.lb.bind('<Double-Button-1>', self.onClick)
        self.lb.bind("d", self.deleteName)

        # "Search" Label
        searchLabel = Label(master, text='Search:')
        searchLabel.place(x=290, y=205, height=40, width=80)
        searchLabel.config(font=("Arial Bold", 16), bg=self._darkGrey, fg=self._yellow)

        self.nameVar = StringVar()
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)

        # Creates the search textbox/entrybox
        searchbox = Entry(master, textvariable=self.search_var, bg=self._lightGrey)
        searchbox.place(x=360, y=215, height=20, width=141)
        searchbox.config(highlightthickness=0)

        # 'D' Key label
        dKeyLabel = Label(master, text='= Deletes Name')
        dKeyLabel.place(x=547, y=550, height=30, width=200)
        dKeyLabel.config(font=("Arial Bold", 18))
        dKeyLabel.config(bg=self._backgroundColor, fg="Grey")

        # Key label
        dKey = Label(master, text="'D'")
        dKey.place(x=543, y=550, height=30, width=30)
        dKey.config(font=("Arial Bold", 20))
        dKey.config(bg="Grey", fg=self._backgroundColor)

    def loadLB(self):
        """
        Loads in student names that are already added to the database.

        :param
        None

        Example Usage:
        //initialize Listbox first, then you can call loadLB()
        self.lb = Listbox(fr, selectmode="browse", bg=self._backgroundColor, selectbackground=self._green)
        self.loadLB()
        """
        self.numberOfNames = 0
        self.nameList = []

        sm = StudentModel.StudentModel(self.db)
        for item in sm.all():
            self.lb.insert(END, item[1])
            self.nameList.append(item[1])
            self.numberOfNames += 1

    def update_listbox(self, *args):
        """
        Function to update the listbox based on what the user has entered in
        the search box on the MainMenu window. Listbox will only display
        student names that are in the database and contain the string in the
        search box.

        :param
        event :None

        Example Usage:
        //When the StringVar changes, call self.update_listbox
        self.search_var = StringVar()
        self.search_var.trace('w', self.update_listbox)
        """
        self.loadLB()
        search_term = self.search_var.get()
        self.lb.delete(0, END)
        for item in self.nameList:
            if search_term.lower() in item.lower():
                self.lb.insert(END, item)

    def onClick(self, event):
        """
        A function used to perform a specific set of actions when a particular
        item is activated with an event. The item must be bound to this function
        for the action to occur. Once activated through an event, the system
        will find the currently selected item(student) from the MainMenu window
        and load the ClassManagement window for that student.

        :param
        event :the event type of an item binded to this function

        Example Usage:
        //Binds a double-click event on Listbox to this function
        self.lb.bind('<Double-Button-1>', self.onClick)
        """
        w = event.widget
        if not w.curselection() == ():
            index = int(w.curselection()[0])
            selectedStudent = w.get(index)
            ClassManagement(self.master, selectedStudent, self.db)

    def collectBtnClick(self, event):
        """
        A function used to launch the collectData window when an event occurs.
        This function should be bound to an onclick event on the collectBtn.

        :param
        event :the event type of an item bound to this function

        Example Usage:
        //Binds a left click action on the collectBtn to this function
        collectBtn.bind("<Button-1>", self.collectBtnClick)
        """
        collectData(self.master, self.db)

    def deleteName(self, event):
        """
        Function used to delete students from the database when their info
        is no longer needed/they no longer need to registration assistance.
        Also prompts the user to confirm the action prior to deletion.

        :param
        event :the event type of an item bound to this function

        Example Usage:
        //Binds the 'd' key to this function for deleting students
        self.lb.bind("d", self.deleteName)
        """
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
        """
        A function used to launch the AddStudent window when an event occurs.
        This function should be bound to an onclick event on the studentBtn.

        :param
        event :the event type of an item bound to this function

        Example Usage:
        //Binds the left mouse click action on studentBtn to call this function
        studentBtn.bind("<Button-1>", self.addStudentButtonClick)
        """
        AddStudent(self.master, self.db, self.lb)
