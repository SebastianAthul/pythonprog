import re
x='a$'
r='aaa abc aaaa cga' #ending with a
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())