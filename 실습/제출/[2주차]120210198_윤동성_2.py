a=20
b=2.1
c="sogang"
print("a=",a, "b=",b,"c",c)
a, b, c = 1.9, 10.1, 2.1 # a=1.9, b=10.1, c="2.1"
print("a=",a, "b=",b,"c",c)
tmp = a
a = b
b = tmp
print("a=",a,"b=",b,)
a = int(a)
b = b+c
print("a=",a,"b+c=",b)