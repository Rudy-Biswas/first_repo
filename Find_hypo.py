import math

y = float(input("Enter the height of the outpost: "))
x = float(input("Enter the firing range: "))

z = math.sqrt(x**2 - y**2)

print("The Horizontal Distance till which firing can occur: ", z)


