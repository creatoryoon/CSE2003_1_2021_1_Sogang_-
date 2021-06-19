sample = "abcABCdEFaBCDeFAbC"

tsample = sample.lower()
f1 = "abc"
f2 = "def"
tf1 = f1.lower()
tf2 = f2.lower()


indexf1 = tsample.find(tf1)
countf1 = tsample.count(tf1)
indexf2 = tsample.find(tf2)
countf2 = tsample.count(tf2)


print("index of %s : %d, %d times" %(f1, indexf1, countf1))
print("index of %s : %d, %d times" %(f2, indexf2, countf2))
