def Counting( sf ) :
  lowerC = 0; upperC = 0
  for c in sf : 
    if c.islower() :
      lowerC += 1
    elif c.isupper() :
      upperC += 1
  return lowerC, upperC

s = input("문자열 입력 : ")
if s == "" :
  print("입력 데이터가 없습니다")
else :
  c1, c2 = Counting(s)
  print("소문자 개수 : %d, 대문자 개수 : %d" %(c1, c2))
