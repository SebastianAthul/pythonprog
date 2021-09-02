a=int(input("enter the  start range: "))
b=int(input("enter the  end range: "))
r=5
for i in range(a,b):
    if (i%2==0):
        print(i)
        for k in range (r,0,-1):
            for j in range (0,k):
                print(i,end=" ")
            print("\r")
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(l,end=" ")
            print("\r")
