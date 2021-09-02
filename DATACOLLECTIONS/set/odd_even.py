set1={1,2,3,4,5,6,7,8,9,10}
even=set()
odd=set()
print(set1)
for i in set1:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("even set =", even, "\n""odd set  =", odd)


