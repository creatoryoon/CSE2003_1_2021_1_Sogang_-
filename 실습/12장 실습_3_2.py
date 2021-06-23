def say(M,N):
    L=[]
    for i in range(len(M)):
        if M[i] in N:
            L.append(M[i])
            L=set(L);L=list(L)
    if len(L)!=0:
        return True,L
    else:
        return False,L            
            
list1=list(int(x) for x in input("enter list1 elements:").split())
list2=list(int(y) for y in input("enter list2 elements:").split())
a,b=say(list1,list2)
if a!=0:
    print(b,'overlapping elements')
else:
    print('No overlapping elements')
    
