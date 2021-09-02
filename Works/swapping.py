#assignment method
a=1
b=2
a,b=b,a
print("a=", a, "b=", b)

#Temp storage method
a=1
b=2
t=a  #1
a=b  #2
b=t   #1
print(a,b)

#3rd method
a,b=1,2
a=a+b #3
b=a-b  #3-1 #2
a=a-b #3-2 #1
print(a,b)

