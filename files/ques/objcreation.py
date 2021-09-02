class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("name=",self.name)
        print("age=",self.age)
    def __str__(self):
        return self.name
f1=open('athul','r')
for i in f1:
    line=i.split(",")
    name=line[0]
    age=line[1]
    obj=Person(name,age)
    print(obj)
    obj.print()