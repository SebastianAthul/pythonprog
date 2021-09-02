import re
n='56kg'
x='[0-9]{2}[k][g]'
match =re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
