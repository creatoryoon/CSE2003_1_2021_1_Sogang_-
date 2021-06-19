n1 = int(input("Enter an integer : "))

 
temp = 0 
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 
n2 = 0
n3 = 0


while ( n1 > len(prime)):
    n2 = prime[-1]+1
    for i in prime:
        if (n2%i == 0):
            n3 = 1
            n2 = n2+1 
    if n3 == 1 :
        continue
    else:
        prime.append(n2)

          

print(prime)





while (temp != n1):
    print(prime[temp])
    temp += 1     

    
    
print("Find  %d prime number!" %n1)
