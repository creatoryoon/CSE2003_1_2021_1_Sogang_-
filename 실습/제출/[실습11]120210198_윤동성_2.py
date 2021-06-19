from random import *
j = 0

fp_w = open("in_num.txt", 'w')
for j in range(2):
    line = fp_w.read
    for i in range(10):
        j = random()+2
        j = round(j, 2)
        fp_w.write(str(j)+" ")
    fp_w.write('\n')
fp_w.close()

fp_w= open("_out_num.txt", 'w')
fp_r = open("in_num.txt", 'r')
for k in fp_r:
    num = list(float(x) for x in k.split())
    for i in range(len(num)):
        sq = num[i]*num[i]
        sq = int(sq)
        print("%d " %sq, end='')
        print("%d " %sq, file = fp_w, end='')
    fp_w.write('\n')
    print('')
fp_r.close()
fp_w.close()
