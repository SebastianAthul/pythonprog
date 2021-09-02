import re
x='[^a-zA-Z0-9]'
matcher=re.finditer(x,"aTh@#uL69S3^*BAstIAN@")
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())
