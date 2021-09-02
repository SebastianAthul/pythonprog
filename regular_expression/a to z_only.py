import re
x='[a-z]'
matcher=re.finditer(x,"aThuL SeBAstIAN")
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())
