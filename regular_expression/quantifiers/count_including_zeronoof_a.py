import re
x='a*' #will consider postion if there is no a
r='aaa abc aaaa cga'
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())