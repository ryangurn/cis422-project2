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
import RequirementsParser
import Datastore
import ClassModel
import os

DB = 'testing.db'

if not os.path.exists('testing.db'):
    # setup datastore
    ds = Datastore.DB(DB)
    ds.generateTables()

# # call ClassParser
p = ClassParser.ClassParser("201903", "BI")
p.deleteFormatting()
p.parseData()

# call RequirementsParser
# rp = RequirementsParser.RequirementsParser()
# rp.parseData()

# classModel = ClassModel.ClassModel('testing.db')
# print(classModel.insert(321321, 201901, '123', '{}', '{}'))
# print(classModel.find_by('term', 201903))