class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvaluee(self):
        print("Name=",self.name)
        print("age=",self.age)
obj=Person("Athul",23)
obj.printvaluee()
