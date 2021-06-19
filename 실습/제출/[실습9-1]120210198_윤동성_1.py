a = input("Input:")
flag = 0
idx = []

for i in a:
    
    if i == "h":
        idx.append(flag)
    flag += 1

output = a[0:idx[0]]+a[idx[-1]+1:]

print("Output:"+output)
