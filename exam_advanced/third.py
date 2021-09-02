class Book:
    def setvalue(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print("LIBRARY Name=", self.library_name)
        print("BOOK NAME=",self.book_name)
        print("AUTHOR=",self.author)
        print("PAGeS=",self.pages)
obj=Book()
obj.setvalue("Brilliance","The Theory Of Everything",'Stephen Hawkings',123)
obj.print()