def revert_val(func): #div(2,10)
    def wrapper(no1,no2):
        if no1<no2: #since condition is true
            (no1,no2)=(no2,no1) # swapping happens
            return func(no1,no2) #returns div(10,2)
        else:
            return func(no1,no2)
    return wrapper
@revert_val #calling the decorator
def div(num1,num2):
    return num1/num2
print(div(2,10))

   #SUBSTRACTION
@revert_val #calling the decorator
def sub(num1,num2):
    return num1-num2
print(sub(2,10))