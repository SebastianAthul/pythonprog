class Animal:
    def __init__(self,breed,location):
        self.breed=breed
        self.location=location
    def printvalue(self):
        print("BREED=",self.breed)
        print("LOCATION=",self.location)
class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("Name=", self.name)
        print("AGE=", self.age)
obj=Dog('Loki',2)
obj.print()
obj2=Animal('Pitbull','Kochi')
obj2.printvalue()


