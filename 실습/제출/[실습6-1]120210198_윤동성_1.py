a, b, c = map(float, input("실수 세 개 입력").split())

median = 0

if (a>b) :
    if (b>c):
        median = b
    elif (c>a):
        median = a
    else:
        median = c
elif (a>c) :
    median = a
elif (c>b) :
    median = b
else:
    median = c



print("********************************************\n","중간 값 : %f" %median)
