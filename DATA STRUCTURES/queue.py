que=[]
size=int(input("enter the size "))
front=0
top=0
n=0
def enqueue():
    global front,size,top
    if top>size:
        print("queue is full")
    else:
        p= int(input("enter the elemenets:"))
        que.append(p)
        top+=1
def dequeue():
    if top<=0:
        print("empty")
    else:
        que.pop(0)
        front=-1
def display():
    print(que)
while n!=1:
    print("Enter the options")
    opt=int(input("1.enqueue 2. dequeue 3 DISPLAY"))
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    elif opt==3:
        display()
