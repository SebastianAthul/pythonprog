# def printval(* args):  #many values can be given if *args is used
#     return(args)
# print(printval(1,2,3,4,5,6)) #output type is TUPLE
#
def printval(** args): #double star is used for assigning variables to values
    return(args)
print(printval(name='Athul',age=24,place="kochi")) #op type is Dictonary


