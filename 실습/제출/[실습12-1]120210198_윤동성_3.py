def operation(in1):
    ft1, ft2, ft3 = in1.split()
    ft1 = float(ft1)
    ft3 = float(ft3)
    result = 0
    flag = 0

    if ft2 == "+":
        result = ft1 + ft3
    elif ft2 == "-":
        result = ft1 - ft3
    elif ft2 == "*":
        result = ft1 * ft3
    elif ft2 == "/":
        if ft3 == 0:
            flag = 1
            result = str(ft3) + " cannot divide"
        else:
            result = ft1 / ft3
    else:
        flag = 1
        result = ft2 + " is not supported."
    return flag, ft1, ft2, ft3, result

flag, ft1, ft2, ft3, result = operation(input("Enter the operation (Ex 20 * 40) : "))
if flag == 0:
    print(ft1,ft2,ft3,"=",result)
else:
    print(result)

