import math
bottle = []

def vol():
    
    pi = math.pi
    bottle.append(bottle[1]*pi*(bottle[0]**2))
    bottle.append((bottle[2]/bottle[3])*100)
    bottle[3] = round(bottle[3], 2)
    bottle[4] = round(bottle[4], 2)
    if bottle[4] > 100:
        bottle.append("overflow")
    else:
        bottle.append("")
    return bottle




bottle = list(map(float, input("Enter height & radius: ").split()))
vol()
print("volume of bucket :%.2f" %bottle[3])
print("percentage of water : %.2f%% %s" %(bottle[4], bottle[5]))
