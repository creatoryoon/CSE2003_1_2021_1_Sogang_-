#!/usr/bin/python3

import random, time, os
size=4
life_count=100
game_over=0
check=0

#TODO
solution = []
users = []

def incode():
    solution.reverse()
    for i in range(len(solution)):
        if solution[i] == 0 :
            solution[i] = "S"
        elif solution[i] == 1:
            solution[i] = "D"
        elif solution[i] == 2:
            solution[i] = "W"
        elif solution[i] == 3:
            solution[i] = "A"
    return solution
def solusort():
    incode()
    flag = True
    while flag:
        if len(solution) <= 1:
            break;
        for i in range(len(solution)):
            if i < len(solution)-1 and solution[i] == "S":
                if solution[i+1] == "W":
                    del solution[i]
                    del solution[i]
                    break;
            elif i < len(solution)-1 and solution[i] == "W":
                if solution[i+1] == "S":
                    del solution[i]
                    del solution[i]
                    break;
            elif i < len(solution)-1 and solution[i] == "A":
                if solution[i+1] == "D":
                    del solution[i]
                    del solution[i]
                    break;
            elif i < len(solution)-1 and solution[i] == "D":
                if solution[i+1] == "A":
                    del solution[i]
                    del solution[i]
                    break;
            else:
                flag = False
   
                

def userincode():
    if len(users) >= 1:
        for i in range(len(users)):
            if users[i] == 0 :
                users[i] = "W"
            elif users[i] == 1:
                users[i] = "A"
            elif users[i] == 2:
                users[i] = "S"
            elif users[i] == 3:
                users[i] = "D"
        print("Your input is..")
        print("[",end="")
        for i in range(len(users)):
            if i == (len(users)-1):
                print(users[i], end="")
                if len(users)%5 == 0:
                    print("]")
                else : print("--"*(5-(len(users)%5))+"]")            
            elif (i+1)%5 == 0:
                print(users[i]+"]\n[", end="")
            else : 
                print(users[i], end="-")
    else: pass




def Test_one(puzzle): #ANS : W W A A A
    puzzle[0][0] = 15;	puzzle[0][1] = 14;	puzzle[0][2] = 13;	puzzle[0][3] = 12;
    puzzle[1][0] = 0;	puzzle[1][1] = 10;	puzzle[1][2] = 9;	puzzle[1][3] = 8;
    puzzle[2][0] = 11;	puzzle[2][1] = 6;	puzzle[2][2] = 5;	puzzle[2][3] = 4;
    puzzle[3][0] = 7;	puzzle[3][1] = 3;	puzzle[3][2] = 2;	puzzle[3][3] = 1;
    global solution
    solution.clear()
    solution = ["W","W","A","A","A"]
    return puzzle

def Test_two(puzzle):  #ANS : W A W D D W A A 
    puzzle[0][0] = 15;	puzzle[0][1] = 14;	puzzle[0][2] = 0;	puzzle[0][3] = 12;
    puzzle[1][0] = 11;	puzzle[1][1] = 10;	puzzle[1][2] = 13;	puzzle[1][3] = 9;
    puzzle[2][0] = 7;	puzzle[2][1] = 5;	puzzle[2][2] = 4;	puzzle[2][3] = 8;
    puzzle[3][0] = 3;	puzzle[3][1] = 6;	puzzle[3][2] = 2;	puzzle[3][3] = 1;
    global solution
    solution.clear()
    solution = ["W", "A", "W", "D", "D", "W", "A", "A"]
    return puzzle

def Test_three(puzzle): #ANS : A S S D W A S D W A A W W A 
    puzzle[0][0] = 11;	puzzle[0][1] = 15;	puzzle[0][2] = 13;	puzzle[0][3] = 12;
    puzzle[1][0] = 14;	puzzle[1][1] = 6;	puzzle[1][2] = 10;	puzzle[1][3] = 8;
    puzzle[2][0] = 0;	puzzle[2][1] = 7;	puzzle[2][2] = 9;	puzzle[2][3] = 4;
    puzzle[3][0] = 3;	puzzle[3][1] = 2;	puzzle[3][2] = 5;	puzzle[3][3] = 1;
    global solution
    solution.clear()
    solution = ["A", "S", "S", "D", "W", "A", "S", "D", "W", "A", "A", "W", "W", "A"]
    return puzzle


