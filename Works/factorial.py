num=int(input("enter a number="))
if num>0:
    fact=1
    for i in range (1,num+1):
      fact=fact*i
    print(fact)
elif num==0:
    print("fact of zero is 1")
else:
    print("no Fact")


# #while loop
# num=int(input("enter a number="))
# fact=1
# i=1
# while i<=num:
#     fact=fact*i
#     i=i+1
# print(fact)