# 실습 14_1 
fp_in = open("L_In.txt",'r')
fp_out = open("L_Out.txt", 'w')
index = int(fp_in.readline())

A = list(int(x) for x in fp_in.readline().split())
B = list(int(x) for x in fp_in.readline().split())
fp_in.close()

sum = A[index] + B[index]
print("index = %d" %index, file = fp_out)
print("A =", A, file = fp_out)
print("B =", B, file = fp_out)
print("A[%d] + B[%d] =" %(index, index) , sum, file = fp_out)
fp_out.close()
