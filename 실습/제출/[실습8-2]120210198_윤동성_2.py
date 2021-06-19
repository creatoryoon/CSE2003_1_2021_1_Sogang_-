a = [(1, 2), (3, 4)]
b = [(2, 3), (4, 6)]

aa = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
bb = (b[0][0] * b[1][1]) - (b[0][1] * b[1][0])

print("Matrix A")
if aa != 0:
    ia = [(),()]
    ia[0] = (a[1][1]*(1/aa), a[0][1]*(-1/aa))
    ia[1] = (a[1][0]*(-1/aa), a[0][0]*(1/aa))
    print("inverse matrix of A = ", ia)
else:
    print("There's no inverse.")

print("Matrix B")
if bb != 0:
    ib = [(),()]
    ib[0] = (b[1][1]*(1/bb), b[0][1]*(-1/bb))
    ib[1] = (b[1][0]*(-1/bb), b[0][0]*(1/bb))
    print("inverse matrix of B = ", ib)

else:
    print("There's no inverse.")
