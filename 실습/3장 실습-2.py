from math import *

R=int(input("input(9,999<,<100,000):"))
k=R
a=R//10000; R%=10000
b=R//1000; R%=1000
c=R//100; R%=100
d=R//10 ; e=R%10

print(k, "각 자리:",a , ",", b, ",", c, ",", d, ",",e)

print("average:",trunc((a+b+c+d+e)/5))
