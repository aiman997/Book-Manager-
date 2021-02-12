import mmap

class Book:
    __Name = ""
    __ID = None
    filename = None


    def setfile(self, filename):
        self.filename = filename
        file = open(self.filename, "a")
        print(f"Succesfully opened file: {self.filename} Test complete")
        file.close()

    def __init__(self):
        self.filename = ""
        self.__Name = ""
        self.__ID = None
        self.setfile("books.txt")

    def newbook(self, name, id):
        self.__Name = name
        self.__ID = id
        file = open(self.filename, "a")
        filestr = str(self.__Name) + " " + str(self.__ID) + "\n"
        f = file.write(filestr)
        file.close()

    def searchName(self, name):
        # file = open(self.filename, "a")
        # for line in file:
        #     print(line)
        # file.close()
        with open('books.txt') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(str.encode(name)) != -1:
                print('true')
                print(f"s: {s}")
              # print("book name" "book ID")
            else:
                print("This Book Does Not Exist")

    def searchID(self, id):
        file = open(self.filename, "a")
        for line in file:
            print(line)
        file.close()
