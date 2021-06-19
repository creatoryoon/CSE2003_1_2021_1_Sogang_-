n = int(input("Enter N (0 < N < 10) : "))
if n > 0 and n < 10:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    if n%2 == 0 :
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end="")        
            print()
    else:
        for i in range(n-1, 0, -1):
            for j in range(1, i+1):
                print(j, end="")
            print()

else:
    print("ERROR: N must be 0 < N < 10")
