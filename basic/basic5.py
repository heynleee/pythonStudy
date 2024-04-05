##표준입력
#input() 함수를 이용한 입력
num = input('숫자를 입력하세요: ')
print(num)
#print(num+10) # 입력값은 문자열인 관계로 사칙연산 오류

# 입력 값을 숫자로 변환
num = eval(input('숫자를 입력하세요: '))
print(num+10)
num = int(input('숫자를 입력하세요: '))
print(num)
num = int(input('숫자를 입력하세요(16진수로 변환): '), 16)
print(num)