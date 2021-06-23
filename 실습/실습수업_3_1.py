input_ = input('two nums : ')

if len(input_.split()) != 2:
    print('Number of input data is not 2')
    
else:
    num1, num2 = input_.split()
    if num1.isdigit() == False or num2.isdigit() == False:
        print('Input data is not integer or not positive integer')
        
        
    else:
        num1, num2 = int(num1), int(num2)
        num1_s = set()
        num2_s = set()
        
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                num1_s.add(i)
        
        for j in range(1, num2 + 1):
            if num2 % j == 0:
                num2_s.add(j)
        
        print('first num divisor :', num1_s)
        print('second num divisor :', num2_s)
        print('{} & {} common divisor : {}'.format(num1, num2, num1_s.intersection(num2_s)) )
        if (num1 == 0 or num2 == 0):
            print('Not exist greatest common divisor')
        
        else:
            print('{} & {} greatest common divisor : {}'.format(num1, num2, max(num1_s.intersection(num2_s))))
        







