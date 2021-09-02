import re
n=input("Enter a string:")
x='[A-Z]+\w{3,8}[A-Z]$'
match =re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")