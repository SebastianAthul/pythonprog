# out=[]
# lst=[2,4,6] #[10,8,6]
# print(lst)
# total=sum(lst)
# print("total=",total)
# for num in lst:
#     out.append(total-num)
# print(out)
#
# out=[]
# lst=[3,5,7] #[12,10,8]
# print(lst)
# total=sum(lst)
# print("total=",total)
# for num in lst:
#     out.append(total-num)
# print(out)
#
# #lst comprehension
# lst=[2,4,6]
# total=sum(lst)
# op=[total-num for num in lst]
# print(op)

#map
lst=[2,4,6]
total=sum(lst)
print(list(map(lambda num:total-num,lst)))
