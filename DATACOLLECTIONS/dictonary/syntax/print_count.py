count={}
data=input("enter:")
words=data.split(" ")
print(words)
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        value=int(count[word])
        value+=1
        count.update({word:value})
print(count)