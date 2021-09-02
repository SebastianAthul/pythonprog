class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def print(self):
        print("name=",self.name)
        print("Rollno=",self.rollno)
        print("Course=",self.course)
        print("Marks=",self.mark)
    def __str__(self):
        return self.course
f1=open('student','r')
for i in f1:
    line=i.split(",")
    name=line[0]
    rollno=line[1]
    course=line[2]
    mark=line[3]
    obj=Student(name,rollno,course,mark)
    print(obj)
    obj.print()