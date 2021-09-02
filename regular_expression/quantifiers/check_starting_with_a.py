import re
x='^a'
r='aaa abc aaaa cga' #starting with a only
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())