"""
TogglesModel.py will act as an ORM for the roadmaps_toggles table in the sqlite database
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
March 7nd, 2020

"""
import json
import sqlite3
from datetime import date, datetime

import Datastore


class TogglesModel:
    def __init__(self, db_file):
        """
        Initializer for the road maps toggles model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM opterations, such
        as insert and select.

        :param
        db_file :str

        Example Usage:
        tm = TogglesModel.TogglesModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

        """INSERT INTO "main"."roadmap_toggles"("id","requirements_id","students_id","highlight","created_at",
        "updated_at") VALUES (NULL,NULL,NULL,NULL,NULL,NULL); 
        DELETE FROM "main"."roadmap_toggles" WHERE id IN ('1'); 
        SELECT ,* FROM "main"."roadmap_toggles" WHERE "requirements_id" LIKE '%1%' AND "students_id" LIKE '%2%' AND 
        "highlight" LIKE '%a%'; """

    def insert(self, requirements_id, students_id, text):
        """
        Insert method for the class model that allows the caller to provide the specified
        information and create a record within the database, this will return the id of
        the row created.

        :param
        requirements_id :int
        students_id :int
        text :str

        Example Usage:
        tm = TogglesModel.TogglesModel('testing.db')
        tm.insert(1, 1, "Required")
        """
        # "lecture_count", "lab_count", "discussion_count", "other_count"

        sql = '''INSERT INTO "main"."roadmap_toggles"("requirements_id","students_id","highlight","created_at",
        "updated_at") VALUES (?,?,?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (requirements_id, students_id, text, date.today(), date.today()))
            self.conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def delete(self, requirements_id, students_id, text):
        """
        Delete method for the class model that allows the caller to delete a record within the database.

        :param
        requirements_id :int
        students_id :int
        text :str

        Example Usage:
        tm = TogglesModel.TogglesModel('testing.db')
        tm.delete(1, 1, "Required")
        """
        sql = "DELETE FROM \"main\".\"roadmap_toggles\" WHERE \"requirements_id\" = \"{}\" AND \"students_id\" = \"{}\" AND \"highlight\" = \"{}\";".format(requirements_id, students_id, text)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except ValueError:
            return cur.fetchall()

    def find_using(self, requirements_id, students_id, text):
        """
        Find method for the class model that allows the caller to find a record within the database.

        :param
        requirements_id :int
        students_id :int
        text :str

        Example Usage:
        tm = TogglesModel.TogglesModel('testing.db')
        tm.find(1, 1, "Required")
        """
        sql = "SELECT * FROM \"main\".\"roadmap_toggles\" WHERE \"requirements_id\" = '{}' AND \"students_id\" " \
              "='{}' AND \"highlight\" = '{}';".format(requirements_id, students_id, text)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find(self, students_id):
        """
        Find method for the class model that allows the caller to find a record within the database.

        :param
        students_id :int

        Example Usage:
        tm = TogglesModel.TogglesModel('testing.db')
        tm.find(1, 1, "Required")
        """
        sql = "SELECT * FROM \"main\".\"roadmap_toggles\" WHERE  \"students_id\" = '{}' ".format(students_id)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()
