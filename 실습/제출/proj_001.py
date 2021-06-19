#!/usr/bin/python3

import random, time, os
size=4
life_count=5
game_over=0
check=0
def Test_one(puzzle): #ANS : W W A A A
    puzzle[0][0] = 15;	puzzle[0][1] = 14;	puzzle[0][2] = 13;	puzzle[0][3] = 12;
    puzzle[1][0] = 0;	puzzle[1][1] = 10;	puzzle[1][2] = 9;	puzzle[1][3] = 8;
    puzzle[2][0] = 11;	puzzle[2][1] = 6;	puzzle[2][2] = 5;	puzzle[2][3] = 4;
    puzzle[3][0] = 7;	puzzle[3][1] = 3;	puzzle[3][2] = 2;	puzzle[3][3] = 1;
    return puzzle

def Test_two(puzzle):  #ANS : W A W D D W A A 
    puzzle[0][0] = 15;	puzzle[0][1] = 14;	puzzle[0][2] = 0;	puzzle[0][3] = 12;
    puzzle[1][0] = 11;	puzzle[1][1] = 10;	puzzle[1][2] = 13;	puzzle[1][3] = 9;
    puzzle[2][0] = 7;	puzzle[2][1] = 5;	puzzle[2][2] = 4;	puzzle[2][3] = 8;
    puzzle[3][0] = 3;	puzzle[3][1] = 6;	puzzle[3][2] = 2;	puzzle[3][3] = 1;
    return puzzle

def Test_three(puzzle): #ANS : A S S D W A S D W A A W W A 
    puzzle[0][0] = 11;	puzzle[0][1] = 15;	puzzle[0][2] = 13;	puzzle[0][3] = 12;
    puzzle[1][0] = 14;	puzzle[1][1] = 6;	puzzle[1][2] = 10;	puzzle[1][3] = 8;
    puzzle[2][0] = 0;	puzzle[2][1] = 7;	puzzle[2][2] = 9;	puzzle[2][3] = 4;
    puzzle[3][0] = 3;	puzzle[3][1] = 2;	puzzle[3][2] = 5;	puzzle[3][3] = 1;
    return puzzle


"""**********************************************************
* 퍼즐게임의 global 변수와 게임판을 초기화 해준다.
  빈칸의 경우 0으로 초기화 해준다.
* input	: (list) 퍼즐게임판
* return: none
***********************************************************"""
def init(puzzle):
    i=0
    j=0
    game_over = 0
    for i in range(size):
        for j in range(size):
            puzzle[i][j] = size*size-1-size*i-j;
 
"""**********************************************************
* 퍼즐게임판을 출력해준다.
* input	: (list) 퍼즐게임판
* return: none
***********************************************************/"""
def printPuzzle(puzzle):
    i=0
    j=0
    os.system("clear");
    for i in range(size):
        for j in range(size):
            print("+--",end="")
        print("+")
        for j in range(size-1):
            if puzzle[i][j] == 0:
                print("|  ",end="")
            else:
                print("|"+"\033[33m"+"%2d"%puzzle[i][j]+"\033[0m",end='')
        if(puzzle[i][j+1] == 0):
            print("|  |")
        else:
            print("|"+"\033[33m%2d\033[0m|\n"%puzzle[i][j+1],end='')
    for j in range(size) :
        print("+--",end="");
    print("+");


"""**********************************************************
* 퍼즐게임이 끝났는지를 체크한다.
* input	: (list) 퍼즐게임판
* return: none
***********************************************************"""
def checkPuzzle(puzzle) :

#TODO
    check1 = []
    check2 = []
    for k in range((len(puzzle)**2)-1,-1,-1):
        check2.append(k)

    for i in puzzle:
        for j in i:
            check1.append(j)
    if check1 == check2:
        global game_over
        game_over = 1
"""**********************************************************
* 퍼즐게임판에서 빈칸의 위치를 찾는다.
* input	: (list) 퍼즐게임판
* return: (int)퍼즐의 빈칸의 위치
***********************************************************/"""
def find_0_loc(puzzle):
 
#TODO
    temp1 = 0
    row, col = 0, 0
    for i in puzzle:
        
        if 0 in i:
            row = temp1
            col = i.index(0)
            
            break;
        temp1 = temp1 + 1
    return row, col

"""**********************************************************
* 콘솔창에 입력하는 key의 값을 받아온다.(Enter 필요없음)
* input	: none
* return: (str) 입력받은 key
***********************************************************/"""
def getch():
    import termios, sys, tty
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch

