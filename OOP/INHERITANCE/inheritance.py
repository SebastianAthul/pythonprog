#single INheritance
class Person: #BASE/PARENT/SUPER Class
    def walk(self,):
        print("walking")
    def read(self):
        print("reading")
class Student(Person): #DERRIVED/SUB/CHILD class
    def exam(self):
        print("exam")
obj=Person()
obj.walk()
obj.read()
#
# obj1=Student()
# obj1.exam()
# obj1.walk()
# obj1.read()
#
#
# #multiple
#
# class A:
#     def printA(self):
#         print("inside A")
# class B(A):
#     def printB(self):
#         print("inside B")
# class C(B):
#     def printC(self):
#         print("inside C")
# a=A()
# a.printA()
#
# b=B()
# b.printB()
# b.printA()
#
# c=C()
# c.printC()
# c.printB()
# c.printA()
  #eg
class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("Name=",self.name)
        print("AGE=",self.age)
        print("address=",self.address)
class Employee(Person):
    def setvalue(self,job,salary):
        self.job=job
        self.salary=salary
        print("job=",self.job)
        print("salary=",self.salary)
class child(Employee):
    def setval(self,height,weight):
        self.height=height
        self.weight=weight
        print("height=",self.height)
        print("weight=",self.weight)


c=child()
c.setval(2.5,25)
c.setvalue("coder",25000)
c.set("athul",23,"kurisingal")