# lst={'name': 'Athul', 'age': 24, 'college': 'ss college', 'location': 'kochi'}
# user=input("enter the key to check: ")
# for i in lst:
#     if i==user:
#         print("present")
#         break
# else:
#     print("not")

# method 2
d={1:2,4:5,7:9}
def present(x):
    if x in d:
        print("present")
    else:
        print("not present")
x=int(input("enter key :"))
present(x)

