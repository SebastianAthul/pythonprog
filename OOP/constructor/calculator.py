# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def printvalue(self):
#         print("addition=",self.num1+self.num2)
#         print("subs=",self.num1-self.num2)
#         print("mult=",self.num1*self.num2)
#         if self.num2!=0:
#             print("div=",self.num1/self.num2)
#         else:
#             print("Div=Zero div not possible")
# obj=Calculator(num1=int(input("enter number")),num2=int(input("enter num")))
# obj.printvalue()
#
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
a=int(input("Enter number:"))
b=int(input("enter number: "))
obj=calc(a,b)
print("addition=",obj.add())
print("sub=",obj.sub())
print("mult=",obj.mult())
print("div=",obj.div())