import calendar

def yearcount(year):
    
    if (year%4 == 0 and year%100!=0 or year%400 == 0):
        print("%d는 윤년입니다."%year)
    else:
        print("%d는 윤년이 아닙니다."%year)
    


def daycount():
    global day
    global month
    global year
    total=0
    data1, data2 =  calendar.monthrange(year,month)
    date = ((data1 + day)-1 ) % 7  
    if date == 0:
        print("%s년 %s월%s일은 월요일입니다."%(year,month,day));
    elif date == 1:
        print("%s년 %s월%s일은 화요일입니다."%(year,month,day));
    elif date == 2:
        print("%s년 %s월%s일은 수요일입니다."%(year,month,day));
    elif date == 3:
        print("%s년 %s월%s일은 목요일입니다."%(year,month,day));
    elif date == 4:
        print("%s년 %s월%s일은 금요일입니다."%(year,month,day));
    elif date == 5:
        print("%s년 %s월%s일은 토요일입니다."%(year,month,day));
    else:
        print("%s년 %s월%s일은 일요일입니다."%(year,month,day));


year, month, day = input("날짜를 입력하세요: ").split()
year=int(year)
month=int(month)
day=int(day)
yearcount(year)
daycount()
print (calendar.month(year, month))

#테스트할 때 1987과 1988, 1989를 대입해 보세요. 1988은 윤년입니다.
