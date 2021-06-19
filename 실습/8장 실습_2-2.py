a = [(1,2),(3,4)]
b = [(2,3),(4,6)]

print("Matrix A")
if (a[0][0]*a[1][1]-a[0][1]*a[1][0])==0:
    print("There's no inverse.")
else :
    new_a = 1/(a[0][0]*a[1][1]-a[0][1]*a[1][0])*a[1][1]
    new_b =-1/(a[0][0]*a[1][1]-a[0][1]*a[1][0])*a[0][1]
    new_c =-1/(a[0][0]*a[1][1]-a[0][1]*a[1][0])*a[1][0]
    new_d = 1/(a[0][0]*a[1][1]-a[0][1]*a[1][0])*a[0][0]
    inv_a = [(new_a,new_b),(new_c, new_d)]
    print("inverse matrix of A = ", inv_a)

print("Matrix B")
if (b[0][0]*b[1][1]-b[0][1]*b[1][0])==0:
    print("There's no inverse.")
else :
    new_a = 1/(b[0][0]*b[1][1]-b[0][1]*b[1][0])*b[1][1]
    new_b =-1/(b[0][0]*b[1][1]-b[0][1]*b[1][0])*b[0][1]
    new_c =-1/(b[0][0]*b[1][1]-b[0][1]*b[1][0])*b[1][0]
    new_d = 1/(b[0][0]*b[1][1]-b[0][1]*b[1][0])*b[0][0]
    inv_b = [(new_a,new_b),(new_c, new_d)]
    print("inverse matrix of B", inv_b)
