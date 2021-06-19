import random
L=[]
num=random.randint(10,20)

for x in range (num) :
    x= random.randint(-10,10)
    L.append(x)
print("random integer list:",L)
L=[int(x) for x in L]
n=1
while n<=10 :
    if n in L :
        z=0
        for x in range(len(L)):
            if L[x]==n :
                z=z+1
    else:
        z=0
    print("number {} : {} time(s).".format(n,z))
    n=n+1
