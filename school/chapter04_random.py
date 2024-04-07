import random
name1 = input('Player1의 이름: ')
name2 = input('Player2의 이름: ')
print(".....주사위를 굴립니다.....")

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(name1 + "의 주사위 번호는 " + str(num1))
print(name1 + "의 주사위 번호는 " + str(num2))
if num1 == num2 : 
    print("비겼습니다")
else: 
    if num1 > num2 :
        print(name1 + "이  이겼습니다.")
    else:
        num1 < num2 
        print(name2 + "이 이겼습니다.")


