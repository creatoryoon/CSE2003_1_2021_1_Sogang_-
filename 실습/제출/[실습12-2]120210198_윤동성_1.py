import random

def coin(j):
    
    cosum = 0
    for k in range(1, j+1):
        cosum += random.randint(0, 1)
        if k <=10:
            print("Front side of \t %d : \t %d%%" %(k, ((k-cosum)/k)*100))        
        elif ((k % 10) == 0) and (k < j):
            print("Front side of \t %d : \t %d%%" %(k, ((k-cosum)/k)*100))


    cosum = j - cosum    
    

    return cosum

j = input("Enter the number(1 - 100) : ")
if j.isdigit() == False:
    print("wrong input, plz input only int(range(1-100)")
else : 
    j = int(j)
    if j > 100:
        print("wrong input, plz input under 100")
    else:
        l = coin(int(j))
        print("Front side of \t %d : \t %d%%" %(j, (l/j)*100))
    
    
