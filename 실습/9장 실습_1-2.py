#리스트만큼 반복
score = [82, 98, 100, 40, 75, 55, 73, 24, 10, 64]
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
