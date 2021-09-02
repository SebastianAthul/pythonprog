import re
n=input("Enter a string:")
x='^a[0-9]+b$'
match =re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")