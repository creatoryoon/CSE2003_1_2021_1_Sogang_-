A = list(map(int, input("Enter list A numbers : ").split()))
B = list(map(int, input("Enter list B numbers : ").split()))
C = []
for i in A:
    if i not in C:
        C.append(i)
for i in B:
    if i not in C:
        C.append(i)
for i in A:
    for j in B:
        if i==j:
            if j in C:
                C.remove(j)
C.sort()
print(C)

        
       

