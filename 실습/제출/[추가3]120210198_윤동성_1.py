ints = list(input("two nums : ").split())
sets1 = set()
sets2 = set()
ints2 = []
if len(ints) != 2:
    print("Number of input data is not 2")
elif (ints[0].isdigit()==True) and (ints[1].isdigit()==True):
    
    int1 = int(ints[0])
    int2 = int(ints[1])
       
    for j in range(1, int1+1):
            if int1 % j == 0:
                sets1.add(j)  
    for j in range(1, int2+1):
            if int2 % j == 0:
                sets2.add(j)
     
    print("first num divisor : ",sets1)
    print("second num divisor : ",sets2)
    print("%d & %d common divisor : "%(int1, int2),sets1.intersection(sets2))
    if sets1.intersection(sets2) == set([1]) or len(sets1.intersection(sets2))==0 :
        print("Not exist greatest common divisor")
    else :
        ints2 = list(sets1.intersection(sets2))
        ints2.sort()
        print("%d & %d greatest common divisor : %d" %(int1, int2, ints2[-1]))

    


else: print("Input data is not integer or not positive integer")
