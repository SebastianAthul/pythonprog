import re
n=input("Enter a string:")
x='[a-zA-Z]+\d$' #or \w+\d$
match =re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")