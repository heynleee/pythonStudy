##리스트
list1 = [10, 20, 30, 40]
list2 = [i for i in range(1,10)]
list3 = [0 for i in range(10)] 
#list3 = [0] * 10 # 특정 값으로 초기화 (0, 0, 0, 0, 0, 0, 0, 0, 0)
print(sum(list1))

#리스트 값 조작
list1.append(50)
list1[0] = 100
list1[1:2] = [200,300]
list2.insert(1,2)
del(list2[3]) 
list3.remove(0)

#리스트 값 출력
print(list1)
print(list2)
print(list3)
print(list1[2:5])
print(list1[:3])

#리스트 결합
print(list1 + list2)
print(list1 * 3)

# for 문과 함께 사용시 유용한 방법들
for i, n in enumerate(list1) :
    print(i, n)

for l1, l2, in zip(list1, list2) : # 두개의 리스트로 부터 입력을 받아 처리, 짧은 쪽에 맞춰짐.
    print(l1, l2)

#기타
print(len(list1))
print(list1.pop()) # 맨 마지막 값을 리턴하고 삭제
print(list1)

print(list3.count(0)) # 특정 값이 몇개 있는지 카운트

list1.sort() #정렬, 오름차순, 리스트 구조 변경됨.
print(list1)

list1.sort(reverse=True) # 내림차순
print(list1)

list1.reverse() #배치 역순으로
print(list1)

list4 = list1.copy() # 값을 복사한 새로운 리스트 객체
#list4 = list1 #list1을 가리키는 변수로 list1과 동일 객체
list4.append(500)
print(list1)
print(list4)

