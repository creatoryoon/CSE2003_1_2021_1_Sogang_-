major = {"computer" : [9,"R"], "math" : [2,"AS"], "elec" : [11,"R"], "psy":[1,"X"]}

a = input("Enter the major : ")


if a in major.keys():
    print("{} is floor {} in {}" .format(a, major.get(a)[0], major.get(a)[1]))
else:
    major[a] = [1, "GN"]
    print("{} has no data. The arrangement is floor {} in {} ." .format(a, major.get(a)[0], major.get(a)[1]))
print("\nsorting :",sorted(major.items()))
