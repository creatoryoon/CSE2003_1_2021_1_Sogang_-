

first_num, ope, second_num = input('Enter the operation : ').split()
first_num_f = float(first_num)
second_num_f = float(second_num)

if ope == '+':
    result = first_num_f + second_num_f
    print('%.2f' % first_num_f, ope, '%.2f' % second_num_f, '= %.2f' % result) 
    
elif ope == '-':
    result = first_num_f - second_num_f
    print('%.2f' % first_num_f, ope, '%.2f' % second_num_f, '= %.2f' % result) 
    
elif ope == '*':
    result = first_num_f * second_num_f
    print('%.2f' % first_num_f, ope, '%.2f' % second_num_f, '= %.2f' % result) 
    
elif ope == '/':
    if second_num_f == float(0):
        print('\'0\' cannot divide other number.')
    else:
        result = first_num_f / second_num_f
        print('%.2f' % first_num_f, ope, '%.2f' % second_num_f, '= %.2f' % result)
    
else:
    print(ope, 'is not supported.')





