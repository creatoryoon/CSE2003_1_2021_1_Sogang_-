L = [12, 29, 30, 0, 99]

t1 =  input("Enter the data for L:")

if (t1.isnumeric()):
    t1 = int(t1)
    if ( t1 != L[0] and t1 != L[1] and t1 != L[2] and t1 != L[3] and t1 != L[4] ):
        L[5:5] = [t1]
        print(L)
    else :
        print("Input is already in L.")
        print(L)
else :
    print("Input can be only bigger integer  than 0.")
    print(L)



