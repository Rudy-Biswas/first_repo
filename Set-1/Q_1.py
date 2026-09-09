n = int(input("Days of selling goods: "))

sales_list = []
for i in range (n):
    x = int(input("Enter the sales value: "))
    sales_list.append(x)

print("The Total sales: ", sum(sales_list))

print("The Average sales: ", sum(sales_list)/n)

print("The Maximum sale was: ", max(sales_list))

print("The Minimum sale was: ", min(sales_list))
    



