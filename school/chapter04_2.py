#나이 검사
age = int(input('나이: '))
if(age >= 15) :
    print("본 영화를 보실 수 있습니다")
else: 
    print("영화를 보실 수 없습니다\n")
    print("다른 영화를 보시겠어요?")

#윤년
year = int(input('연도를 입력하세요: '))
if( ((year % 4==0) and (year % 100 !=0))or(year % 400 ==0)):
    print(f'{year} 년은 윤년입니다.')

else:
    print("윤년이 아닙니다.")


#랜덤함수로 동전 던지기 게임
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")