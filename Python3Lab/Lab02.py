#     #18
# print('***세금 계산기***')
# 결혼 = input('결혼하셨습니까?(예/아니오)')
# 연봉 = int(input('연봉이 얼마입니까?'))
# msg = '납부해야할 세금은 %d 만원입니다.'
# if 결혼 == '아니오':
#     if 연봉 < 3000:
#         print(msg % (연봉 * 0.1))
#     else:
#         print(msg % (연봉 * 0.25))
# elif 결혼 == '예':
#     if 연봉 < 6000:
#         print(msg % (연봉 * 0.1))
#     else:
#         print(msg % (연봉 * 0.25))
#
#     #19
# print('***윤년 여부 판독기***')
# year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('%d년은 윤년입니다' % (year))
# else:
#     print('%d년은 윤년이 아닙니다' % (year))
#
#
    #20
# print('*** 3자리 복권 맞추기 ***')
# import random
# lotto = str(random.randint(100,999))
# print(lotto)
# lucky = input('3자리 복권 숫자를 입력하세요(100~999) ')
# match = 0
#
# for i in [0,1,2]:
#     if lotto[i] == lucky[i]:
#         match += 1
#     elif lotto[i] != lucky[i]:
#         match += 0
#
# if match == 0:
#     print('아쉽군요 꽝입니다')
# elif match == 1:
#     print('1개 일치하셨습니다 상금 1천 입니다!')
# elif match == 2:
#     print('2개 일치하셨습니다 상금 1만 입니다!')
# else:
#     print('모두 일치하셨습니다 상금 1백만 입니다!')

#     #21
# print('*** 구구단 출력기 ***')
# dan = input('보고 싶은 단수를 입력하세요(1~9) ')
# if ord('1') <= ord(dan[0]) and ord(dan[0]) <= ord('9'):
#     for i in range(1,10):
#         print('%d X %d = %d' % (int(dan), i, int(dan)*i))
# else:
#     print('잘못 입력하셨습니다!!')


#     #22
# print('***대문자 출력기***')
# val = input('소문자를 입력하세요(a~z) ')
# if ord('a') <= ord(val[0]) and ord(val[0]) <= ord('z'):
#     print(val.upper())
# else:
#     print('잘못 입력하셨습니다notnot')

    #23
print('***숫자 맞추기 게임***')
import random
num1 = int(input('숫자를 입력하세요(1~100) '))
num2 = random.randint(1,100)
print(num2)
while num1 != num2:
    num1 = int(input('숫자를 입력하세요(1~100)'))
    if num1 < num2:
        print('추측한 숫자가 작습니다')
    elif num1 > num2:
        print('추측한 숫자가 큽니다')
print('빙고not 숫자를 맞췄습니다')

#     #24
# print('            Multiplication Table')
# print('        1   2   3   4   5   6   7   8   9')
# print('-----------------------------------------')
# for i in range(1, 10) :
#     if i != 1:
#         print('')
#     print('%d  | ' % (i), end="")
#     for j in range(1, 10):
#         print('  %2d' % (i*j), end="")
#
#     #25
# print('***신용카드 정보 조회***')
# pInput = input('카드번호를 입력해주세요')
# if pInput[0,1] == '35':
#     if pInput
