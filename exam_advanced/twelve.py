# # __str__ used in classes to represent the objects as a string.
# eg:
class Student:
    def __init__(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
    def printvalue(self):
        print("Name=",self.name)
        print("Rollno=",self.rollno)
        print("Department=",self.dep)
    def __str__(self):
        return self.name +self.dep

obj=Student("Athul",23,'Science')
obj.printvalue()
print(obj)