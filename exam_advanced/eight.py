#finally block is excecuted always even if there is an exception.
lst=[1,2,3]
index=int(input("enter the index:"))
try:
    print(lst[index])
except:
    print("index not exist")
finally:
    print("hello")