lst=[1,6,8,3,9,5,11,10]
def binarysearch():
    lst.sort()
    print(lst)
    ele=int(input("enter the element:"))
    low=0
    flag=0
    upper=len(lst)-1
    while low<=upper:
        mid=(low+upper)//2
        if ele > lst[mid]:
           low=mid+1
        elif ele<lst[mid]:
           upper=mid-1
        elif ele==mid:
           flag=1
           break
    if flag==1:
       print("found")
    else:
       print("not found")
binarysearch()