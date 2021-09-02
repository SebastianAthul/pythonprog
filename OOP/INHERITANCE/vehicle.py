class Vehicle:
    def __init__(self,model,regno,color):
       self.model=model
       self.regno=regno
       self.color=color
    def print(self):
        print("Model=",self.model)
        print("regno=",self.regno)
        print("color=",self.color)
    def __str__(self):
        return self.model #2string,single value,must assign + for adding next attrbute
obj=Vehicle('Honda','KL43M3966','Red')
obj.print()
print(obj)