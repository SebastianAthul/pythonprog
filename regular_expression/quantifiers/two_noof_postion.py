import re
x='a{2}'
r='aaa abc aaaa cga' #groups only where there is 2 a's/2 no:of position
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())