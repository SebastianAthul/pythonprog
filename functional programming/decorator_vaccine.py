def vaccination(func):
    def wrapper(a,b):
        if b<18:
            raise Exception("not eligible for vaccination")
        else:
            return func(a,b)
    return wrapper
@vaccination
def details(name,age):
    return name+" age "+str(age)+" you are eligible for vaccination"
print(details('Athul',18))