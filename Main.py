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
import requests
import Parser
import ClassParser


# # call ClassParser
p = ClassParser.ClassParser("201903", "CIS")
p.deleteFormatting()

