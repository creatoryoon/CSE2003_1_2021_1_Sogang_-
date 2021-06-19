flag = True


def strfind(strs):
    if len(strs) == 0:

        global flag
        flag = False
    
      
    big = 0
    small = 0
    for i in strs:
        if i.islower() == True:
            small = small + 1
        if i.isupper() == True:
            big = big + 1
    return big, small







n1, n2 = strfind(input("문자열 입력 : "))
if flag == True:
    print("소문자 개수 : %d, 대문자 개수 : %d" %(n2, n1))
else: print("입력 데이터가 없습니다")
