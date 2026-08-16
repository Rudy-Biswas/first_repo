a = int(input("Sales of Day 1: "))
b = int(input("Sales of Day 2: "))
c = int(input("Sales of Day 3: "))
d = int(input("Sales of Day 4: "))
e = int(input("Sales of Day 5: "))
f = int(input("Sales of Day 6: "))
g = int(input("Sales of Day 7: "))

sales=[]
sales.append(a)
sales.append(b)
sales.append(c)
sales.append(d)
sales.append(e)
sales.append(f)
sales.append(g)

print("Sales of last 3 days: ", sales[4]+sales[5]+sales[6])
print("Sales of whole week: ", sales[0]+sales[1]+sales[2]+sales[3]+sales[4]+sales[5]+sales[6])
print("Sales of last 2 days - Previous 2 days: ", (sales[5]+sales[6]) - (sales[3]+sales[4]))

