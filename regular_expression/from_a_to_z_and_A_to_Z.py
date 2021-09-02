import re
x='[a-zA-Z]'
matcher=re.finditer(x,"aThuL777S3BAstIAN")
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())
