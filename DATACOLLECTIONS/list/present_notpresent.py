
a=[1,2,3,4,5,6,8,9,10,22]
def present(a):
    user=int(input("enter the element tocheck: "))
    for i in a:
      if i == user:
          print("present")
          break
    else:
       print("not present")
present(a)
