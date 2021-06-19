import math

height, radius = input("Enter height & radius:").split()
height = float(height)
radius = float(radius)

area = (2 * math.pi * radius * height) + (2 * math.pi * (radius**2))


print("In height {:.2f} and radius {:.2f} , the area of cylinder is {:.4e}." .format(height, radius, area))
print("the area is bigger than 10(>10)?", end=" ")
print(area > 10)

