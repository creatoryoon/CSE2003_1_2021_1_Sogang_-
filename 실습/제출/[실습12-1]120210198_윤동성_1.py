def checkpw(st):
    flag = True
    if len(st) < 8:
        flag = False
        print("Error! At least, password has 8 character")
    if st.isalnum() == False:
        print("Error! Password must have ONLY alphabet and number.")
        flag = False
    if st.isdigit() == True:
        print("Error! Password must have alphabet.")
        flag = False

    numcount = 0
    for num in range(10):
        numcount = numcount + st.count(str(num))

    if st.isalpha() == True:
        print("Error! Password must have number.") 
        flag = False
    elif num < 2:
        print("Error! Password must have 2 numbers, at least.")
    return flag


for i in range(5):
    pw = input("Enter password: ")
    chk = checkpw(pw)
    if chk == False:
        print("Invalid password")
        continue
    else:
        print("Valid password")
        break
