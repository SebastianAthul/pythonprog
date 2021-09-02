lst=[2,3,4,5]
def check_even(num):
    return num %2==0

evens=list(filter(lambda num:num%2==0,lst))
print("even=",evens)
odd_numbers=list(filter(lambda num:num%2!=0,lst))
print("odds=",odd_numbers)