class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("Name=",self.name)
        print("AGE=",self.age)
class Child(Person):
    def setvalue(self,school,std):
        self.school=school
        self.std=std
        print("school=",self.school)
        print("std=",self.std)
class Parent(Person):
    def setval(self,loc,kids_count):
        self.loc=loc
        self.kids_count=kids_count
        print("location=",self.loc)
        print("kids_count=",self.kids_count)
class Student(Child):
    def value(self,uniform,division):
        self.uniform=uniform
        self.division=division
        print("uniform=",self.uniform)
        print("Division=",self.division)
