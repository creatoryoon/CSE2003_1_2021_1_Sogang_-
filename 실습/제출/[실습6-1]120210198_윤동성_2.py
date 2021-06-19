import math

a, b, c = map(float, input("Enter a, b ,c : ").split())
d = (b**2)-(4*a*c)
if (d > 0) :
    d = math.sqrt(d)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)
    print("root1 = {:.4f}. and root2 = {:.4f}." .format(root1, root2))
elif (d == 0):
    root = (-1 * b) / (2 * a)
    print("single root = %.4f." %root)
else :
    print("no root exists.")

