import sys
from sqlite import DB

def Menu():
    print("Welcome to Book Organizer")
    print("Press 0 to Exit")
    print("Press 1 to Enter New Book")
    print("Press 2 to Search Existing Book")
    print("Press 3 to display Existing Book")
    print("Press 4 to edit Existing Book")


def addNew():
    BName = ""
    while True:
        print("Enter New Book Name or (q) to quit ")
        BName = str(input())
        if BName == "q":
            break
        else:
            print("Enter New Book Number")
            Bnum = int(input())
            print("Enter Placement Of Book")
            Bplace = str(input())
            print("Enter Author Name")
            Bauth = str(input())
            print("Enter Publish Date")
            Bpub = str(input())

            db.addBook(Bnum, BName, Bauth, Bplace, Bpub)

def exit():
    print("Exit")
    print(f"Hi you system is {sys.version} your max size is {sys.maxsize} and finally the platform is {sys.platform}")
    sys.exit()

def search():
    while True:
        print("Enter Book Name/ID/Author or Press q To Quit")
        usr = str(input())
        if usr == "q":
            break
        else:
            db.search(usr)

def displayElements():
    db.printTable()

def edit():
    while True:
        print("Enter Book ID or Press 0 To Quit")
        usr = int(input())
        if usr == 0:
            break
        else:
            print("Enter Updated Book Name")
            Bname = str(input())
            print("Enter Updated Author Name")
            Bauth = str(input())
            db.Update(usr, Bname, Bauth)


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
        elif option == 4:
            edit()
            Menu()
            option = int(input())
        else:
            print("Option Invalid")
            break
db = DB()
db.open()
try:
    db.createTable()
except:
    print("createTable exeption")
__init__()