"""**********************************************************
* command에 대한 동작을 수행한다.
  'w' 'W' - 빈칸을 아래로
  'a' 'A' - 빈칸을 오른쪽으로 
  's' 'S' - 빈칸을 위로
  'd' 'D' - 빈칸을 왼쪽으로
  'q' 'Q' - 게임 종료
* input	: (list) 퍼즐게임판
          (int) 퍼즐게임판에서 빈칸의 위치
          (int) 입력받은 key에 대한 command
* return: (int) command에 대한 동작 수행여부
***********************************************************/"""
def move_to(puzzle,row, col, command):#////////////HERE

#TODO 
    temp = 0
    
    if command == 2:
        if row == 0:
            temp = 0
        else:
            temp = puzzle[row-1][col]
            puzzle[row-1][col] = 0
            puzzle[row][col] = temp
            temp = 1

    elif command == 3:
        if col == 0:
            temp = 0
        else:
            temp = puzzle[row][col-1]
            puzzle[row][col-1] = 0
            puzzle[row][col] = temp
            temp = 1
    elif command == 0:
        if row == size-1:
            temp = 0
        else:
            temp = puzzle[row+1][col]
            puzzle[row+1][col] = 0
            puzzle[row][col] = temp
            temp = 1
    elif command == 1:
        if col == size-1:
            temp = 0
        else:
            temp = puzzle[row][col+1]
            puzzle[row][col+1] = 0
            puzzle[row][col] = temp
            temp = 1
    else:
        temp = 0
    return temp


"""**********************************************************
* 퍼즐게임판을 랜덤하게 섞는다.
* input	: (list) 퍼즐게임판
* return: none
***********************************************************"""
def shuffle(puzzle):
    r=0
    l=0
    i = 100
    while i:
        i=i-1
        l, c = find_0_loc(puzzle)
        r = random.randint(0,100)%4
        move_to(puzzle,l, c,r)

"""**********************************************************
* getch()함수로 입력받은  key를 가져와 해당하는 key 값을 return 해준다.
  'w', 'W', 'a', 'A', 's', 'S', 'd', 'D' key를 제외한 다른 key가 입력으로 들어올시 -1을 return 한다.
* input	: none
* return: (int) getch()로 입력받은 key의 값
***********************************************************/"""
def GetCommand():
    ch = getch()

    if ch =='w' or ch=='W':
        return 0
    elif ch=='a' or ch=='A':
        return 1
    elif ch=='s' or ch=='S':
        return 2
    elif ch=='d' or ch=='D':
        return 3
    elif ch=='q' or ch=='Q':
        return 4
    else:
        return -1
    return -1



"""**********************************************************
* 퍼즐게임 시작시 실행되며, 퍼즐게임판을 초기화하고,
  입력받은 command에 대한 동작을 수행한다.
  life가 0이 되거나, 게임을 clear했을 시 프로그램을 종료한다.

* input	: none
* return: 0
***********************************************************"""
puzzle = []
for i in range(size):               # 크기가 size * size인 퍼즐게임판
    p = [0 for i in range(size)]
    puzzle.append(p)
life = life_count                   # 게임 생명 카운트 
command = -1
flag=0
location=0
random.seed(time.time())            # 난수를 생성하기 위한 설정
init(puzzle)                        #  퍼즐게임판 초기화 
shuffle(puzzle)                     # 퍼즐게임판 섞기

Test_one(puzzle) 
#Test_two(puzzle) 
#Test_three(puzzle) 

""""입력이 일어날때마다 퍼즐게임판을 새롭게 그린다."""

while game_over != 1:
    command = GetCommand()
#TODO
#퍼즐게임판에서 빈칸을 찾는다(find_0_loc(_))
    row, col = find_0_loc(puzzle)
#key에 대한 동작을 수행한다.
    if command==0 or command==1 or command==2 or command==3:
        check = move_to(puzzle,row, col, command)
        life = life - check
    else :
        pass;
    printPuzzle(puzzle) # 퍼즐게임판 그리기

#게임 진행에 필요한 정보 출력 
    print('\033[32m'+"up    : w\nleft  : a\ndown  : s\nright : d\n"+'\033[0m')
    print('\033[33mLife : %d\n\033[0m'%life)
    print('\033[31m'+"Press Command...\n"+'\033[0m')

#TODO 
#퍼즐게임 종료조건 체크한다.
    checkPuzzle(puzzle)
    if command == 4:
        break;
    if life == 0:
        break;
#while 부분 ---------------------------------------------

"""퍼즐게임 결과 출력"""
print("\n\n\n\n\n")
if game_over:
    print("\033[31m"+"      Success!\n\n\n"+"\033[0m")
else:
    if life <= 0 or command == 4:
        print("\033[31m"+"      Fail!\n\n\n"+"\033[0m")
    else:
        print("\033[31m"+"      Success!\n\n\n"+"\033[0m")

