my_string=input("ENTER THE STRING : ")
check=""
for i in my_string:

   if i not in check:
    check=check+i
   else:
       print(i)
       break