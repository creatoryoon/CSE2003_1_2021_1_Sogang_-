input1_ = input('Enter the first string:')
input2_ = input('Enter the second string:') 
input_1 = list(input1_)
input_2 = list(input2_)

if (sorted(input_1) == sorted(input_2)) and (len(input_1) == len(input_2)):
    print(input1_, ',', input2_, 'is anagram.')
    
else:
    print(input1_, ',', input2_, 'is not anagram.')






