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
        print("salary=",self.salary)
        print("job=",self.job)

obj=Employee()
obj.set("Athul",23,'kurisingal')
obj.setvalue('python',25000)


