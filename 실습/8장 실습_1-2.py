employee = {'kim','lee','park','choi','jung','kang','jo','yoon','jang', 'lim'}
late = {'yoon','park'}
absent = {'jung','yoon','park', 'lim'}
print("The whole employee : ", employee)
print("late : ",late)
print("absence : ",absent)
print("The list of the employees that get bonus : ", employee-late-absent) #지각과 결근을 하지 않은 사원
print("The list of the employees that must work overtime : ", late & absent) #야근: 지각과 결근을 모두 한 사원

new = set(input("Enter the new employees : ").split()) #입력받은 스트링의 리스트를 집합으로 변환

#중복여부 확인
over = employee & new #겹치는 사원
if over != set() : #공집합의 형태에 주의
    print("the names of the new and existing employess is same.")

employee |= new #고용자에 신입사원 추가하기
print("The list of entire employees : ", employee)







