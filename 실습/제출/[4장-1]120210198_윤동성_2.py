s1 = "2021"
s2 = "03"
s3 = "21"
n1 = 12345.12345
n2 = 54321.54321

print("(1) Today is {}/{}/{}" .format(s1, s2, s3))
print("(2) n1={}, n2={}" .format(n1, n2))
print("(3) n1={:!^40.3f}" .format(n1))
print("(4) n2={:15.3e}" .format(n2))
print("(5) n1={:%<10.2f}" .format(n1))