"""**********************************************************
* ??????????????? global ????????? ???????????? ????????? ?????????.
  ????????? ?????? 0?????? ????????? ?????????.
* input	: (list) ???????????????
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
* ?????????????????? ???????????????.
* input	: (list) ???????????????
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
* ??????????????? ??????????????? ????????????.
* input	: (list) ???????????????
* return: none
***********************************************************"""
def checkPuzzle(puzzle) :

#TODO
    check1 = []
    check2 = []
    for k in range((size**2)-1,-1,-1):
        check2.append(k)

    for i in puzzle:
        for j in i:
            check1.append(j)
    if check1 == check2:
        global game_over
        game_over = 1
"""**********************************************************
* ????????????????????? ????????? ????????? ?????????.
* input	: (list) ???????????????
* return: (int)????????? ????????? ??????
***********************************************************/"""
def find_0_loc(puzzle):
 
#TODO
    temp = 0
    flag = False
    for i in puzzle:
        if flag == True:
            break;
        for j in i:
            if j == 0:
                flag = True
                break;
            else: temp = temp + 1


    return temp
"""**********************************************************
* ???????????? ???????????? key??? ?????? ????????????.(Enter ????????????)
* input	: none
* return: (str) ???????????? key
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
* command??? ?????? ????????? ????????????.
  'w' 'W' - ????????? ?????????
  'a' 'A' - ????????? ??????????????? 
  's' 'S' - ????????? ??????
  'd' 'D' - ????????? ????????????
  'q' 'Q' - ?????? ??????
* input	: (list) ???????????????
          (int) ????????????????????? ????????? ??????
          (int) ???????????? key??? ?????? command
* return: (int) command??? ?????? ?????? ????????????
***********************************************************/"""
def move_to(puzzle,loc, command):#////////////HERE

