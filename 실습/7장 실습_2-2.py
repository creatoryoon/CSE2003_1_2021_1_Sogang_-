month= input("Enter the month: ")
check=['1','2','3','4','5','6','7','8','9','10','11','12']
if month not in check:
    print("Wrong input.")
else: 
    month = int(month)
    print("***** 1st version(if) *****")
    if month==1: name="January"
    elif month==2: name="February"
    elif month==3: name="March"
    elif month==4: name="April"
    elif month==5: name="May"
    elif month==6: name="June"
    elif month==7: name="July"
    elif month==8: name="August"
    elif month==9: name="September"
    elif month==10: name="October"
    elif month==11: name="November"
    elif month==12: name="December"

    if month==1:
        print("{}st month is {}.".format(month,name))
    elif month==2:
        print("{}nd month is {}.".format(month,name))
    elif month==3:
        print("{}rd month is {}.".format(month,name))
    else:
        print("{}th month is {}.".format(month,name))

    print("***** 2nd version(list) *****")
    year=["January","February","March","April","May","June",
       "July","August","September","October","November","December"]
    if month==1:
        print("{}st month is {}.".format(month,year[month-1]))
    elif month==2:
        print("{}nd month is {}.".format(month,year[month-1]))
    elif month==3:
        print("{}rd month is {}.".format(month,year[month-1]))
    else:
        print("{}th month is {}.".format(month,year[month-1]))

