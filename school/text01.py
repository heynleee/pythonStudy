"""
a = int(input('정수 a를 입력하시오 : '))
b = int(input('정수 b를 입력하시오 : '))
print(f'a / b의 몫 : {a//b}')
print(f'a / b의 나머지 : {a%b}')
"""

"""
a = int(input('세 자리 정수를 입력하시오 : '))
print(f'{a%10}')
print(f'{(a%100)//10}')
print(f'{a//100}')
"""

"""
x1 = int(input('x1 좌표를 입력하시오 : '))
y1 = int(input('y1 좌표를 입력하시오 : '))
x2 = int(input('x2 좌표를 입력하시오 : '))
y2 = int(input('y2 좌표를 입력하시오 : '))
print(f'직각삼각형의 면적은: {((x2-x1)*(y2-y1))/2}')
"""
#정육면체의 부피(1,2번)
s1 = 13
print(f'모서리의 길이가 13인 정육면체 : {s1**3:.2f}')

s2 = 22
print(f'모서리의 길이가 22인 정육면체: {s2**3:.2f}')
print('\n')

#직윤면체의 부피(3번)
w1 = 17
h1 = 25
l1 = 16
print(f'가로, 세로, 길이가 각각 17, 25, 16인 직육면체 : {w1 * h1 * l1:.2f}')
print('\n')

# 원뿔의 부피(4번)
r1 = 10
h2 = 15
print(f'반지름과 높이가 각각 10, 15인 원뿔 : {1/3 * 3.14 * (r1**2) * h2:.2f}')
print('\n')



#구의 부피(5번)
r2 = 25
print(f'반지름이 25인 구 : {4/3 * 3.14 * (r2**3):.2f}')
print('\n')


#원기둥의 부피(6번)
r3 = 10
h3 = 15
print(f'반지름과 높이가 각각 10, 15인 원기둥 : {3.14 * (r3**2)*h3:.2f}')
print('\n')


#import math를 이용하여 math.pi 값을 가져와서(4,5,6)번 문제를 다시 풀어보라.
# 원뿔의 부피(4번)
import math
r1 = 10
h2 = 15
print(f'반지름과 높이가 각각 10, 15인 원뿔 : {1/3 * math.pi * (r1**2) * h2:.2f}')

#구의 부피(5번)
r2 = 25
print(f'반지름이 25인 구 : {4/3 * math.pi * (r2 ** 3):.2f}')

#원기둥의 부피(6번)
r3 = 10
h3 = 15
print(f'반지름과 높이가 각각 10, s5인 원기둥 : {math.pi * (r3**2)*h3:.2f}')

