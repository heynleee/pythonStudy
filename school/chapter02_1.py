"""
kg = eval(input('체중을 입력하세요: '))
m = eval(input('키를 입력하세요: '))
bmi = kg/m**2
print(f'bmi: {bmi}')
"""
"""" 피자 면적 계산
radius = eval(input('radius: '))
area = 3.14 * radius**2
print(f'피자 면적: {area}')
"""

"""
import turtle

t = turtle.Turtle()
t.shape('turtle')

radius = 100
t.circle(radius)

radius = 200
t.circle(radius)

radius = 50
t.circle(radius)

t.left(90)
radius = 100
t.circle(radius)

radius = 200
t.circle(radius)

radius = 50
t.circle(radius)
"""
"""
ori = eval(input('원금: '))
plus = eval(input('이율: '))
period = eval(input('기간: '))
get = ori * (1.0 + 0.03) ** 5
print(f'수령금액: {get}')
"""

where = input('경기장은 어디입니까? ')
win = input('이긴 팀은 어디입니까? ')
lose = input('진 팀은 어디입니까? ')
mvp = input('우수선수는 누구입니까? ')
score = input('스코어는 몇대몇입니까? ')

print('==================================\n')
print(f'오늘 {where}에서 야구 경기가 열렸습니다.')
print(f'{win} 과 {lose} 은 치열한 공방전을 펼쳤습니다.')
print(f'{mvp}의 맹활약으로 {win} 가 {lose} 를 {score}로 이겼습니다. ')

