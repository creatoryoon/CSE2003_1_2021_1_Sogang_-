from math import *

x1, y1, x2, y2 = input("Enter x1, y1, x2, y2 : ").split()

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)

distance= sqrt((x2-x1)**2+(y2-y1)**2)
print("distance between x and y: %.2f" % distance)
print("the distance is under 5? :", distance < 5)		

