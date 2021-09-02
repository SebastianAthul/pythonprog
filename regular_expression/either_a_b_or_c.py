import re
x='[abc]'
matcher=re.finditer(x,"athul sebastian kurisingall house")
for match in matcher:
    print("starting=",match.start())
    print("Group=",match.group())
