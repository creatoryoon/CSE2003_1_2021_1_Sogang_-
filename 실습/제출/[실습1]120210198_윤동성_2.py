wallet = 5000
grape = 120
orange = 150
apple = 180
strawberry = 20


grapecount = 6
orangecount = 7
applecount = 10
strawberrycount = 17

totalgrape = grape*grapecount
totalorange = orange*orangecount
totalapple = apple*applecount
totalstrawberry = strawberry*strawberrycount

totalall = totalgrape+totalorange+totalapple+totalstrawberry
change = wallet - totalall



print("My wallet :",wallet)
print("grape:",grape,",amount:",grapecount)
print("orange:",orange,",amount:",orangecount)
print("apple:",apple,",amount:",applecount)
print("strawberry:",strawberry,",amount:",strawberrycount)
print("total:",totalall,",change:",change)
