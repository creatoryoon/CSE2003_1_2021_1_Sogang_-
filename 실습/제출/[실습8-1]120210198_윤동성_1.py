today = tuple(map(int,input("Enter the date(year, month, day) :").split()))

lm = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]


print("Today (month/day/year) : %02d/%02d/%04d" %(today[1], today[2], today[0]))
if (today[1], today[2]) in lm:
    if (today[1], today[2]) == lm[11] :
        print("Tomorrow (month/day/year) : %02d/%02d/%04d" %(1, 1, today[0]+1))
    else:
        print("Tomorrow (month/day/year) : %02d/%02d/%04d" %(today[1]+1, 1, today[0]))

else:
    print("Tomorrow (month/day/year) : %02d/%02d/%04d" %(today[1], today[2]+1, today[0]))
