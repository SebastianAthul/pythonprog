#MULTIPLE INHERITANCE
class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("Name=",self.name)
        print("AGE=",self.age)
class Child:
    def setvalue(self,school,std):
        self.school=school
        self.std=std
        print("school=",self.school)
        print("std=",self.std)
class Student(Person,Child): #multiple inheritance, inheriting proprty of both Person and child classes
    def printvalue(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        print("Roll=",self.rollno)
        print("marks=",self.marks)
obj=Student()
obj.set("ATHUL",23,"kurisingal")
obj.setvalue("LUMINAR",12)
obj.printvalue(18,45)

