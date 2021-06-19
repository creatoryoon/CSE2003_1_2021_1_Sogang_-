import math
#입력받은 수를 리스트로 저장
data = list(float(x) for x in input("Enter data : \n").split()) # data input
                     # \n is newline
N = len(data)    # N = data size
M2 = E2 = 0      # initialize
for d in data :
    M2 += d * d  # accumulate d square
    E2 += d      # accumulate d
M2 = M2/N        # average of sum(d^2 in data)
E2 = (E2/N)**2   # square of average
std_dev = math.sqrt(M2 - E2)
print("Standard deviation = %.5f" %std_dev)


