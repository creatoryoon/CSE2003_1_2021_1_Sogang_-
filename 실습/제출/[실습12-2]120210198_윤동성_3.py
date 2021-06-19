

def trans():
    global s
    for i in range(3):
        print("***original string: %s ***##" %s, end="")
        
    s = "The string printed out!"
    print(s)
    return s

s = input("Enter the string: ")
trans()
print(s)
