fp_r = open("in.txt", 'r')
s = fp_r.readlines()
index = int(s[0])


line1 = list(map(int, s[1].split()))
line2 = list(map(int, s[2].split()))
fp_r.close()

print("index =",index)
print("A =",line1)
print("B =",line2)

print("A[%d] + B[%d] = %d" %(index, index, line1[index]+line2[index]))


