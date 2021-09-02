def factorial(num):
    fact=1
    if num>0:
        for i in range(1,num+1):
            fact=fact*i
        print(fact)
    elif num==0:
        print('fact of zero is 1')
    else:
        print("no negative factorial")
factorial(-8)


