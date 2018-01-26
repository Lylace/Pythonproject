#파이선 자료구조
#리스트 : sequence 자료구조를 사용
#sequence : 순서가 있는 데이터 구조를 의미
#리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용
#리스트 []를 이용해서 각 요소에 접근할 수 있다
msg = 'Hello, World!!'

#파이썬에서는 자료구조를 의미하는 접미사를
#변수명에 사용하기도 한다
list1_list = []                          #빈 리스트
list2_list = [1,2,3,4,5]                 #숫자
list3_list = ['a','b','c']               #문자
list4_list = ['a','b','c',1,2,3,True]    #혼합

print(list1_list)

#간단한 연산
#요소 존재 여부 파악 : in/not in 연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)

#길이 연산 : len()
print(len(list1_list))
print(len(list2_list))

#연결 연산 : +
print(list2_list + list3_list)

#반복 연산 : *
print(list2_list * 2)

#요소의 특정값 참조 : index 사용
print( msg[4], msg[9])
print(list2_list[2])
print(list3_list[2])
print(list4_list[5])

#요소값 변경 : index, = 사용
list2_list[2] = -3
print(list2_list)

#주민번호 성별 여부 판별
jumin_list = [1,2,3,4,5,6,1,2,3,4,5,6,7]
if jumin_list[6] == 1:
    print('이 주민번호는 남성입니다')
else:
    print('이 주민번호는 여성입니다')

#주민코드에서 생년월일 추출
for i in range(0,6):
    print(jumin_list[i], end='')    #줄바꿈 없이 출력 시 종결문자를 지정

#특정범위 내 요소들을 추출할 때는 슬라이스를 사용 [i:j:step]
print(jumin_list[0:6])      #0~5까지
print(jumin_list[:6])       #처음부터 5까지
print(jumin_list[6:])       #6부터 끝까지
print(jumin_list[:])        #전부 출력

print(jumin_list[0:6:2])    #0~5까지 2칸 건너 뛰어서
print(jumin_list[::-1])     #역순 출력

# print(jumin_list[100])      #인덱스 초과 - 오류?
# print(jumin_list[0:100:2])  #인덱스 초과 - 오류?

#리스트관련 통계함수
print(sum(list2_list))
print(max(list2_list))
print(min(list2_list))

#리스트가 주어지면
#이것의 가운데에 있는 요소값을 출력
#[1,2,6,8,4] => 6
#[1,2,6,8,4,10] => 6,8

test_list = [1,2,6,8,4,10]
test_list[len(test_list)-1]

# def middleoflist(list):
#     checklist = len(list) % 2
#     if checklist == 0:
#         print(list[int(len(list)/2)-1:int((len(list)/2)+1)])
#     else:
#         print(list[int((len(list)-1)/2)])
#
# middleoflist(test_list)

def listcenter(list):
    size = len(list)
    mid = int(size/2)
    if size % 2 == 0:
        print(list[mid-1:mid+1])
    else:
        print(list[mid])

listcenter(test_list)

#리스트 조작 함수
#요소 추가 : append
test_list = [1,2,3,4,5]
test_list.append(9)
test_list.append(8)
print(test_list)

#요소 추가 : insert(위치, 값)
test_list.insert(-1, 7)
print(test_list)

#요소 제거 : remove(값), 왼쪽부터 검색 후 검색
test_list.remove(9)
test_list.insert(-2,6)
print(test_list)

#요소 제거 : pop(), pop(위치)
test_list.pop(5)
print(test_list)
test_list.pop()     #마지막 요소 제거
print(test_list)

#모두 제거 : clear()
test_list.clear()
print(test_list)


### 튜플 tuple
#리스트 자료구조와 유사하지만 한 번 입력한 자료는 변경불가
#즉, 요소 추가는 가능/수정,삭제는 불가
#튜플은 ()을 이용해서
#튜플생성 시 단일 요소는 요소 뒤에 , 를 추가

t = [1, 2, 3]   #리스트
t = (1, 2, 3)   #튜플
t = (1, 'a', True)
t = (1)         #숫자
t = (1,)        #단일요소로 구성된 튜플

