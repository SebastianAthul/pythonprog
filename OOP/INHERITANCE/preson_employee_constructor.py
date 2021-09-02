class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name=",self.name)
        print("age=",self.age)
class Employee(Person):
    def __init__(self,ID,salary,name,age):
        super().__init__(name,age)
        self.ID=ID
        self.salary=salary
    def print(self):
        print("ID=",self.ID)
        print("salary=",self.salary)
obj=Employee(123,2500,'Athul',23)
obj.printvalue()
obj.print()

