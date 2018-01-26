#30

i = 100
tot = 0

while True:
    if i % 5 == 0:
        tot += i
        i += 1
    elif i >= 10000:
        print(tot)
        break
    else:
        i += 1


#34






#43
def myRange(start, end, hop = 1):
    retVal = start
    while retVal <= end:
        yield retVal
        retVal += hop

hap = 0
# for i in myRange(1, 5, 2):      #종료값이 포함된 range 함수 작성
                                  #결국, 리스트 형태의 값이 출력
# for i in range(1, 5 ,2):        #i : 1, 3
for i in [1, 3, 5]:               #i : 1, 3, 5
    hap += i
print(hap)

def myRange2(start, end, hop = 1):
    retVal = start
    while retVal <= end:
        yield retVal        #실행 중에 계산된 값은
                            #generator 타입에 저장해 둠
        retVal += hop

a = myRange2(1,5,2)         #yield로 넘긴 데이터는 순환형식의 generator 타입 생성
print(a)
print(next(a))              #generator 타입에 저장된 값은
print(next(a))              #iterator형식으로 다룰 수 있음
print(next(a))              #iterator는 리스트에 저장된 객체를
                            #순환하며 하나씩 꺼내 사용하는 자료구조


for i in a:                 #generator 타입에 저장된 값은
    print(i)                #for문으로도 출력 가능

def myRange3(start, end, hop = 1):
    retVal = start
    val_list = []
    while retVal <= end:
        # yield retVal
        # return retVal ??        #중간 계산결과를 출력 또는 처리
        val_list.append(retVal)
        retVal += hop

    return val_list



hap2 = 0

for i in myRange3(1,5,2):
    hap2 += i
print(hap2)