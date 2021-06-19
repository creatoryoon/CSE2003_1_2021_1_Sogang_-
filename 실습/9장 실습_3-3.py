A = [int(x) for x in input("Enter list A numbers : ").split()]
B = [int(x) for x in input("Enter list B numbers : ").split()]
C=[]
if len(A)==len(B):
    for i in range(len(A)):
        if A[i] not in B and A[i] not in C:
            C.append(A[i])
        if B[i] not in A and B[i] not in C:
            C.append(B[i])
elif len(A)<len(B):
    for i in range(len(A)):
        if A[i] not in B and A[i] not in C:
           C.append(A[i])
        if B[i] not in A and B[i] not in C:
           C.append(B[i])
    for j in range(len(A),len(B)):
        if B[i] not in A and B[i] not in C:
           C.append(B[i])
else:
    for i in range(len(B)):
        if A[i] not in B and A[i] not in C:
           C.append(A[i])
        if B[i] not in A and B[i] not in C:
           C.append(B[i])
    for j in range(len(B),len(A)):
        if A[i] not in B and A[i] not in C:
           C.append(A[i])
C.sort()
print(C)
