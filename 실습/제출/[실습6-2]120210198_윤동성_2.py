a, b, c = map(int, input("Enter the triangle : ").split())

if ( a >= 0 and b >= 0 and c >= 0 ):
    if ( (a + b) > c  and (a + c) > b and (b + c)>a ):
        if( a == b or b == c or c == a ):
            if( a == b and a == c ):
                print("Equilateral triangle")
            else:
                print("Isosceles triangle")
        elif( ((a**2)+(b**2) == (c**2)) or ((a**2)+(c**2)==(b**2)) or ((b**2)+(c**2)==(a**2))):
            print("Right-angled triangle")
        else:
            print("Normal triangle")
        
    else:
        print("It is not trialgle.")




else:
    print("There is the negative number(<0)!!")

