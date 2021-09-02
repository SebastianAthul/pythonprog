def admin_req(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("Operation not allowed")
        else:
            return func(a,b)
    return wrapper
@admin_req
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_req
def acc_delete(user,accno):
    return str(accno)+"deleted"
print(change_pin("admin",1000))
print(acc_delete("user",1000))