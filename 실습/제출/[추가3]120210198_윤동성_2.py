import calendar
days = ["월","화","수","목","금","토","일"]
y, m, d = map(int, input("날짜를 입력하세요 : ").split())


def isyear(y):
    if y%4 == 0:

        if y%400 == 0:
            print("%d는 윤년입니다." %y)
        elif y%100 == 0:
            print("%d는 윤년이 아닙니다." %y)
        else:
            print("%d는 윤년입니다." %y)
    else: print("%d는 윤년이 아닙니다." %y)
def isday():
    global y, m, d
    a, b = calendar.monthrange(y, m)
    dd = d+a-1
    dd = dd%7
    print("%d년 %d월 %d일은 %s요일입니다." %(y, m, d, days[dd]))

if m in range(1,13):
    if d in calendar.monthrange(y, m):

        isyear(y)

        isday()  

        print(calendar.month(y,m,w=0,l=0)    )
    else:print("잘못된 날짜입니다.")
else: print("잘못된 월입니다.")
