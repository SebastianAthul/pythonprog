class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name=",self.name)
        print("age=",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)#calling the attributes from parent class using super().
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("rollno=",self.rollno)
        print("mark=",self.mark)
st=Student(4,23,'athul',23)
st.printvalue()
st.print()

