fruit = {'pear':[2, 1000], 'grape':[3, 2000], 'melon':[1, 8000],'apple':[6, 800]}

buy = input("What fruits do you want? : ")
if buy in fruit.keys():
    if fruit[buy][0] == 0:
        print("Sorry, {} is sold out" .format(buy))
    else:
        print("{}  thanks" .format(buy))
        fruit[buy][0] = fruit[buy][0]-1



else :
    print(" There is no",buy)



price = 0
print("")
print(" Each fruits have to be 5 in stock at least")
for a in fruit:
    if fruit[a][0] < 5:
        price += (5-fruit[a][0])*fruit[a][1]
    else :
        pass    
print(" Total price for buying : {}" .format(price))

