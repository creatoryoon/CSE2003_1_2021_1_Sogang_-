def menu1():
    L=input("이름 중간 기말 성적 입력:").split()
    global D;global M
    if len(L)!=3:
        print("입력 데이터 갯수 오류입니다.")
    else:
        if L[0] in D:
            print("이미 존재하는 학생 정보입니다.")
        else:
            for i in range(1,len(L)):
                L[i]=int(L[i])
            score=L[1]*40/100+L[2]*60/100
            import math
            score=math.trunc(score)
            if score>=90:
                grade='A'
            elif score>=80:
                grade='B'
            elif score>=70:
                grade='C'
            else:
                grade='D'
            D[L[0]]=L[1],L[2],grade
            M=list(D)
def menu2():
    if len(D)==0:
        print("입력된 학생 정보가 없습니다")
    else:
        print();print("name    mid  final  grade");print('-'*25)
        for i in range(len(D)):
            print("%s    %d    %d    %s"%(M[i],D[M[i]][0],D[M[i]][1],D[M[i]][2]))
def menu3():
    if len(D)==0:
        print("입력된 학생 정보가 없습니다")
    else:        
        name=input("삭제할 학생의 이름을 입력:")
        if name in D:
            del D[name]
            print("%s 학생의 정보를 삭제했습니다."%name)
        else:
            print("정보가 없는 학생입니다.")
print("*Menu******************************")
print("1. 성적 관리(입력 형태는 name score1 score2")
print("2. 학생 정보 출력")
print("3. 학생 정보 삭제")
print("4. 프로그램 종료")
print('*'*35)
D={}
while(True):
    select=input("메뉴 1,2,3,4번 중 하나 선택:")
    if select=='1':
        menu1()
    elif select=='2':
        menu2()
    elif select=='3':
        menu3()
    elif select=='4':
        print("프로그램을 종료합니다")
        break
    else:
        print("없는 번호의 명령어입니다. 다시 선택하세요.")

