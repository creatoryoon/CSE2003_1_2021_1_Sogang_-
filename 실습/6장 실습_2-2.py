num1, num2, num3 = input('Enter the triangle : ').split()
int1, int2, int3 = int(num1), int(num2), int(num3)
if (((int1 + int2) <= int3) or ((int1 + int3) <= int2) or ((int2 + int3) <= int1)):
    if int1 <= 0 or int2 <=0 or int3 <=0:
        print('There is the negative number(>0)!!')
        
    else:
        print('It is not trialgle.')
    
elif int1 == int2 == int3:
    print('Regular triangle')
    
elif ((int1 == int2) or (int2 == int3) or (int3 == int1)):
    print('Isosceles triangle')
    
elif (int1 ** 2 + int2 ** 2 == int3 ** 2) or (int1 ** 2 + int3 ** 2 == int2 ** 2) or (int2 ** 2 + int3 ** 2 == int1 ** 2):
    print('Right-angled triangle')
    
else:
    print('Normal triangle')
    





