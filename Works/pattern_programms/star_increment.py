# for i in range(12):   #rows
#     for j in range(0,i):    #star
#         print("*",end=" ")
#     print()   #nextrowil pokaan


# for i in range(12,0 ,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()

#1
#2 3
#4 5 6
#7 8 9 10
# def pattern(n):
#     count=1
#     for i in range(n):
#         for j in range(0,i):
#             print(count,end=" ")
#             count=count+1
#         print()
# pattern(5)

# 1
# 12
# 123
# 1234
# 12345
# def pattern(n):
#     for i in range(n):
#         count=1
#         for j in range(i):
#             print(count,end=" ")
#             count+=1
#         print()
# pattern(5)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*",end=" ")
#         print()
# pattern(6)

    #     *
    #    *  *
    #   *  *  *
    # *  *  *  *
# def pattern(n):
#     space=n-1
#     for i in range(n):
#         for j in range(0,space):
#             print(end=" ")
#         space=space-1
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print()
# pattern(7)

  #
  # * * * * *
  #  * * * * *
  #   * * * * *
  #    * * * * *
  #     * * * * *

def pattern(n):
   k=n
   for i in range(0,n):
       for r in range(0,k):
           print(end=" ")
       k=k+1
       for j in range(0,n):
          print("*", end=" ")
       print()
pattern(6)