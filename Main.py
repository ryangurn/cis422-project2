"""
Main.py is the first file that will be run when the program starts being run
This will start the running of all other subroutines for graphics, parsing,
processing.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Priority credit to:
Ryan Gurnick - 2/25/20  Creation

"""
import Parser
import ClassParser
import Datastore
import ClassModel
import StudentModel
import StudentClassModel
import os
import GUI.MainMenu
import tkinter as tk

DB = 'testing.db'

if not os.path.exists('testing.db'):
    # setup datastore
    ds = Datastore.DB(DB)
    ds.generateTables()

# # call ClassParser
# p = ClassParser.ClassParser("201903", "CIS")
# p.deleteFormatting()
# p.parseData()

# call RequirementsParser
# rp = RequirementsParser.RequirementsParser()
# rp.parseData()

# classModel = ClassModel.ClassModel('testing.db')
# print(classModel.update(201901, 'testing123', 'BIC', '123', '{}', '{}'))
# print(classModel.find_by('term', 201903))

# studentModel = StudentModel.StudentModel('testing.db')
# studentModel.insert("Ryan Gurnick")
# print(studentModel.find("Ryan Gurnick"))
# print(studentModel.search("Gurnick"))

# studentClassModel = StudentClassModel.StudentClassModel('testing.db')
# studentClassModel.associate(1,1)

root = tk.Tk()
root.resizable(False, False)
myGUI = GUI.MainMenu.MainMenu(root, DB)
root.mainloop()
