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
import sqlite3
from datetime import date, datetime

import Datastore


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

    def insert(self, term, name, subject, number, credits, total_count, lecture_count, lab_count, discussion_count,
               other_count, sections):
        """
        Insert method for the class model that allows the caller to provide the specified
        information and create a record within the database, this will return the id of
        the row created.

        :param
        name :str
        subject :str
        number :str
        credits :str
        total_count :int
        lecture_count :int
        lab_count :int
        discussion_count :int
        other_count :int
        sections :str

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        cm.insert(321321, 201901, '123', '{}', 1, 2, 0, 0, '{}')
        """
        # "lecture_count", "lab_count", "discussion_count", "other_count"

        sql = '''INSERT INTO "main"."classes"("term","name","subject","number","credits","total_count", "lecture_count", "lab_count", "discussion_count", "other_count","sections","created_at","updated_at") VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (
                term, name, subject, number, credits, total_count, lecture_count, lab_count, discussion_count,
                other_count,
                sections, date.today(), date.today()))
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

    def find_by_term(self, subject, year, term):
        """
        Search for records within the class database and return them as lists of lists.

        :param
        subject :str
        year :str
        term :str

        return :list

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        cm.find_by_term('CIS', 2019, 1)
        cm.find_by_term('CIS', 2015, 2)
        """
        s = str(year) + "0" + str(term)

        sql = "SELECT * FROM \"main\".\"classes\" WHERE \"subject\" = \"{}\" AND \"term\" = \"{}\";".format(subject, s)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find_class_id(self, subject, courseNumber, term):
        """
        Finds records in the classes table given a subject, courseNumber, and term
        :param subject:
        :param courseNumber:
        :param term:
        :return:
        """
        sql = "SELECT \"number\", \"id\"  FROM \"main\".\"classes\" WHERE \"subject\" = \"{}\" and \"number\" = \"{}\" and \"term\" = \"{}\";".format(
            subject, courseNumber, term)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def predict_future_class_id(self, subject, courseNumber):
        """
        The query used to determine the most recent occurance of a specific subject and course number combination.
        :param subject:
        :param courseNumber:
        :return:
        """
        sql = "SELECT \"number\", \"id\" FROM \"main\".\"classes\" WHERE \"subject\" = \"{}\" AND \"number\" = {} ORDER BY \"term\" desc LIMIT 1;".format(
            subject, courseNumber)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except:
            return cur.fetchall()
        return cur.fetchall()

    def crt_class_search(self, typeNum, priorYear):
        """
        This function takes the type code for the arts and letters or social sciences and then
        returns a list of courses that have at least one record.

        :param typeNum:
        :param priorYear:
        :return:
        """
        sql = """SELECT \"subject\", \"term\", \"number\", \"name\", \"aprnce\"
		        FROM (SELECT \"subject\", \"term\", \"number\", \"name\",count(*) as \"aprnce\"
                    FROM \"main\".\"classes\" WHERE \"term\" like \"{}%\"
                    GROUP BY \"subject\", \"number\") miniQuery
                WHERE \"aprnce\" = 1
                AND name like \"%>{}\" 
                ORDER BY \"subject\", \"number\" asc;""".format(priorYear, typeNum)

        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def delete_sub_term(self, subject, term):
        """
        This function will delete a set of records from the database given a subject and term that match.

        :param subject:
        :param term:
        :return:
        """
        sql = "DELETE FROM \"main\".\"classes\" WHERE \"subject\" = \"{}\" AND \"term\" = \"{}\";".format(subject, term)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except ValueError:
            return cur.fetchall()

    def count(self, subject, number):
        """
        This function will provide count values for the critical counts and fill in the data
        for previous section distribution.

        :param subject:
        :param number:
        :return:
        """
        sql = "SELECT \"term\", \"subject\", \"number\", \"total_count\", \"lecture_count\", \"lab_count\", \"discussion_count\", \"other_count\" FROM \"main\".\"classes\" WHERE \"subject\"=\"{}\" AND \"number\"=\"{}\";".format(
            subject, number)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find_course(self, name, subject, number, term, year):
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
        s = str(year) + "0" + str(term)
        t = None
        y = int(year)
        if term == "Fall":
            t = 1
        elif term == "Winter":
            y -= 1
            t = 2
        elif term == "Spring":
            y -= 1
            t = 3
        elif term == "Summer":
            y -= 1
            t = 4

        sql = "SELECT * FROM \"main\".\"classes\" WHERE \"name\" LIKE '%{}%' AND \"subject\" LIKE '%{}%' AND \"number\" LIKE '%{}%' and \"term\" = '{}' ".format(
            name, subject, number, str(y) + "0" + str(t))
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def distinct(self, needle):
        """
        Get the distinct values for the column of needle.

        :param
        needle :str

        return :list

        Example Usage:
        cm = ClassModel.ClassModel('testing.db')
        cm.distinct('subject')
        """
        sql = "SELECT DISTINCT {} FROM classes".format(needle)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()
