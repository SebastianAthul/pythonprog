no1=int(input("Enter first number: "))
no2=int(input("Enter first number: "))
no3=int(input("Enter first number: "))
if (no1>no2) and (no2>no3):
    print("No1 is greater")
elif no2>no1>no3:
    print("no2 is greater")
elif no1==no2==no3:
    print("Equal")
else:
    print("No3 is greater")

