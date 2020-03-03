"""
StudentClassModel.py will act as an ORM for the class table in the sqlite database
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
Ryan Gurnick - 03/02/20  Creation

"""
import Datastore
import sqlite3
from datetime import date, datetime


class StudentClassModel:
    def __init__(self, db_file):
        """
        Initializer for the student class model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM opterations, such
        as insert and select.

        db_file :str

        Example Usage:
        scm = StudentClassModel.StudentClassModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

    def associate(self, student_id, class_id):
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
        scm = StudentModel.StudentModel('testing.db')
        scm.associate(1, 3) where 1 is the student_id and 3 is the class_id
        """
        sql = '''INSERT INTO "main"."students_classes"("students_id","classes_id","created_at","updated_at") VALUES (?,?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (student_id, class_id, date.today(), date.today()))
            self.conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None