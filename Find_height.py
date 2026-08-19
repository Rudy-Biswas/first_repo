#A person standing at a distance d from the base of a vertical tower looks up at the top with an angle of elevation theta (in degrees). Write a program to calculate the height of the tower h.
import math

theta = int(input("Enter the angle of elevation(in degrees): "))
d = float(input("Distance from the base(in metres): "))


print("The Height of the tower is: ", math.tan(math.radians(theta))*d)
