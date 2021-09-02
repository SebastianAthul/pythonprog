def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)  #6*5*4*3*2*1
num=int(input("Enter a number :"))
print("Factorial is :", factorial(num))