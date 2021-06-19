list1 = []
sum1 = 0
avg = 0
temp = 0
while True:
    i = int(input("Enter an integer(0: exit) : "))
    if i == 0:
        break
    list1.append(i)
    sum1 = sum1+i
    temp = temp + 1
    
print("Integer list : " ,list1)
print("sum : ", temp)
print("Average : ", sum1/temp)
