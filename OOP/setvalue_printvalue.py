class Person:
    def setvalue(self,name,age):
        self.name=name    #instance variables
        self.age=age
    def printvalue(self):
        print("name is :",self.name)
        print("age is :", self.age)
pe=Person()
pe.setvalue("ATHUL",23)
pe.printvalue()
