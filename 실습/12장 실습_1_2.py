def char_freq( s ) :
  D = {}
  for c in s :  # s의 모든 문자에 대해
    if c.isspace( ) :  # 공백 문자이면 skip
      continue
    D[c]=D.get(c,0)+1
  return D


s = input("Enter the string : ")
s = s.lower()
D = char_freq(s)
for k in D :
    print("%s : %d" %(k, D[k]))