#TODO 
    temp = 0
    
    global size
    if command == 2:
        if (loc//size) == 0:
            temp = 0
        else:
            temp = puzzle[(loc//size)-1][(loc%size)]
            puzzle[(loc//size)-1][(loc%size)] = 0
            puzzle[(loc//size)][(loc%size)] = temp
            temp = 1

    elif command == 3:
        if (loc%size) == 0:
            temp = 0
        else:
            temp = puzzle[(loc//size)][(loc%size)-1]
            puzzle[(loc//size)][(loc%size)-1] = 0
            puzzle[(loc//size)][(loc%size)] = temp
            temp = 1
    elif command == 0:
        if (loc//size) == size-1:
            temp = 0
        else:
            temp = puzzle[(loc//size)+1][(loc%size)]
            puzzle[(loc//size)+1][(loc%size)] = 0
            puzzle[(loc//size)][(loc%size)] = temp
            temp = 1
    elif command == 1:
        if (loc%size) == size-1:
            temp = 0
        else:
            temp = puzzle[(loc//size)][(loc%size)+1]
            puzzle[(loc//size)][(loc%size)+1] = 0
            puzzle[(loc//size)][(loc%size)] = temp
            temp = 1
    else:
        temp = 0
    return temp


"""**********************************************************
* ?????????????????? ???????????? ?????????.
* input	: (list) ???????????????
* return: none
***********************************************************"""
def shuffle(puzzle):
    r=0
    l=0
    i = 100
    while i:
        i=i-1
        l = find_0_loc(puzzle)
        r = random.randint(0,100)%4
        #TODO
        flag = move_to(puzzle,l,r)
        if flag ==1:
            solution.append(r)

"""**********************************************************
* getch()????????? ????????????  key??? ????????? ???????????? key ?????? return ?????????.
  'w', 'W', 'a', 'A', 's', 'S', 'd', 'D' key??? ????????? ?????? key??? ???????????? ???????????? -1??? return ??????.
* input	: none
* return: (int) getch()??? ???????????? key??? ???
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
* ???????????? ????????? ????????????, ?????????????????? ???????????????,
  ???????????? command??? ?????? ????????? ????????????.
  life??? 0??? ?????????, ????????? clear?????? ??? ??????????????? ????????????.

* input	: none
* return: 0
***********************************************************"""
puzzle = []

for i in range(size):               # ????????? size * size??? ???????????????
    p = [0 for i in range(size)]
    puzzle.append(p)

life = life_count                   # ?????? ?????? ????????? 
command = -1
flag=0
location=0
random.seed(time.time())            # ????????? ???????????? ?????? ??????
init(puzzle)                        #  ??????????????? ????????? 
shuffle(puzzle)                     # ??????????????? ??????
solusort()
#Test_one(puzzle) 
#Test_two(puzzle) 
#Test_three(puzzle) 

""""????????? ?????????????????? ?????????????????? ????????? ?????????."""

while game_over != 1:
    command = GetCommand()
#TODO
#????????????????????? ????????? ?????????(find_0_loc(_))
    location = find_0_loc(puzzle)
#key??? ?????? ????????? ????????????.
    if command==0 or command==1 or command==2 or command==3:
        check = move_to(puzzle,location, command)
        if check == 1:
            users.append(command)
        life = life - check
    else :
        pass;
    printPuzzle(puzzle) # ??????????????? ?????????
    # print(solution) # test??? ????????? ??????
    # userincode() # test???
#?????? ????????? ????????? ?????? ?????? 
    print('\033[32m'+"up    : w\nleft  : a\ndown  : s\nright : d\n"+'\033[0m')
    print('\033[33mLife : %d\n\033[0m'%life)
    print('\033[31m'+"Press Command...\n"+'\033[0m')

#TODO 
#???????????? ???????????? ????????????.
    checkPuzzle(puzzle)
    if command == 4:
        break;
    if life == 0:
        break;
#while ?????? ---------------------------------------------

"""???????????? ?????? ??????"""
print("\n\n\n\n\n")
if game_over:
    print("\033[31m"+"      Success!\n\n\n"+"\033[0m")
    userincode()
    print("Standard Solution is:\n[",end="")
    for i in range(len(solution)):
        if i == (len(solution)-1):
            print(solution[i], end="")
            if len(solution)%5 == 0:
                print("]")
            else : print("--"*(5-(len(solution)%5))+"]")            
        elif (i+1)%5 == 0:
            print(solution[i]+"]\n[", end="")
        else : 
            print(solution[i], end="-")
    print("The standard solution is possible with '%d' attempts, but you have tried '%d' times." %(len(solution), (life_count-life)))
else:
    if life <= 0 or command == 4:
        print("\033[31m"+"      Fail!\n\n\n"+"\033[0m")
        userincode()
        print("Standard Solution is:\n[",end="")
        for i in range(len(solution)):
            if i == (len(solution)-1):
                print(solution[i], end="")
                if len(solution)%5 == 0:
                    print("]")
                else : print("--"*(5-(len(solution)%5))+"]")            
            elif (i+1)%5 == 0:
                print(solution[i]+"]\n[", end="")
            else : 
                print(solution[i], end="-")
        if command==4:
            if life_count == life:
                print("The standard solution is possible with '%d' attempts, but you haven't even tried." %len(solution))        
                
            else: 
                print("The standard solution is possible with '%d' attempts, but you gave up on '%d' attempts." %(len(solution), (life_count-life)))        
            
        else :
            print("The standard solution is possible with '%d' attempts." %len(solution))
            print("You've failed '%d' attempts, but you haven't given up, so next time it'll be possible."  %life_count )        
    else:
        print("\033[31m"+"      Success!\n\n\n"+"\033[0m")
        userincode()
        for i in range(len(solution)):
            if i == (len(solution)-1):
                print(solution[i], end="")
                if len(solution)%5 == 0:
                    print("]")
                else : print("--"*(5-(len(solution)%5))+"]")            
            elif (i+1)%5 == 0:
                print(solution[i]+"]\n[", end="")
            else : 
                print(solution[i], end="-")
        print("The standard solution is possible with '%d' attempts, but you have tried '%d' times." %(len(solution), (life_count-life)))
