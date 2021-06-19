def strings(st):
    st = st.lower()
    st1 = set([])
    for i in st:
        if i == " ":
            pass
        else:
            st1.add(i)
    list1 = list(st1)
    list1.sort()
    list2 = []
    for l in list1:
        list2.append(0)

    for j in st:
        for k in range(len(list1)):
            if list1[k] == j:
                list2[k] = list2[k] + 1
    for m in range(len(list1)):
        print(list1[m],":",list2[m])

    

st = input("Enter the string : ")
strings(st)
        

