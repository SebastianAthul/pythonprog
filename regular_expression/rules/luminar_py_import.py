import re
f1=open('lumregno','r')
f2=open('regpy','w')
x='[L][U][M][P][Y][0-9]{3}$'
for num in f1:
    number=num.rstrip("\n")
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")

