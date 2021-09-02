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
c.set("athul",23,"kurisingal")
c.setval(5.9,65)
c.setvalue("Developer",25000)
