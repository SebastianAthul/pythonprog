def primetotal(sum):
    return sum
sum=0
for i in range(1,50+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        sum=sum+i
print("sum of prime numbers is:",sum)

