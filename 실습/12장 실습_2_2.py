import math

def cal():
    global h
    global r
    global vol
    b_vol = math.pi*r*r*h
    w_per = vol/b_vol * 100

    print("volume of bucket :{:.2f} ".format(b_vol))
    
    if w_per > 100:
        print("percentage of water : {:.2f}%".format(w_per),"overflow")
    else:
        print("percentage of water : {:.2f}%".format(w_per))

per =0

h, r, vol = input("Enter height & radius: ").split()
h = float(h)
r = float(r)
vol = float(vol)
cal()
