def calcPlus(v1, v2) :
    return v1 + v2

def calcMul(v1, v2) :
    return v1 * v2

def calcDiv(v1, v2) :
    return v1 / v2

def calcMinus(v1, v2) :
    return v1 - v2


num1, op, num2 = input("Enter the operation (Ex: 20 * 40) : ").split()
num1 = float(num1)
num2 = float(num2)

if  op == "+" :
    print("%f %s %f = %f "%(num1, op, num2, calcPlus(num1, num2)))
elif  op == "*" :
    print("%f %s %f = %f "%(num1, op, num2, calcMul(num1, num2)))
elif  op == "/" :
    if num2 == 0 :
        print("%f cannot divide"%(num2))
    else:
        print("%f %s %f = %f "%(num1, op, num2, calcDiv(num1, num2)))
elif  op == "-" :
    print("%f %s %f = %f "%(num1, op, num2, calcMinus(num1, num2)))
else:
    print(op, "is not supported.")
