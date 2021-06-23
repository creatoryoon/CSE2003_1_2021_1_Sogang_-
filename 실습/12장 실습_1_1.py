def CheckPassword(s):
    if len(s) < 8:
        print("Error! At least, password has 8 character. ")
        return False
    if not(s.isalnum()):
        print("Error! Password must have ONLY alphabet and number.")
        return False
    if s.isalpha():
        print("Error! Password must have number.")
        return False
    if s.isdigit():
        print("Error! Password must have alphaber.")
        return False        
    
    count = 0
    for ch in s:
        if ch.isnumeric():
            count += 1
    if count >=2:
            return True
    else:
        print("Error! Password must have 2 numbers, at least.")
        return False

for i in range(5):
    p = input("Enter password: ")
    if CheckPassword(p):
        print("Valid password")
        break
    else:
        print("Invalid password")

