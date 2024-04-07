import random
me = int(input('가위(1), 바위(2), 보(3) : '))
computer = random.randint(1,4)
print("컴퓨터의 선택은 " + str(computer))
print("사람의 선택은 " + str(me))

if(computer == 1) :
    if( me == 2) :
        print(" 사람이 이겼습니다. 컴퓨터 패배 ")
        if(me == 3) :
            print(" 사람이 졌습니다. 컴퓨터 승")
        else:
            print("비겼습니다.")
if(computer == 2) :
    if( me == 3) :
        print(" 사람이 이겼습니다. 컴퓨터 패배 ")
        if(me == 1) :
            print(" 사람이 졌습니다. 컴퓨터 승")
        else:
            print("비겼습니다.")

if(computer == 3) :
    if( me == 1) :
        print(" 사람이 이겼습니다. 컴퓨터 패배 ")
        if(me == 2) :
            print(" 사람이 졌습니다. 컴퓨터 승")
        else:
            print("비겼습니다.")
    
   
    




