class Employee:
    def __init__(self,name,age,job,salary):
        self.name=name
        self.age=age
        self.job=job
        self.salary=salary
    def printvalue(self):
        print("name=",self.name)
        print("age=",self.age)
        print("job=",self.job)
        print("salar=",self.salary)
obj=Employee("Athul",23,"developer",25000)
obj.printvalue()