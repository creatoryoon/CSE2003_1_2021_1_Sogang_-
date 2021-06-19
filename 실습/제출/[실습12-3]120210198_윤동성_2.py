

def dup(list1, list2):
    list3 = set()
    temp = False
    for i in list1:
        for j in list2:
            if i == j :
                list3.add(i)
                temp = True
                
   
    list3 = list(list3)
    list3.sort()
    return list3, temp


list1 = list(map(int, input("enter list1 elements:").split()))
list2 = list(map(int, input("enter list2 elements:").split()))

list3, temp = dup(list1, list2)

if temp == True:
    print(list3,"overlapping elements")
else:
    print("No overlapping elements")
