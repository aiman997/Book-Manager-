import sqlite3

class DB:
    file = "test.db"
    c = None
    con = None

    def open(self):
      conn = sqlite3.connect(self.file)
      print("Opened database successfully")
      self.c = conn.cursor()
      self.con = conn
    def close(self):
        self.c.close()
        print("Connection to sql CLOSED")

    def createTable(self):
      self.c.execute('''CREATE TABLE Books
         (ID INT PRIMARY KEY    NOT NULL,
         NAME           TEXT    NOT NULL,
         AUTHOR         TEXT    NOT NULL);''')
      print("Table created successfully")

    def addBook(self, id, name, author):
         self.c.execute(f"INSERT INTO Books (ID,NAME,AUTHOR) VALUES ('{id}', '{name}', '{author}')")
         self.con.commit()

    def printTable(self):
        cursor = self.c.execute("SELECT * from Books")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("AUTHOR = ", row[2])
            print(row,"\n")

    def search(self,x):
        cursor = self.c.execute(f"SELECT * FROM Books WHERE NAME = '{x}' OR ID = '{x}' OR AUTHOR = '{x}';")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("AUTHOR = ", row[2])

    def Update(self, id, updName, updAuthor ):
        try:
            cursor = self.c.execute(f"UPDATE Books SET NAME = '{updName}', AUTHOR = '{updAuthor}' WHERE ID = '{id}';")
        except:
            print("An error occured during this Opration")
