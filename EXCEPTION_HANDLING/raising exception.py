age=int(input("enter your age: "))
if age<18:
    raise Exception("not eligible for vaccination")
else:
    print("eligible")
