import math as mt

L = [int(x) for x in input("Enter data :\n").split()]


m2 = 0
e2 = 0

for d in L:
    m2 += d**2
    e2 += d
m2 = m2/len(L)
e2 = (e2/len(L))**2
stdDev = mt.sqrt(m2 - e2)
print("Standard deviation = %.5f" %stdDev)
