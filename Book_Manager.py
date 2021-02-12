import sys
from BookM import Book

# function to display menu to user
def Menu():
    print("Welcome to Book Organizer")
    print("Press 0 to Exit")
    print("Press 1 to Enter New Book")
    print("Press 2 to Search Existing Book")

# Function to add new book
def addNew():
    BName = ""
    book = Book()
    while True:
        print("Enter New Book Name or (q) to quit ")
        BName = str(input())
        if BName == "q":
            break
        else:
            print("Enter New Book Number")
            Bnum = int(input())
            book.newbook(BName, Bnum)

def exit():
    print("Exit")
    print(f"Hi you system is {sys.version} your max size is {sys.maxsize} and finally the platform is {sys.platform}")
    sys.exit()

def search():
    book = Book()
    while True:
        print("Enter Book Name or Press q To Quit")
        name = str(input())
        if name == "q":
            break
        else:
            book.searchName(name)

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
        else:
            print("Fuck U")

__init__()
