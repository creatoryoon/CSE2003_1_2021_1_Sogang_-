

import math





double_ = input("Enter height & radius:")
height, radius = double_.split()
height_f = float(height)
radius_f = float(radius)
height_f1 = "%.2f" % height_f
radius_f1 = "%.2f" % radius_f
surface_area = (2 * math.pi * radius_f * height_f) + (2 * math.pi * (radius_f ** 2))
answer = "%.4e" % surface_area
print("In height {} and radius {} , the area of cylinder is {}.".format(height_f1, radius_f1, answer))
print("the area is bigger than 10(>10)? ", end = '');print(surface_area >= 10)

