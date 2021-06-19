today = tuple(map(int, input("Enter the date(year, month, day) :").split()))

print("Today(month/day/year) : %02d/%02d/%04d" % (today[1],today[2],today[0]))
year, month, day = today

end_of_month = (today[1], today[2]) in [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]

end_of_year = month == 12 and day == 31
if end_of_month:
    if end_of_year:
        year += 1
        month = 1
        day = 1
    else:
        month += 1
        day = 1
else:
    day += 1
tomorrow = year, month, day
print("Tomorrow(month/day/year) : %02d/%02d/%04d" % (tomorrow[1], tomorrow[2], tomorrow[0]))


