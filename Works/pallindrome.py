user=input("ENter the word : ")
buser=user[::-1]
if user==buser:
    print("pallindrome", buser)
else:
    print("not pallindrome", buser)
