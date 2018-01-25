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