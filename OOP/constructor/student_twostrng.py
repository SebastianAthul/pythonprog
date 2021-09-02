class Student:
    college="ss college"
    def __init__(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
    def printvalue(self):
        print("Name=",self.name)
        print("Rollno=",self.rollno)
        print("Department=",self.dep)
        print("College=",Student.college)
    def __str__(self):
        return self.name +self.dep+str(self.rollno) #converts integer to string

obj=Student("Athul",23,'Science')
obj.printvalue()
print(obj)