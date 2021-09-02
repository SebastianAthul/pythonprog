
min=int(input("enter min"))
max=int(input("enter the max"))
for i in range(min,max+1):
    for j in range(0,i):
        print(min,end=" ")
    print()
for k in range(max,0,-1):
    for l in range(0,k):
        print(min+1,end=" ")
    print()