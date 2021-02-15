import sys
from sqlite import DB

def Menu():
    print("Welcome to Book Organizer")
    print("Press 0 to Exit")
    print("Press 1 to Enter New Book")
    print("Press 2 to Search Existing Book")
    print("Press 3 to display Existing Book")

def addNew():
    BName = ""
    # book = Book()
    while True:
        print("Enter New Book Name or (q) to quit ")
        BName = str(input())
        if BName == "q":
            break
        else:
            print("Enter New Book Number")
            Bnum = int(input())
            print("Enter Author Name")
            Bauth = str(input())
            book.newbook(BName, Bnum)
            db.addBook(Bnum, BName, Bauth)

def exit():
    print("Exit")
    # print(f"Hi you system is {sys.version} your max size is {sys.maxsize} and finally the platform is {sys.platform}")
    sys.exit()

def search():
    book = Book()
    while True:
        print("Enter Book Name/ID or Press q To Quit")
        usr = str(input())
        if usr == "q":
            break
        else:
            book.search(usr)

def displayElements():
    # file = open("books.txt")
    # lines = file.readlines()
    # for line in lines:
    #     print(line)
    # file.close()
    db.printTable()


def __init__():
    Menu()
    option = int(input())

    while option != 0:

        if option == 0:
            exit()
        elif option == 1:
            addNew()
            Menu()
            option = int(input())
        elif option == 2:
            search()
            Menu()
            option = int(input())
        elif option == 3:
            displayElements()
            Menu()
            option = int(input())
        else:
            print("Option Invalid")
            break
db = DB()
db.open()
__init__()
