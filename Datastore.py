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

import RequirementModel


class DB:

    def __init__(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        self.db = db_file
        conn = None
        try:
            conn = sqlite3.connect(db_file, timeout=1)
            self.conn = conn
            return
        except Error as e:
            print(e)

        self.conn = conn
        return

    def ret(self):
        return self

    def _create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def generateTables(self):
        """
        This function will generate all of the required tables within the sqlite file for
        us and allow us to start with a common basis in sql.

        Example Usage:
        ds = Datastore.Datastore('testing.db')
        ds.generateTables()
        """
        if self.conn is not None:
            self._create_table("""CREATE TABLE "classes" (
                    	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    	"term"	integer NOT NULL,
                    	"name"	text NOT NULL,
                    	"subject"	text NOT NULL,
                    	"number"	text NOT NULL,
                    	"credits"	text NOT NULL,
                    	"total_count"	INTEGER DEFAULT 0,
                    	"lecture_count"	INTEGER DEFAULT 0,
                    	"lab_count"	INTEGER DEFAULT 0,
                    	"discussion_count"	INTEGER DEFAULT 0,
                    	"other_count"	INTEGER DEFAULT 0,
                    	"sections"	text NOT NULL,
                    	"created_at"	datetime NOT NULL,
                    	"updated_at"	datetime NOT NULL,
                    	CONSTRAINT "class_unique" UNIQUE("term","subject","number")
                        );""")

            self._create_table("""CREATE TABLE students (
                        id integer NOT NULL CONSTRAINT students_pk PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL
                        );""")

            self._create_table("""CREATE TABLE students_classes (
                        id integer NOT NULL CONSTRAINT students_classes_pk PRIMARY KEY AUTOINCREMENT,
                        students_id integer NOT NULL,
                        classes_id integer NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL
                        );""")

            self._create_table("""CREATE TABLE requirements (
                        id integer NOT NULL CONSTRAINT requirements_pk PRIMARY KEY AUTOINCREMENT,
                        term integer NOT NULL,
                        major varchar(255) NOT NULL,
                        type varchar(255) NOT NULL,
                        data text NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL
                     );""")

            self._create_table("""CREATE TABLE "roadmap_toggles" (
                        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                        "requirements_id"	INTEGER,
                        "students_id"	INTEGER,
                        "highlight"	TEXT,
                        "created_at"	datetime,
                        "updated_at"	datetime
                    );""")

            rm = RequirementModel.RequirementModel(self.db)
            rm.setupTable()
