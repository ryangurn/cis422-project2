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

    def __init__(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            self.conn = conn
            return
        except Error as e:
            print(e)

        self.conn = conn
        return


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
        if self.conn is not None:

            self._create_table("""CREATE TABLE classes (
                        id integer NOT NULL CONSTRAINT classes_pk PRIMARY KEY AUTOINCREMENT,
                        crn integer NOT NULL,
                        term integer NOT NULL,
                        type varchar(100),
                        seats text NOT NULL,
                        sections text NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL,
                        CONSTRAINT class_unique UNIQUE (crn, term)
                    );""")

            self._create_table("""CREATE TABLE students (
                        id integer NOT NULL CONSTRAINT students_pk PRIMARY KEY AUTOINCREMENT,
                        duckID integer NOT NULL,
                        first_name varchar(255) NOT NULL,
                        last_name varchar(255) NOT NULL,
                        majors text NOT NULL,
                        minors text NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL
                        );""")

            self._create_table("""CREATE TABLE students_classes (
                        id integer NOT NULL CONSTRAINT students_classes_pk PRIMARY KEY AUTOINCREMENT,
                        students_id integer NOT NULL,
                        classes_id integer NOT NULL,
                        created_at datetime NOT NULL,
                        updated_at datetime NOT NULL,
                        CONSTRAINT students_classes_students FOREIGN KEY (students_id)
                        REFERENCES students (id),
                        CONSTRAINT students_classes_classes FOREIGN KEY (classes_id)
                        REFERENCES classes (id)
                        );""")
