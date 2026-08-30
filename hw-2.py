x1 = float(input("Enter the X coordinate of point A: "))
y1 = float(input("Enter the X coordinate of point B: "))
x2 = float(input("Enter the Y coordinate of point A: "))
y2 = float(input("Enter the Y coordinate of point B: "))

import math

m = (y2 - y1)/(x2 - x1)

theta = math.atan(m)

print("The angle between the line and positive x-axis is: ", math.degrees(theta))


