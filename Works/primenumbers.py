num=int(input("ENTER A NUMBER"))
if num>1:
    for i in range (2,num):
        if num%i==0:
          print("NUMBER IS NOT PRIME")
          break
    else:
      print("number is prime")
else:
    print("not a prime number")


