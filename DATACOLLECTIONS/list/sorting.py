a=[1,2,5,3,6,4,9,8]
new=[]
while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    new.append(min)
    a.remove(min)
print(a)
print(new)
