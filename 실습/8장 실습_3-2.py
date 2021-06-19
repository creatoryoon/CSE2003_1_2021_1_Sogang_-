fruit = {'pear' : [2, 1000], 'grape' : [3, 2000], 'melon' : [1, 8000], 'apple' : [6, 800]}

want = input("What fruits do you want? : ")
#먹고싶은 과일이 있는 경우
if (want in fruit) :
    if fruit[want][0] > 0:
        print(want, " thanks")
        fruit[want][0] -= 1
else :
    print(" There is no ",want)

print()
print(" Each fruits have to be 5 in stock at least")

#과일당 5개를 채우기 위해서는 얼마가 필요한지 계산
price = 0
if (fruit["pear"][0] < 5 ):
    price += (5 - fruit["pear"][0]) * fruit["pear"][1] #모자란 수량 * 단가
if (fruit["grape"][0] < 5 ):
    price += (5 - fruit["grape"][0]) * fruit["grape"][1]
if (fruit["melon"][0] < 5 ):
    price += (5 - fruit["melon"][0]) * fruit["melon"][1]
if (fruit["apple"][0] < 5 ):
    price += (5 - fruit["apple"][0]) * fruit["apple"][1]

print(" Total price for buying :", price)


