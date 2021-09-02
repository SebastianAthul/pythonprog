import re
x='[0-9]'
matcher=re.finditer(x,"aThuL69S3BAstIAN")
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())
