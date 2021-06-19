fp_r = open("input.txt", 'r')
fp_w = open("120210198_out_time.txt", 'w')
nums = 0
for i in fp_r:
    nums = nums + 1
    num = list(int(x) for x in i.split())
    if num == []:
        break;
    num[1] = num[1] + num[2]
    while num[1] >= 60 :
        num[0] = num[0]+1
        num[1] = num[1]-60
        if num[1] < 60:
            break
    if num[0] >= 24:
        num[0] = num[0]-24

    if num[1] < 0:
        while num[1] <= -60:
            num[0] = num[0]-1
            num[1] = num[1]+60
            if num[1] > -60:
                break
        else:
            num[1] = 60+num[1]
            num[0] = num[0]-1

        if num[0] < 0:
            num[0] = num[0] + 24
    print("%d: time = %d:%d"%(nums, num[0],num[1]), file=fp_w)
    print("%d: time = %d:%d"%(nums, num[0],num[1]))
fp_r.close()
fp_w.close()
