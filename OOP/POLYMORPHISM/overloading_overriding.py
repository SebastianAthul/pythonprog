# #overloading works acc to no of values
# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
# obj=Student()
# obj.show(3,6)
#
# class Op:
#     def sum(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
#     def sum(self,n3):
#         self.n3=n3
#         print(self.n3)
# k=Op
# k.sum(4,5)

#overriding
class Person:
    def print(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def print(self,class1): #child class method overrides parent class method,
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.print('Athul')