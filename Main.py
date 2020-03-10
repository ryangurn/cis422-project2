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
import Datastore
import os
import GUI.MainMenu
import tkinter as tk

DB = 'testing.db'

os.environ['TK_SILENCE_DEPRECATION'] = "1"

if not os.path.exists('testing.db'):
    # setup datastore
    ds = Datastore.DB(DB)
    ds.generateTables()

root = tk.Tk()
root.resizable(False, False)
myGUI = GUI.MainMenu.MainMenu(root, DB)
root.mainloop()
