from functools import reduce
lst=[1,2,3,4]
#total
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
#largest
largest=reduce(lambda num1,num2:num1  if num1>num2 else  num2,lst)
print(largest)