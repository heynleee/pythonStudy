#4.4
i = int(input('정수를 입력하시오 : '))
if(i%2!=0) :
    print(f'{i}는 2(으)로 나누어지지 않습니다.')
else :
    print(f'{i}는 2(으)로 나누어집니다. ')

if(i%3!=0) :
    print(f'{i}는 3(으)로 나누어지지 않습니다.')
else :
    print(f'{i}는 3(으)로 나누어집니다. ')

if(i%3!=0 or i%2!=0) :
    print(f'{i}는 2와(과) 3 모두로 나누어지지 않습니다.')

#4.5

import random
rotto = [random.randint(0,9) for _ in range(3)]

num1, num2, num3 = map(int, input('세 복권번호를 입력하시오: ').split())

matched =0

matched += rotto.count(num1)
matched += rotto.count(num2)
matched += rotto.count(num3)

matched=min(matched, 3)

if matched == 3 :
    print('상금 1억원')
elif matched ==2 :
    print('상금 1천만원')
elif matched == 1:
    print('상금 1만원')
else :
    print('다음 기회에...')


