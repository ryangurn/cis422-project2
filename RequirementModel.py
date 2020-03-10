"""
RequirementModel.py will act as an ORM for the requirements table in the sqlite database
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
Ryan Gurnick - 03/05/20  Creation

"""
import json
import sqlite3
from datetime import date, datetime

import Datastore


class RequirementModel:
    def __init__(self, db_file):
        """
        Initializer for the requirement model. This will want to know which file to look at for the db.
        Then it will provide a connection to that database and allow for some ORM operations, such
        as insert and select.

        db_file :str

        Example Usage:
        rm = RequirementModel.RequirementModel('testing.db')
        """
        # init db connection using the datastore
        self.conn = Datastore.DB(db_file).ret().conn

    def _insert(self, term, major, type, data):
        """
        Insert method for the requirement model that allows the caller to provide the specified
        information and create a record within the database, this will return the id of
        the row created.
        :param term:
        :param major:
        :param type:
        :param data:
        :return:
        """
        sql = '''INSERT INTO "main"."requirements"("term","major","type","data","created_at","updated_at") VALUES (?,?,?,?,?,?);'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, (term, major, type, data, date.today(), date.today()))
            self.conn.commit()
            cur.close()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def setupTable(self):
        """
        This method will seed the database and ensure that the required rows exist for
        requirements. This data is manually generated and then added here to ensure
        that its in the initial seed and the empty database if needed.
        :return:
        """
        # CIS BS
        BS = 'BS'
        # year 1 fall
        self._insert(0, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 122 Introduction to Programming and Problem Solving",
                "milestones": "",
                "course": "CIS 122"
            },
            {
                "description": "MATH 112 Elementary Functions",
                "milestones": "",
                "course": "MATH 112"
            },
            {
                "description": "General-education course in arts and letters",
                "milestones": "",
                "course": ">1"
            },
            {
                "description": "General-education course in social science",
                "milestones": "",
                "course": ">2"
            }
        ]))
        # year 1 winter
        self._insert(1, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 210 Computer Science I",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 210"
            },
            {
                "description": "MATH 231 Elements of Discrete Mathematics I",
                "milestones": "Need grade of B- or better for majors",
                "course": "MATH 231"
            },
            {
                "description": "WR 121 College Composition I",
                "milestones": "",
                "course": "WR 121"
            },
            {
                "description": "General-education course in arts and letters",
                "milestones": "",
                "course": ">1"
            }
        ]))
        # year 1 spring
        self._insert(2, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 211 Computer Science II",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 211"
            },
            {
                "description": "MATH 232 Elements of Discrete Mathematics II",
                "milestones": "Need grade of B- or better for majors",
                "course": "MATH 232"
            },
            {
                "description": "WR 122 College Composition II/WR 123 College Composition III",
                "milestones": "",
                "course": "WR 122/123"
            },
            {
                "description": "General-education course in social science",
                "milestones": "",
                "course": ">2"
            },
        ]))
        # year 1 summer (no classes)
        self._insert(3, "Computer & Information Science", BS, json.dumps([]))
        # year 2 fall
        self._insert(4, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 212 Computer Science III",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 212"
            },
            {
                "description": "MATH 251 Calculus I/MATH 246 Calculus for the Biological Sciences I/MATH 261 Calculus "
                               "with Theory I",
                "milestones": "",
                "course": "MATH 251/246/261"
            },
            {
                "description": "General-education course in arts and letters",
                "milestones": "",
                "course": ">1"
            },
            {
                "description": "General-education course in social science",
                "milestones": "",
                "course": ">2"
            },
        ]))
        # year 2 winter
        self._insert(5, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 313 Intermediate Data Structures",
                "milestones": "",
                "course": "CIS 313"
            },
            {
                "description": "CIS 314 Computer Organization",
                "milestones": "",
                "course": "CIS 314"
            },
            {
                "description": "MATH 252 Calculus II/MATH 246 Calculus for the Biological Sciences II/MATH 261 "
                               "Calculus with Theory II",
                "milestones": "",
                "course": "MATH 252/246/262"
            },
            {
                "description": "General-education course in arts and letters that also satisfies multicultural "
                               "requirement",
                "milestones": "",
                "course": ">1 AC IP IC"
            },
        ]))
        # year 2 spring
        self._insert(6, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 315 Intermediate Algorithms",
                "milestones": "",
                "course": "CIS 315"
            },
            {
                "description": "CIS 330 C/C++ and Unix",
                "milestones": "",
                "course": "CIS 330"
            },
            {
                "description": "MATH 253 Calculus III/MATH 283 Calculus with Theory III/MATH 341 Elementary Linear "
                               "Algebra/MATH 343 Statistical Models and Methods/MATH 425 Statistical Methods I",
                "milestones": "",
                "course": "MATH 253/283/341"
            },
            {
                "description": "General-education course in social science that also satisfies a multicultural "
                               "requirement",
                "milestones": "",
                "course": ">2 AC IP IC"
            },
        ]))
        # year 2 summer
        self._insert(7, "Computer & Information Science", BS, json.dumps([]))
        # year 3 fall
        self._insert(8, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 415 Operating Systems",
                "milestones": "",
                "course": "CIS 415"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "Maximum of 8 upper-division elective credits in courses with numbers less than 410",
                "course": ""
            },
            {
                "description": "First course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 3 winter
        self._insert(9, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 422 Software Methodology I",
                "milestones": "",
                "course": "CIS 422"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Second course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 3 spring
        self._insert(10, "Computer & Information Science", BS, json.dumps([
            {
                "description": "CIS 425 Principles of Programming Languages",
                "milestones": "",
                "course": "CIS 425"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Third course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 3 summer
        self._insert(11, "Computer & Information Science", BS, json.dumps([]))
        # year 4 fall
        self._insert(12, "Computer & Information Science", BS, json.dumps([
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Upper-division mathematics elective",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 4 winter
        self._insert(13, "Computer & Information Science", BS, json.dumps([
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Upper-division mathematics elective",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 4 spring
        self._insert(14, "Computer & Information Science", BS, json.dumps([
            {
                "description": "WR 320/321",
                "milestones": "",
                "course": "WR 320/321"
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 2",
                "milestones": "",
                "course": ""
            },
        ]))
        # year 4 summer
        self._insert(15, "Computer & Information Science", BS, json.dumps([]))

        # CIS BA
        BA = 'BA'
        # year 1 fall
        self._insert(0, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 122 Introduction to Programming and Problem Solving",
                "milestones": "",
                "course": "CIS 122"
            },
            {
                "description": "MATH 112 Elementary Functions",
                "milestones": "",
                "course": "CIS 112"

            },
            {
                "description": "First term of second-language sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "General-education course in social science",
                "milestones": "",
                "course": ">2"
            }
        ]))
        # year 1 winter
        self._insert(1, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 210 Computer Science I",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 210"
            },
            {
                "description": "MATH 231 Elements of Discrete Mathematics I",
                "milestones": "Need grade of B- or better for majors",
                "course": "MATH 231"
            },
            {
                "description": "WR 121 College Composition I",
                "milestones": "",
                "course": "WR 121"
            },
            {
                "description": "Second term of second-language sequence",
                "milestones": "",
                "course": ""
            }
        ]))
        # year 1 spring
        self._insert(2, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 211 Computer Science II",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 211"
            },
            {
                "description": "MATH 232 Elements of Discrete Mathematics II",
                "milestones": "Need grade of B- or better for majors",
                "course": "MATH 232"
            },
            {
                "description": "WR 122/WR 123",
                "milestones": "",
                "course": "WR 122/123"
            },
            {
                "description": "Third term of second-language sequence",
                "milestones": "",
                "course": ""
            }
        ]))
        # year 1 summer
        self._insert(3, "Computer & Information Science", BA, json.dumps([]))
        # year 2 fall
        self._insert(4, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 212 Computer Science III",
                "milestones": "Need grade of B- or better for majors",
                "course": "CIS 212"
            },
            {
                "description": "Math 251/Math 246/Math 261",
                "milestones": "",
                "course": "MATH 251/246/261"
            },
            {
                "description": "General-education course in arts and letters",
                "milestones": "",
                "course": ">1"
            },
            {
                "description": "General-education course in social science",
                "milestones": "",
                "course": ">2"
            }
        ]))
        # year 2 winter
        self._insert(5, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 313 Intermediate Data Structures",
                "milestones": "",
                "course": "CIS 313"
            },
            {
                "description": "CIS 314 Computer Organization",
                "milestones": "",
                "course": "CIS 314"
            },
            {
                "description": "MATH 252/MATH 247/MATH 262",
                "milestones": "",
                "course": "MATH 252/247/262"
            },
            {
                "description": "General-education course in arts and letters that also satisfies multicultural requirement",
                "milestones": "",
                "course": ">1 AC IP IC"
            }
        ]))
        # year 2 spring
        self._insert(6, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 315 Intermediate Algorithms",
                "milestones": "",
                "course": "CIS 315"
            },
            {
                "description": "CIS 330 C/C++ and Unix",
                "milestones": "",
                "course": "CIS 330"
            },
            {
                "description": "MATH 253/MATH 263/MATH 341/MATH 343/MATH 425",
                "milestones": "",
                "course": "MATH 253/263/341/343/425"
            },
            {
                "description": "General-education course in social science that also satisfies a multicultural "
                               "requirement",
                "milestones": "",
                "course": ">2 AC IP IC"
            }
        ]))
        # year 2 summer
        self._insert(7, "Computer & Information Science", BA, json.dumps([]))
        # year 3 fall
        self._insert(8, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 415 Operating Systems",
                "milestones": "",
                "course": "CIS 415"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "Maximum of 8 upper-division elective credits in courses with numbers less than 410",
                "course": ""
            },
            {
                "description": "First course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "General-education course in arts and letters",
                "milestones": "",
                "course": ">1"
            },
        ]))
        # year 3 winter
        self._insert(9, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 422 Software Methodology I",
                "milestones": "",
                "course": "CIS 422"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Second course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "General-education course in social science that also meets multicultural requirements",
                "milestones": "",
                "course": ">2"
            }
        ]))
        # year 3 spring
        self._insert(10, "Computer & Information Science", BA, json.dumps([
            {
                "description": "CIS 425 Principles of Programming Languages",
                "milestones": "",
                "course": "CIS 425"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Third course of additional science sequence",
                "milestones": "",
                "course": ""
            },
            {
                "description": "General-education course in arts and letters that also meets multicultural requirements",
                "milestones": "",
                "course": ">1"
            }
        ]))
        # year 3 summer
        self._insert(11, "Computer & Information Science", BA, json.dumps([]))
        # year 4 fall
        self._insert(12, "Computer & Information Science", BA, json.dumps([
            {
                "description": "MATH 253/263/341/343/425",
                "milestones": "",
                "course": "MATH 253/263/341/343/425"
            },
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            }
        ]))
        # year 4 winter
        self._insert(13, "Computer & Information Science", BA, json.dumps([
            {
                "description": "Upper-division elective course with CIS subject code",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Upper-division mathematics elective",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            }
        ]))
        # year 4 spring
        self._insert(14, "Computer & Information Science", BA, json.dumps([
            {
                "description": "WR 320/321",
                "milestones": "",
                "course": "WR 320/321"
            },
            {
                "description": "Elective course 1",
                "milestones": "",
                "course": ""
            },
            {
                "description": "Elective course 2",
                "milestones": "",
                "course": ""
            }
        ]))
        # year 4 summer
        self._insert(15, "Computer & Information Science", BA, json.dumps([]))

    def find_by(self, haystack, needle):
        """
        Search for records within the requirements table and return them as lists of lists.

        :param
        haystack :str
        needle :str

        return :list

        Example Usage:
        rm = RequirementModel.RequirementModel('testing.db')
        rm.find_by('term', 201901)
        rm.find_by('type', 321321)
        """
        sql = "SELECT * FROM \"main\".\"requirements\" WHERE \"{}\" = \"{}\"".format(haystack, needle)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find(self, major, type):
        """
        Find for records within the requirements table and return them as lists of lists.

        :param
        major :str
        type :str

        return :list

        Example Usage:
        rm = RequirementModel.RequirementModel('testing.db')
        rm.find('CIS', "BA")
        """
        sql = "SELECT * FROM \"main\".\"requirements\" WHERE \"major\" = \"{}\" AND \"type\" = \"{}\"".format(major,
                                                                                                              type)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()

    def find_by_term(self, major, type, term):
        """
        Find for records within the requirements table and return them as lists of lists.

        :param
        major :str
        type :str

        return :list

        Example Usage:
        rm = RequirementModel.RequirementModel('testing.db')
        rm.find('CIS', "BA")
        """
        sql = "SELECT * FROM \"main\".\"requirements\" WHERE \"major\" = \"{}\" AND \"type\" = \"{}\" AND \"term\" = \"{}\" ".format(
            major, type, term)
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except ValueError:
            return cur.fetchall()
        return cur.fetchall()
