# pair=6
# lst=[2,3,4,5]
# for i in lst:
#     for j in lst:
#         if(i!=j):
#             if((i+j)==pair):
#                 print(i,j)
# lst=[2,3,4,5]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if (lst[i]+lst[j]==6):
#             print(lst[i],lst[j])
#
lst=[1,2,3,4,5]
low=0
upp=len(lst)-1
pair=6
pairs=[]
while(low<upp): #0<4
    sum=lst[low]+lst[upp] #1+5
    if(sum==pair): #1+5==6
        pairs.append((lst[low],lst[upp]))
        low+=1
    elif(sum>pair):
        upp-=1
    elif(sum<pair):
        low+=1
print(pairs)
