    #이름 짓기
    #파스칼 표기법 : 첫 단어를 대문자로 시작하여 이름을 지음
    #               ex) Employees, Departments, JoinMember
    #카멜 표기법 : 첫 단어를 소문자로 시작하여 이름을 지음
    #               ex) registerEmployee, joinMember
    #스네이크 표기법 : 소문자와  _기호를 이용해서 이름을 지음
    #               ex) register_employee, join_member
    #헝가리안 표기법 : 자료형을 의미하는 접두사를 이용해서 이름을 지음
    #               ex) strName, isMarried, boolMarried

# 지금까지의 예제를 함수로 작성
# Qna8, 10, 11, 12, 17, 18, 19, 20

import random

    #8
def compareRoom(width, height, price):
    return (width * height) / price

roomA = compareRoom(2.5, 3, 27)
roomB = compareRoom(4, 2, 30)

if roomA > roomB :
    print('방A가 나아요')
else:
    print('방B가 나아요')

    #10
def computeProfit():
    c = int(input('불변자본을 입력하세요'))
    v = int(input('가변자본을 입력하세요'))
    s = int(input('잉여가치액을 입력하세요'))
    #Constant capital, Variable capital, Surplus value

    return s / ( c + v )

print(computeProfit())

    #11
def getExchangeRate(country):
    if country.lower == 'usa':
        return 1070
    elif country.lower == 'euro':
        return 1319

buyUS = 780 * getExchangeRate('usa')
buyEuro = 650 * getExchangeRate('euro')

if buyUS > buyEuro:
    print('유로화로 구입하는게 더 싸요')
else:
    print('달러로 구입하는게 더 싸요')

    #12
def howManyRun(radius):
    pi = 3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생A는 학생B보다 %dM만큼 더 뜀' % (studentA - studentB))

    # 17
def intCal():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = '%d + %d = %d \n %d - %d = %d \n %d * %d = %d \n %d / %d = %.2f \n %d ^ %d = %d'
    print(fmt % (num1, num2, num1+num2, num1, num2, num1-num2, num1, num2, num1*num2,
                 num1, num2, num1 / num2,num1, num2, num1**num2, ))

intCal()

    #18
def computeTax():
    결혼 = input('결혼하셨습니까?(예/아니오)')
    연봉 = int(input('연봉이 얼마입니까?'))
    fmt = '연봉 : %d, 결혼여부 : %s 세금 : %.2f'
    if 결혼 == '아니오':
        if 연봉 < 3000:
            print(fmt % (연봉,결혼,연봉 * 0.1))
        else:
            print(fmt % (연봉,결혼,연봉 * 0.25))
    elif 결혼 == '예':
        if 연봉 < 6000:
            print(fmt % (연봉,결혼,연봉 * 0.1))
        else:
            print(fmt % (연봉,결혼,연봉 * 0.25))

computeTax()

    #19
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isleap = '윤년이 아닙니다'
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        isleap = '윤년입니다'

    print('%d년은 %s' % (year,isleap))

isLeapYear()

    #20
def rouletteLotto():
    lotto = str(random.randint(100,999))
    print(lotto)
    lucky = input('3자리 복권 숫자를 입력하세요(100~999) ')
    match = 0

    for i in [0,1,2]:
        if lotto[i] == lucky[i]:
            match += 1
        elif lotto[i] != lucky[i]:
            match += 0

    if match == 0:
        print('아쉽군요 꽝입니다')
    elif match == 1:
        print('1개 일치하셨습니다 상금 1천 입니다!')
    elif match == 2:
        print('2개 일치하셨습니다 상금 1만 입니다!')
    else:
        print('모두 일치하셨습니다 상금 1백만 입니다!')

rouletteLotto()