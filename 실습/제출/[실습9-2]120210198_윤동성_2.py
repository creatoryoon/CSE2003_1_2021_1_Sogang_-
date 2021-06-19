n1, n2 = map(int, input("Enter N1, N2(0 < N1 <= N2) : ").split())
n3 = 0
for i in range(n1, n2+1):
    if (i % 2) == 0 :
        n3 = n3 + i
    else :
        continue






print("Sum of even numbers between %d and %d is %d." %(n1, n2, n3))
