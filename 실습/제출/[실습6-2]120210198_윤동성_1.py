a, b, c = input("Enter the operation : ").split()
a = float(a); c = float(c)
d = 0
if ( b == "+" or b == "*" or b == "--" or b == "/" ):
    if (b == "+"):
        print(a, "+", c, "=",  a + c )
    elif (b == "*"):
        print(a, "*", c,"=",  a * c )
    elif (b == "/"):
        if (c == 0):
            print("'0' cannot divide other number.")
        else :
            print(a, "/", c, "=",  a / c )
    else:
        print( a - c )
else :
    print(b, "is not supported.")
