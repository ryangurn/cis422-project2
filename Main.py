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
import RequirementsParser
import Datastore

# # call ClassParser
p = ClassParser.ClassParser("201903", "CIS")
p.deleteFormatting()
p.parseData()

# call RequirementsParser
# rp = RequirementsParser.RequirementsParser()
# rp.parseData()

# setup datastore
#ds = Datastore.DB("testing.db")
#ds.generateTables()
