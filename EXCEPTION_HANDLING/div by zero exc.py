a=int(input("enter a number"))
b=int(input("enter another number"))
try:
    result=a/b
    print("result=",result)
except Exception as e:
    print(e.args)