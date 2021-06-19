score = list(int(x) for x in input("Enter the scores: ").split())
number = 0

for i in score: 
    number = number +1 
    if i >= 90: 
        print("%d student : A" % number)
    elif i >= 70: 
        print("%d student : B" % number)
    elif i >= 50: 
        print("%d student : C" % number)
    else: 
        print("%d student : F" % number)

