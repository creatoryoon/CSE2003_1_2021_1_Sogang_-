st1 = input("Enter the first string:")
st2 = input("Enter the second string:")

st1 = list(st1)
st2 = list(st2)


if sorted(st1) == sorted(st2):
    print("%s, %s is anagram." %(str(''.join(st1)),str(''.join(st2))))

else :
    print("%s, %s is not anagram." %(str(''.join(st1)),str(''.join(st2))))


