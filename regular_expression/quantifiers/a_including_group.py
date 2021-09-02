import re
x='a+\d+b'
r='aaa a1234bc A32435Baaa cga'
matcher=re.finditer(x,r)
for match in matcher:
    print("starting=",match.start())
    print("Matching Group=",match.group())