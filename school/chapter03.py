"""
sec = eval(input('초를 입력하세요: '))
hour = sec//3600
min = (sec%3600) // 60
second = (sec%3600) % 60
print(f'입력한 시간은 {hour} 시간 {min} 분 {second} 초입니다.')
"""

"""
f = eval(input('화씨 온도: '))
c = (f-32) * (5/9)
print(f'섭씨온도: {c}')
"""

sex = int(input('여성이면1, 남성이면 0을 입력하세요: '))
height = int(input('당신의 키는 얼마입니까? '))
waist = int(input('당신의 허리 둘레는 얼마입니까? '))
print(f'당신의 rfm은 {64-(20*(height / waist)+ 12 * sex)}')