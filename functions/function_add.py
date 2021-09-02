# #fn without arg
def add():
    num1=int(input("ener number"))
    num2=int(input("ener number"))
    sum=num1+num2
    print(sum)
add()

#  f wiht arg

def add(num1,num2):
     print(num1+num2)
add(12,22)
add(23,2)

# fn with arg and return type

def add(num1,num2):
    return num1+num2
print(add(1,2))
