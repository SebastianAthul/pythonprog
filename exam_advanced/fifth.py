class Book:
    def print(self,name):
        self.name=name
        print("Book Name=",self.name)
class Category(Book):
    def print(self,theme):
        self.theme=theme
        print("Theme=",self.theme)
obj=Category()
obj.print('Fiction')
