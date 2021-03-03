import sqlite3

class DB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(DB)
            return cls.__instance
        return cls.__instance

    def __init__(self, db_name='datab'):
        self.name = db_name
        # connect takes url, dbname, user-id, password
        self.con = self.connect()
        self.c = self.con.cursor()

    def connect(self):
        try:
            return sqlite3.connect(self.name, check_same_thread=False)
        except sqlite3.Error as e:
            pass

    def __del__(self):
        self.c.close()
        self.con.close()
        print("Connection to sql CLOSED")

    def createTable(self):
      self.c.execute('''CREATE TABLE IF NOT EXISTS FlaskBooks
         (id INT PRIMARY KEY    NOT NULL,
         name           TEXT    NOT NULL,
         place          TEXT    NOT NULL,
         authname       TEXT    NOT NULL,
         publish        TEXT    NOT NULL);''')

    def addBook(self, id, name, place, authname, publish):
        print("Saving book")
        try:
            self.c.execute("INSERT INTO FlaskBooks (id,name,place,authname,publish) VALUES (?, ?, ?, ? ,?)", (id, name, place, authname, publish))
            self.con.commit()
            msg = "Record successfully added"
        except Exception as e:
            self.con.rollback()
            msg = "Error in insert operation"
            print(e)
        return msg


    def printTable(self):
        cursor = self.c.execute("SELECT * from FlaskBooks")
        for row in cursor:
            print("id = ", row[0])
            print("name = ", row[1])
            print("place = ", row[2])
            print("authname = ", row[3])
            print("publish = ", row[4])
            print(row,"\n")

    def search(self,x):
        self.con.row_factory = sqlite3.Row
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM FlaskBooks WHERE id LIKE '%{x}%' OR name LIKE '%{x}%' OR place LIKE '%{x}%' OR authname LIKE '%{x}%' OR publish LIKE '%{x}%';")
        rows = cur.fetchall();
        for row in rows:
            print("id = ", row[0])
            print("name = ", row[1])
            print("place = ", row[2])
            print("authname = ", row[3])
            print("publish = ", row[4])
            print(row,"\n")
        return rows

    def Update(self, name, place, authname, publish):
        try:
            cursor = self.c.execute("UPDATE FlaskBooks SET (name,place,authname,publish) VALUES (?, ?, ? ,?)", ( name, place, authname, publish))
        except:
            print("An error occured during this Opration")

    def getRows(self):
        self.con.row_factory = sqlite3.Row
        cur = self.con.cursor()
        cur.execute("select * from FlaskBooks")
        rows = cur.fetchall();
        return rows
