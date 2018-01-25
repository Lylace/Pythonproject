import random

# 윤년여부
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isleap = '윤년이 아닙니다'
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        isleap = '윤년입니다'

    print('%d년은 %s' % (year,isleap))

# 복권발행
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

# 계산기(제곱연산 추가)
def intCal():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = '%d + %d = %d \n %d - %d = %d \n %d * %d = %d \n %d / %d = %.2f \n %d ^ %d = %d'
    print(fmt % (num1, num2, num1+num2, num1, num2, num1-num2, num1, num2, num1*num2,
                 num1, num2, num1 / num2,num1, num2, num1**num2, ))
    
# 리스트 중간값 짝수 일때는 중간 2개값    
def listcenter(list):
    size = len(list)
    mid = int(size/2)
    if size % 2 == 0:
        print(list[mid-1:mid+1])
    else:
        print(list[mid])


# 성적 데이터 클래스
class SungJukVO:

    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

# 성적 처리용 클래스
class SungJukService:

    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self, sj):
        avg = self.getTotal(sj) / 3
        return avg

    def getGrade(self, sj):
        gradelist = '가가가가가양미우수수'
        idx = int(self.getAverage(sj) / 10) - 1
        return gradelist[idx]