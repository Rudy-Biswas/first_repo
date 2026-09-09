x1 = float(input("Enter the x-coordinate of point A: "))
y1 = float(input("Enter the y-coordinate of point A: "))
x2 = float(input("Enter the x-coordinate of point B: "))
y2 = float(input("Enter the y-coordinate of point B: "))

import math

D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance between the 2 points is: ",D)