"""
Datastore.py will establish a connection with the database that will fill in the content
of this application. It will be the persistent data store for the classes and student
status.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

References: https://www.tutorialspoint.com/sqlite/sqlite_python.htm

Priority credit to:
Ryan Gurnick - 2/27/20  Creation

"""
import sqlite3

class DB:

    def __init__(self, db_name: string):
        self.conn = sqlite3.connect(db_name)