days = ('일', '월', '화', '수', '목', '금', '토')
print(days)         #요일을 튜플로 정의하고 출력

#수요일 출력
print(days[3])
print(len(days))
print(days[3:])

# days[3] = '水'       #튜플요소에 값 변경 - 불가!


##### 집합set
#저장된 데이터를 순서에 따라 관리하지 않고
#중복을 허용하지 않는 (unique) 자료구조
#집합은 {}을 이용
#집합의 개념에 따라 합/교/차집합이 지원

t = [1,1,1,1]
print(t)
t = (1,1,1,1)
print(t)
t = {1,1,1,1}
print(t)

t = [1,1,1,3,5,6,7,3,3,4,5,6,6,2,3,7,9]
print(t)
t = set( t )    #리스트를 집합으로 변환
print(t)

#집합 정의
#1월 중 교육받는 날을 집합으로 정의
edu = { 1,2,3,4,5,8,9,10,11,12 }

#집합의 기본적인 연산
동물 = {'사자','늑대','호랑이','얼룩말','기린'}
육상동물 = {'기린','여우','사슴','돼지'}
해상동물 = {'고래','상어','청새치','고등어'}
조류 = {'독수리','매','부엉이','올빼미'}

print(len(동물))      #길이
print('여우' in 육상동물)       #여우 검색 : in 연산자
print('여우' in 조류)           #여우 검색 : in 연산자
# print(동물[2])                  #인덱스 연산 : set에선 idx 안됨

print( 육상동물.union(해상동물))        #합집합
print( 육상동물 | 해상동물)        #합집합
육해상동물 = 육상동물 | 해상동물
print(육해상동물.intersection(육상동물))     #교집합
print(육해상동물.intersection(해상동물))     #교집합
print(육해상동물 & 육상동물)     #교집합

print(육해상동물.difference(육상동물))       #차집합
print(육해상동물.difference(해상동물))       #차집합
print(육해상동물 - 육상동물)       #차집합

print(육해상동물.symmetric_difference(육상동물))     #대칭차집합
print(육해상동물 ^ 육상동물)     #대칭차집합

#집합에서 제공하는 메서드
동물.add('인간')        #데이터 추가
print(동물)
동물.discard('인간')    #데이터 제거
print(동물)

해상동물.remove('고등어')  #데이터 제거
print(해상동물)

print(육상동물.pop())      #데이터 확인 후 제거
print(육상동물)

동물.clear()              #데이터 모두 제거
print(동물)


#### 패킹, 언패킹
# 패킹packing : 여러 데이터를 변수 하나에 묶어 담기
# 언패킹unpacking : 변수에 담긴 데이터를 여러 변수에 풀어 놓기

numbers = (1,2,3,4,5)       #튜플 생성 (packing)
a,b,c,d,e = numbers         #튜플에 저장된 데이터를 언패킹
print(c)

numbers = 1,2,3,4,5         #패킹 시 () 생략 가능

# x,y,z = numbers             #언패킹 시 데이터 수와 변수갯수가 일치 해야함

x,y,*z = numbers            #언패킹 시 변수 갯수 불일치 시 처리 방법

print(z)

a, b, c = 1, 2, 3           #변수 초기화에 패킹 언패킹 동시 적용

#연습문제 풀이
x = [1,2,3,4,5,6,7,8,9]

print(x)
x.append(10)            #요소 하나를 추가할 때
print(x)

x.extend([11,12])       #하나 이상 요소를 리스트에 추가
print(x)

x.remove(11)            #지정값으로 제거
x.remove(12)
print(x)

x.reverse()             #요소를 역순으로 배치
print(x)

print(x.pop())          #마지막요소 빼내고 빼낸 항목은 제거
print(x)

x = [1,5,6,2,3,4,10]    #정렬안된 리스트
print(x)
x.sort()                #리스트 정렬
print(x)


x.insert(-1, 7)          #10앞에 7을 삽입 .insert(index, 값)
print(x)

print(x.count(4))          #요소의 수

print(x.index(5))           #요소의 위치값 출력

z = { 1,1,1,2,2,3,3,3 }
print(z)                    #요소는 모두 3개

z.add(1)                    #의미 없는 코드
print(z)                    #어쨌든 3개


