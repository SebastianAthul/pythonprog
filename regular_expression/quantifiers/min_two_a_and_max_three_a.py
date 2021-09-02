import re
x='a{2,3}'
r='aa abc aaaa cga' #min 2 a and max upto 3 a
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())