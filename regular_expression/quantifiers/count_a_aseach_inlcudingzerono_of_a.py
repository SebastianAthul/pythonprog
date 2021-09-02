import re
x='a?'
r='aaa abc aaaa cga' #each postion considered rather than group including a and no a
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())