N1, N2 = input("Enter N1, N2(0 < N1 <= N2) : ").split()
S = N1 = int(N1)
E = N2 = int(N2)

if N1%2 == 1 :
    S = S + 1
if N2%2 == 0 :
    E = E + 1
Sum = 0
for x in range(S,E,2) :  #begin과 end-1이 짝수여야 한다.
    Sum += x
print("Sum of even numbers between %d and %d is %d." %(N1,N2,Sum))
