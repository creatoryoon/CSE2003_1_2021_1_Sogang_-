""" 입력 받은 횟수까지의 동전 앞면 발생 비율
1-10 : 매 횟수마다, 11-100 : 10 단위마다, 101 - 1000 : 100 단위마다
동전의 앞면 발생 비율 출력"""
import random

def cointhro(n):
    Front = 0 #앞면의 횟수
    for i in range(1, n+1):
        ForB = random.randint(0,1)
        if ForB == 0:    # 동전 앞면 0, 뒷면 1
            Front += 1
        if i < 10:
            print("Front side of %3d : %3d%%" %(i, int(Front/i*100)))
        elif i < 100 and i % 10 == 0:
            print("Front side of %3d : %3d%%" %(i, int(Front/i*100)))

    return Front

n = int(input("Enter the number(1 - 100) : "))
if n < 1 or n > 100 :
    print("Only enter the integer between 1 and 100")
else:
    TotalF = cointhro(n)
    print()
    print("***********************************************")
    print("Front side of the whole try (%d) : %3d%%" %(n, int(TotalF/n*100)))


