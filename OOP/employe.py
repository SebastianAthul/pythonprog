class Employee:
    def setvalue(self,name,ID,salary,age,company,department):
        self.name=name
        self.ID=ID
        self.salary=salary
        self.age=age
        self.company=company
        self.department=department
    def printvalue(self):
        print("Name:",self.name)
        print("ID:",self.ID)
        print("Salary:",self.salary)
        print("Age:",self.age)
        print("Company:",self.company)
        print("Department:",self.department)
emp=Employee()
emp.setvalue("Athul",150021105204,25000,23,"luminar","software development")
emp.printvalue()

#Static method
class Employee:
    company='luminar'  #static defined
    def setvalue(self,name,ID,salary,age,department):
        self.name=name
        self.ID=ID
        self.salary=salary
        self.age=age
        self.department=department
    def printvalue(self):
        print("Name:",self.name)
        print("ID:",self.ID)
        print("Salary:",self.salary)
        print("Age:",self.age)
        print("Company:",Employee.company)
        print("Department:",self.department)
emp=Employee()
emp.setvalue("Athul",150021105204,25000,23,"software development")
emp.printvalue()