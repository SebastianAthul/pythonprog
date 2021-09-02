class Student:
    def setvalue(self,name,rollno,clas,age,school):
        self.name=name
        self.rollno=rollno
        self.clas=clas
        self.age=age
        self.school=school
    def printvalue(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("class:",self.clas)
        print("Age:",self.age)
        print("school:",self.school)

st=Student()
st.setvalue("Athul",18,10,16,"sgvhss")
st.printvalue()

#instance and static variable
class Student:
    school='sgvhss'  #STATIC Variable related to class, avvessed using class name
    def setvalue(self,name,rollno,clas,age):
        self.name=name
        self.rollno=rollno   #INSTANCE Variable are related to methods,accessed using self
        self.clas=clas
        self.age=age
    def printvalue(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("class:",self.clas)
        print("Age:",self.age)
        print("school:",Student.school)

st=Student()
st.setvalue("Athul",18,10,16)
st.printvalue()