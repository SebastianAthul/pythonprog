class Parent:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def print(self):
        print("name=",self.name)
        print("address=",self.address)
class Teacher(Parent):
    def __init__(self,id,dep,name,address):
        super().__init__(name,address)
        self.id=id
        self.dep=dep
    def printval(self):
        print("ID=",self.id)
        print("dep=",self.dep)
        print("Name=",self.name)
        print("address=",self.address)
    def __str__(self):
        return self.name+str(self.id)
obj=Teacher(123,'science','athul','kurisingal')
print(obj)
obj.printval()
