score = [82, 98, 100, 40, 75, 55, 73, 24, 10, 64]
number = 0
for i in score:
    number += 1 
    if i >= 90:
        print("{} student : A" .format(number))
    elif i >= 70:
        print("{} student : B" .format(number))
    elif i >= 50:
        print("{} student : C" .format(number))
    else:
        print("{} student : F" .format(number))
