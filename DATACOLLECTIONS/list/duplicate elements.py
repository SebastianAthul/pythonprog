lst=[1,2,3,4,4,5,2,3]
duplicate=[]
for i in lst:
    if i not in duplicate:
        duplicate.append(i)
    else:
        print(i)
