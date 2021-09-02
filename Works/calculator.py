def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
print("SELECT AN OPERATION")
print("1. ADDITION")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
while True:
    choice=int(input("enter your choice"))

    x=float(input("Enter number"))
    y=float(input("Enter number"))
    if choice==1:
          print(add(x,y))
    elif choice==2:
          print(sub(x,y))
    elif choice == 3:
          print(mult(x,y))
    elif choice == 4:
          print(div(x,y))
    else:
          print("INVALID CHOICE")
