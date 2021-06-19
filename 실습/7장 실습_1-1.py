input_ = input('Enter the data for L:')
L = [12, 29, 30, 0, 99]

if (input_.isnumeric() == False) or ((input_.isnumeric == True) and int(input_) < 0):
    print('Input can be only bigger integer  than 0.')
    print(L)

elif L.count(int(input_)) == 1:
    print('Input is already in L.')
    print(L)
    
else:
    L[len(L):len(L)] = [int(input_)]
    print(L)



