R=int(input("input(9,999<,<100,000):"))
a = R//10000
b = (R-(a*10000))//1000
c = (R-(a*10000)-(b*1000))//100
d = (R-(a*10000)-(b*1000)-(c*100))//10
e = R%10

print("각 자리:",a,",",b,",",c,",",d,",",e)
print("average:",(a+b+c+d+e)//5)
