m = input("Enter the month: ")



if m.isdigit() != True :
    print("Wrong input")
elif int(m) > 12 or int(m) == 0:
    print("Wrong input")


else :
    m = int(m)
    print("***** 1st version(if) *****")
    if m == 1:
        print("%dst month is January" %m)
    elif m == 2:
        print("%dnd month is Feruary" %m)
    elif m == 3:
        print("%drd month is March" %m)
    elif m == 4:
        print("%dth month is April" %m)
    elif m == 5:
        print("%dth month is May" %m)
    elif m == 6:
        print("%dth month is June" %m)
    elif m == 7:
        print("%dth month is July" %m)
    elif m == 8:
        print("%dth month is August" %m)
    elif m == 9:
        print("%dth month is September" %m)
    elif m == 10:
        print("%dth month is October" %m)
    elif m == 11:
        print("%dth month is Novemver" %m)
    else:
        print("%dnd month is December" %m)
    
    print("***** 2nd version(list) *****")   
    mlist = ["st month is January", "nd month is Feruary", "rd month is March", "th month is April", "th month is May", "th month is June", "th month is July", "th month is August", "th month is September", "th month is October", "th month is November", "th month is December"]
    print("%d"%m + mlist[m-1])



    
