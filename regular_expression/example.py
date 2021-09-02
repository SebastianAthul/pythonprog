# import re
# count=0
# matcher=re.finditer('ab','ababbabab')
# for match in matcher:
#     count+=1
# print("count=",count)

import re
count=0
matcher=re.finditer('ab','ababbabab')
for match in matcher:
    print("match availavble at=",match.start()) #return position
    print("group=",match.group())  #returns which ob find match
    count+=1
print("count=",count)