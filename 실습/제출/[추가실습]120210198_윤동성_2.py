import math
x1, y1, x2, y2 = map(float, input("Enter x1, y1, x2, y2 : ").split())
dist = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2)  )


print("distance between x and y : %.2f" %dist)
print("the distance is under 5? : ", (dist < 5))
