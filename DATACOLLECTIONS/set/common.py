s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9,10,11}
common=set()
for i in s1: #iterating elements in s1
        if i in s2: #checking if elements in s1 is in s2
            common.add(i) #assinging the common element in common set
print(common)