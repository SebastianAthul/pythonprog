class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("Name=",self.name)
        print("AGE=",self.age)
        print("address=",self.address)
class Employee:
    def setvalue(self,job,salary):
        self.job=job
        self.salary=salary
        print("job=",self.job)
        print("salary=",self.salary)
class Parent(Person,Employee):
    def setval(self,loc,kids_count):
        self.loc=loc
        self.kids_count=kids_count
        print("location=",self.loc)
        print("kids_count=",self.kids_count)
obj=Parent()
obj.set('Athul',23,'kurisingal')
obj.setvalue('coder',20000)
obj.setval('kochi',3)