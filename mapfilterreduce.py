employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
# MAP()
#print names  (Map case)
for employee in employees:
    print(employee["e_name"])
#Map Function
e_names=list(map(lambda employee:employee["e_name"],employees))
print("employee names:",e_names)

#print names in upper
for employee in employees:
    print(employee["e_name"].upper())
#map function
e_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
print("Upper=",e_upper)


  #FILTER()
#print names working as employee(Condition)(filter)
for employee in employees:
    if(employee["department"]=="developer"):
        print("developers=", (employee["e_name"]))

#Filter function
developers=list(filter(lambda employee:employee["department"]=="developer",employees))
print("developers=",developers)


#REDUCE()
#salary total sum(reduce)
total=0
for employee in employees:
    total+=employee["salary"]
print("total=",total)

salarys=list(map(lambda employee:employee["salary"],employees))
print("salary=",sum(salarys))



#print names whose name start with 'a'(fileter case)
#print lowest salary)reduce
#salary increment(map)
#add bonus of 5000 for devel(filter)

