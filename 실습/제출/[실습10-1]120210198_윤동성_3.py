from random import *
ct = randint(10, 20)
list1 = []
for i in range(ct):
    list1.append(randint(-10, 10))
print("random integer list : ", list1)
list2 = []
for i in range(1, 11):
    temp = 0
    for j in list1:
        if j == i:
            temp += 1
        else:
            pass
    list2.append(temp)
for i in range(1, 11):
    print("number %d : %d time(s)." %(i, list2[i-1]))
