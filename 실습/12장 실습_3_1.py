def wd_remove(L):
    rWord = input("Enter word to remove: ")
    chk=0
    for i in range(len(L)-1,-1, -1):
        if rWord == L[i]:
            del L[i]
            chk=chk+1
    
    if chk == 0:
        print(rWord, "is not in the input words.")
        return chk
    else:
        return chk

input_string = input("Please enter your words :").split()

print("The input list:", input_string)
occ=wd_remove(input_string)
if occ != 0:
    print("the number of the word in input list :", occ)
    print("Updated list is: ", input_string)

