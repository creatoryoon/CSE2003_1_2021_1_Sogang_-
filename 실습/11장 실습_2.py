import random

fp_t = open('in_num.txt', 'w')
for i in range(10):
    i = random.random() + 2
    print('%.2f' % i, file = fp_t, end = ' ')
 
fp_t.write('\n')

for i in range(10):
    i = random.random() + 2
    print('%.2f' % i, file = fp_t, end = ' ')

fp_t.close()

fp_r = open('in_num.txt', 'r')
fp_w = open('out_num.txt', 'w')

for s in fp_r:
    num = list(float(x) for x in s.split())
    
    for i in range(len(num)):
        sq = num[i] * num[i]
        print('%3d' % sq, file = fp_w, end = ' ')
        
    fp_w.write('\n')
    
fp_r.close();fp_w.close()


