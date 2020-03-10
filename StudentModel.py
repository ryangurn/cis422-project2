"""
StudentModel.py will act as an ORM for the class table in the sqlite database
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


class StudentModel:

    def __init__(self, db_file):
        """
        Initializer for the student model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM opterations, such
        as insert and select.

        :param
        db_file :str

        Example Usage:
        sm = StudentModel.StudentModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

    def insert(self, name):
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
        sm = StudentModel.StudentModel('testing.db')
        sm.insert("Ryan Gurnick")
        """
        sql = '''INSERT INTO "main"."students"("name","created_at","updated_at") VALUES (?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (name, date.today(), date.today()))
            self.conn.commit()
            cur.close()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def find(self, name):
        """
        Search for records within the class database and return them as lists of lists.

        :param
        name :str

        return :list

        Example Usage:
        sm = StudentModel.StudentModel('testing.db')
        sm.find("Ryan Gurnick")
        """
        sql = "SELECT * FROM \"main\".\"students\" WHERE \"name\" = \"{}\"".format(name)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            data = cur.fetchall()
            cur.close()
            return data
        data = cur.fetchall()
        cur.close()
        return data

    def search(self, name):
        """
        Search for records within the class database and return them as lists of lists.

        :param
        name :str

        return :list

        Example Usage:
        sm = StudentModel.StudentModel('testing.db')
        sm.search("Ryan Gurnick")
        """
        sql = "SELECT * FROM \"main\".\"students\" WHERE \"name\" LIKE '%{}%' ORDER BY \"id\" ASC LIMIT 0, 49999;".format(
            name)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            data = cur.fetchall()
            cur.close()
            return data
        data = cur.fetchall()
        cur.close()
        return data

    def all(self):
        """
        Returns all student records in the database.

        :param
        None

        return :list

        Example Usage:
        sm = StudentModel.StudentModel('testing.db')
        sm.all()
        """
        sql = "SELECT * FROM \"main\".\"students\";"
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            data = cur.fetchall()
            cur.close()
            return data
        data = cur.fetchall()
        cur.close()
        return data

    def delete(self, id):
        """
        Delete a student record from the database.

        :param
        id :integer

        return :list

        Example Usage:
        sm = StudentModel.StudentModel('testing.db')
        sm.delete(1)
        """
        sql = "DELETE FROM \"main\".\"students\" WHERE id IN ('{}');".format(id)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except ValueError:
            data = cur.fetchall()
            cur.close()
            return data
        data = cur.fetchall()
        cur.close()
        return data
