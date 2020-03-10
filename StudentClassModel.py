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

Created:
March 2nd, 2020

"""
import sqlite3
from datetime import date, datetime

import Datastore


class StudentClassModel:
    def __init__(self, db_file):
        """
        Initializer for the student class model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM opterations, such
        as insert and select.

        :param
        db_file :str

        Example Usage:
        scm = StudentClassModel.StudentClassModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

    def associate(self, student_id, class_id):
        """
        Associate will allow you to insert a record into the students_classes model
        and create a relationship between a student and class based on completion of
        the couse.

        :param
        student_id :int
        class_id :int

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

    def disassociate(self, student_id, class_id):
        """
        The disassociate function allows you to delete the relationship between the student
        and class model. This should also help update the list in the case of a reload of the
        view later on.

        :param
        student_id :int
        class_id :int

        Example Usage:
        scm = StudentModel.StudentModel('testing.db')
        scm.disassociate(1, 3) where 1 is the student_id and 3 is the class_id
        """
        sql = "DELETE FROM \"main\".\"students_classes\" WHERE \"students_id\" = '{}' AND \"classes_id\" = '{}';".format(
            student_id, class_id)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find(self, haystack, needle, sort=None):
        """
        Find a set of records within the class database and return them as lists of lists.

        :param
        needle :str
        haystack :str

        return :list

        Example Usage:
        scm = StudentClassModel.StudentClassModel('testing.db')
        scm.find("student_id", 1)
        """
        if sort == None:
            sql = "SELECT * FROM \"main\".\"students_classes\" WHERE \"{}\" = \"{}\"".format(haystack, needle)
        else:
            sql = "SELECT * FROM \"main\".\"students_classes\" WHERE \"{}\" = \"{}\" {}".format(haystack, needle, sort)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()
