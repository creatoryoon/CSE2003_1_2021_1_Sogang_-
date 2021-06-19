score = [int(x) for x in input("Enter the scores: ").split()]




for i in range(len(score)):
    if score[i] >= 90:
        print("%d student : A" %(i+1))
    elif score[i] >= 70:
        print("%d student : B" %(i+1))
    elif score[i] >= 50:
        print("%d student : C" %(i+1))
    else:
        print("%d student : F" %(i+1))
