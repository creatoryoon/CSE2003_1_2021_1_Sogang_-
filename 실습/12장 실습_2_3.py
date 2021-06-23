def f():
    global s
    for i in range(3):
        print("***original string: ", s, "***", end="##")
    s="The string printed out!"
    print(s)

s = input("Enter the string: ")
f()
print(s)

