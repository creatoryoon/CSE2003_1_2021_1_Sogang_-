n1 = int(input("Enter a number to be checked:"))
cnt = 0
temp = 1
n2 = n1
n3 = 0
list1 = []

while n2  > 0:
    
    list1.append(n2%10)
    n2 = n2//10
list2 = list1.copy()
list2.reverse()


if list1 == list2:
    print("%d is a palindrome!" %n1)
else :
    print("%d is not a palindrome!" %n1)
