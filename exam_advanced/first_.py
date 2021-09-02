class Vehicle:
    def setvalue(self,model,regno,color):
       self.model=model
       self.regno=regno
       self.color=color
       print("Model=",self.model)
       print("regno=",self.regno)
       print("color=",self.color)
class Bus(Vehicle):
    def set(self,transmission,cylinder):
        self.transmission=transmission
        self.cylinder=cylinder
        print("trasnmission=",self.transmission)
        print("cylinder=",self.cylinder)
obj=Bus()
obj.setvalue('bus','KL43M3966','red')
obj.set('6speed','single')

