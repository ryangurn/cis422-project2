"""
ClassModel.py will act as an ORM for the class table in the sqlite database
to the objects that we will use within this application. This will attempt
to make querying the table much simpler.

Authors:
(RegTools)
Joseph Goh
Mason Sayyadi
Owen McEvoy
Ryan Gurnick
Samuel Lundquist

Priority credit to:
Ryan Gurnick - 2/27/20  Creation

"""
import Datastore
import sqlite3
from datetime import date, datetime


class ClassModel:

    def __init__(self, db_file):
        """
        Initializer for the class model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM opterations, such
        as insert and select.

        db_file :str

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

    def insert(self, term, name, subject, number, credits, sections):
        """
        Insert method for the class model that allows the caller to provide the specified
        information and create a record within the database, this will return the id of
        the row created.

        :param
        name :str
        subject :str
        number :str
        credits :str
        sections :str

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        cm.insert(321321, 201901, '123', '{}', '{}')
        """
        sql = '''INSERT INTO "main"."classes"("term","name","subject","number","credits","sections","created_at","updated_at") VALUES (?,?,?,?,?,?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (term, name, subject, number, credits, sections, date.today(), date.today()))
            self.conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def find_by(self, haystack, needle):
        """
        Search for records within the class database and return them as lists of lists.

        :param
        haystack :str
        needle :str

        return :list

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        cm.find_by('term', 201901)
        cm.find_by('crn', 321321)
        """
        sql = "SELECT * FROM \"main\".\"classes\" WHERE \"{}\" = \"{}\"".format(haystack, needle)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()
