
def delete(list1):
    print("The input list:",list1)
    a = input("Enter word to remove: ")
    temp = 0
    if a not in list1:
        print("%s is not in the input words." %a)
        return list1
    else:
        while a in list1:
            list1.remove(a)
            temp = temp + 1
        print("the number of the word in input list :",temp)
        print("Updated list is : ",list1)    
        return list1


list1 = list(input("Please enter your words :").split())

list1 = delete(list1)

