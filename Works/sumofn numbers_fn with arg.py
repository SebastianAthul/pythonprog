def sum(n):
    s=0
    for i in range (n+1):
        s=s+i
    print(s)
sum(9)

#using return

def sum(n):
    s=0
    for i in range (n+1):
        s=s+i
    return s
print(sum(4))

# while True:
#     print("HELLO")