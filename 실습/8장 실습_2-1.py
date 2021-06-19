
input_ = input('Enter sentence:\n')

if input_ == '':
    print('No sentence')
else:
    input_ = input_.lower()
    input_list = list(set(input_.split()))
    print('Non duplicate words (list): ', sorted(input_list))
    connection = input('Enter one character for string : ')
    print('Non duplicate words (string) : ', connection.join(sorted(input_list)))






