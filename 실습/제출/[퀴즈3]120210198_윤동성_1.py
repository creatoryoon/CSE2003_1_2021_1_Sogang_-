sum = 0


while (sum <= 21):
    n = int(input(""))
    sum = sum + n
    if n == 0 :
        print("Total sum is less than 21 and is equal to %d ." %sum)
        break
else:
    print("Total sum is %d" %sum)


