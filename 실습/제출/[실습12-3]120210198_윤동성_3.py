student = [["name", "mid", "final", "grade"]]


def menu1():
    info = list(input("이름 중간 기말 성적 입력:").split())
    if len(info) == 3:
        names = set()
        if len(student) > 1:
            for i in range(1, len(student)):
                names.add(student[i][0])
        if info[0] in names:
            print("이미 존재하는 학생 정보입니다.")
        else:
            info[1] = int(info[1])
            info[2] = int(info[2])
            grade = (info[1]*0.4) + (info[2]*0.6)
            if grade > 89 :
                grade = "A"
            elif grade > 79 :
                grade = "B"
            elif grade > 69 :
                grade = "C"
            else:
                grade = "D"
            info.append(grade)
            student.append(info)
    else:
        print("입력 데이터 갯수 오류입니다.")


def menu2():
    if len(student) <= 1:
        print("입력된 학생 정보가 없습니다")
    else:

        print("%s\t%s\t%s\t%s\t" %(student[0][0],student[0][1],student[0][2],student[0][3]))
        print("----------------------------------------------")
        for i in range(1, len(student)):
            print("%s\t%d\t%d\t%s" %(student[i][0],student[i][1],student[i][2],student[i][3]))


    pass
def menu3():
    if len(student) > 1:

        name1 = input("삭제할 학생의 이름을 입력 :")
        temp = False
        idx = 0
        for i in student:
            if name1 in i:
                temp = True
                break
            else:
                pass
            idx = idx + 1
        if temp == True:
            del student[idx]
            print("%s 학생의 정보를 삭제했습니다." %name1)
        else:
            print("정보가 업는 학생입니다.")
    else:
        print("입력된 학생 정보가 없습니다.")

print("*Menu***********************************")
print("1. 성적 관리 (입력 형태는 name score1 score2)")
print("2. 학생 정보 출력")
print("3. 학생 정보 삭제")
print("4. 프로그램 종료")
print("****************************************")

while True:
    menu = input("메뉴 1,2,3,4번 중 하나 선택 :")
    if menu.isdigit() == False:
        print("숫자를 입력해 주세요")
    else:
        menu = int(menu)
    

        if menu == 1:
            menu1()
        elif menu == 2:
            menu2()
        elif menu == 3:
            menu3()
        elif menu == 4:
            print("프로그램을 종료합니다.")
            break;
        else :
            print("없는 번호의 명령어입니다. 다시 선택하세요.")


