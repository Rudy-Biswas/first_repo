import math

choice = int(input("1:Square, 2:Rectangle, 3:Triangle "))

#square:
a = int(input("Enter the length of a side of SQUARE: "))

#rectangle:
l = int(input("Enter the length of the RECTANGLE: "))
b = int(input("Enter the breadth of the RECTANGLE: "))

#triangle:
p = int(input("Enter the first side of the triangle: "))
q = int(input("Enter the second side of the triangle: "))
r = int(input("Enter the third side of the triangle: "))

s = (p+q+r)/2
A = math.sqrt((s*(s-p)*(s-q)*(s-r)))