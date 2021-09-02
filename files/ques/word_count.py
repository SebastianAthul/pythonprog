count={}
f=open('fil','r')
for n in f:
    wr=n.split(" ")
    for word in wr:
        if word not in count:
            count.update({word:1})
        else:
            value=int(count[word])
            value+=1
            count.update({word.value})
print(count)