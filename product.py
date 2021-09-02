products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]
#print all product name
product_name=list(map(lambda item:item["p_name"],products))
print("product name=",product_name)
#available products
avail_product=list(filter(lambda item:item["avl_qty"]>0,products))
print("available product=",avail_product)
#out of stck
stock=list(filter(lambda item:item["avl_qty"]==0,products))
print("outofstock=",stock)
#costly product
costly=list(map(lambda product:product["mrp"],products))
print(max(costly))
# from functools import reduce
# costly=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
# print("max price=",costly)
#print min
low_cost=list(map(lambda product:product["mrp"],products))
print(min(low_cost))