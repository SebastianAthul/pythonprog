import re
n='hello'
x='[a-z]+' #or '\w' 
match =re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
