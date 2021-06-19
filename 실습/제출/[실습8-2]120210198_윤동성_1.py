
st = list(sorted(set(input("Enter sentence:\n").lower().split())))
if st == []:
    print("No sentence")
else:


    print("Non duplicate words (list):",st)
    a = input("Enter one character for string : ")
    print("Non duplicate words (string) : ",a.join(st))


