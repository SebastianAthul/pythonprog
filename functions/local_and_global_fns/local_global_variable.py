x=5  #global
def foo():
    x=3   #Local
    x+=10
    print("Local x=", x)
foo()
print("global x=",x)