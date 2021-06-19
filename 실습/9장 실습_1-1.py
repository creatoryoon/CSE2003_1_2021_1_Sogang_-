index_count = 0
h_indexes =[]

origin_s = input("Input:")

for i in origin_s:
    if i=='h' :
        h_indexes.append(index_count)
    index_count +=1

first_h_index = h_indexes[0]
last_h_index = h_indexes[len(h_indexes)-1]

print("Output:"+origin_s[0:first_h_index] +origin_s[last_h_index+1:])
