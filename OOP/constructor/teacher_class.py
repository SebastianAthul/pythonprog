class Teacher:
    college = 'luminar'
    def __init__(self, name, sub, dep):
        self.name=name
        self.sub=sub
        self.dep=dep
    def printvalue(self):
        print("name=",self.name)
        print("sub=",self.sub)
        print("department=",self.dep)
        print("college=",Teacher.college)
obj=Teacher('Shifna','python','coding')
obj.printvalue()