num1 = 10
num2 = 20
print(num1, num2)

# 하나의 변수에 두개의 값을 할당하면 배열이됨.
a = 100, 200
print(a)
print(a[1])

print(type([123]))
print(type('hello'))
print(type(12.2))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({10,20,30}))
print(type({'a':10, 'b':20, 'c':30}))

print(num1 + num2)
print(num1 * num2**2 / 100)

result = num1 == num2
print(result)

if(num1 > num2) :
    print('num1이 num2보다 크다')

login = False

if(num1>10 and num2 != 20):
    print('num1이 10보다 크고 num2가 20이 아닌경우 실행')
if(num1 > 10 or num2 <= 20):
    print('num1이 10보다 크거나 20보다 작은 경우 실행')
if(not login) :
    print('login 변수값이 false인 경우 실행')

num1 += 10
print(num1)

print(10 in [10, 20, 30])
num3 = num1
print (num1 is num3)

