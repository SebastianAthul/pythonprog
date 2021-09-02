import re
x='\d'
matcher=re.finditer(x,"aTh@#uL 69 S3^*BAstIAN@")
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())
