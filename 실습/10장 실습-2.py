totalNum = 0 #합계를 위한 변수 초기화
NumList = [] #입력정수 리스트 초기화

while True: #무한반복
    num = int(input("Enter an integer (0: exit) : " ))
    if (num == 0) : 
        break #0입력이면 종료
    #else에 넣어도 되고 안넣어도 된다.
    NumList.append(num)
    totalNum += num

print("Integer list :", NumList)
print("Sum :", totalNum)
print("Average :", totalNum/len(NumList))

