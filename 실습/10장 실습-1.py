n=int(input("Enter a number to be checked:"))

origin=n
reverse=0

while(n>0):
    tail=n%10
    reverse=reverse*10+tail
    n=n//10

if(origin==reverse):
    print(origin,"is a palindrome!")
else:
    print(origin,"is NOT a palindrome")

