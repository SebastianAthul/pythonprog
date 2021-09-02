stack=[]
size=int(input("Enter the size:"))
top=0
n=0
def push():
    global top,size
    if(top>size):
        print("stack is full")
    else:
        p=int(input("enter the elemenets:"))
        stack.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print("empty")
    else:
        stack.pop()
        top-=1
def display():
    print(stack)
while n!=1:
    print("Enter the options")
    opt=int(input("1.PUSH 2. POP 3 DISPLAY"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        display()


