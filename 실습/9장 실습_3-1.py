N = int(input("Enter N (0 < N < 10) : "))
#error 출력
if N >= 10 or N <= 0 :
    print("ERROR: N must be 0 < N < 10.")
else :
    for i in range(1, N+1) :
        for j in range(1, i+1) :
            print(j, end="")
        print()
    Lines = N
    if N % 2 == 1 :
        Lines = N - 1
    for i in range(Lines, 0, -1) :
       for j in range(1, i + 1) :
           print(j, end="")
       print()

