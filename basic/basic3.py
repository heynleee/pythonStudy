# 함수 선언만 해두고 내용은 추후 구현하고자 할때
def printAll():
    pass #pass 없는 경우 에러

#인자가 하나인 함수
def printName(name):
    ptrMsg = name + 'Hello'
    print(ptrMsg)

printName('홍길동')

#인자가 두개이고 리턴이 있는 함수
def calc(num1, num2) :
    return num1 + num2

print('계산결과: ', calc(200,300))
print('계산결과: ', calc(num1=200, num2=300)) # 변수명을 명시해서 호출 가능

# 가변 인자
def total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot

t = total(1,2)
print(t)
t = total(1, 5, 2, 6)
print(t)
print(total(1,2,3)) # print 문 안에서 함수 호출 결과 출력

#리턴이 여러개인 함수, 가변인자 사용
def addNum(*nums) :
    tot = 0
    cnt = 0
    for n in nums :
        tot += n
        cnt += 1
    return cnt, tot

cnt, tot = addNum(10, 20, 30)
print(cnt, tot)

# 매개변수 유형에 따른 caller 값 변경 여부
#원시 자료형은 immutable로 값이 복사되어 전달
#list, dictionary 같은 객체는 mutable로 레퍼런스만 전달되어 caller 값도 변경.
num3 = 10 # num3는 int -> 변경 불가능
m = [1,2,3] # m은 리스트 -> 변경 가능

def varChange(num3, m) :
    num3 = num3 + 1 # 함수 내에서 num3의 값이 변경되더라도, 함수를 호출한 곳의 num3 값은 변경x
    m.append(0) # 리스트에 새로운 요소 0을 추가 -> 리스트 m 자체에 적용

varChange(num3, m)  # 함수 호출
print(num3, m)  # 호출자 값 체크

# 전역 변수, 지역 변수, global, global의 반대는 nonlocal
num4 = 10 #전역변수
def varTest() :
    global num5 # 함수 내부에서 전역 변수를 직접 변경하려면 앞에 global키워드 명시
    num5 = 100
    #global num4
    num4 =100 # global 키워드 주석 처리됨-> 전역변수 num4와는 별개의 지역변수 -> 함수 내부의 변경이 전역변수 num4에 영향을 주지 않음

varTest()
print(num4)
print(num5)
#print(num5) #에러, varTest()에서 num5를 global로 바꾸어서도 테스트