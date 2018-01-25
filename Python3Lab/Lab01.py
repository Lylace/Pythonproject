    #1 print()를 이용하여 다음 내용을 출력
print('#1')
print('☆   ☆    ☆☆    ☆☆☆☆    ☆☆☆☆   ☆   ☆')
print('☆   ☆   ☆  ☆   ☆   ☆   ☆   ☆  ☆   ☆')
print('☆☆☆☆☆  ☆    ☆  ☆☆☆☆    ☆☆☆☆    ☆ ☆')
print('☆   ☆  ☆☆☆☆☆☆  ☆   ☆   ☆   ☆    ☆')
print('☆   ☆  ☆    ☆  ☆    ☆  ☆    ☆   ☆')

    #2
print('#2')
name = '선창훈'
weight = 66
age = 28
print(name, weight, age)

    #3
print('#3')
x, y, z=1, 1, 1
print(3 * x)
print(3 * x + y)
print((x+y)/7)
print((3*x+y)/(z+2))

    #4
print('#4')
x,y = 4,8
x *= y
print(x,y)
x -= y
print(x,y)

    #5
print('#5')
x = 3
print(x+7 == 10)

    #6
print('#6')
print((-32 + 95) * 12 / 3)
print((3*4 - ((-27 + 67)/4))**8)
print((512+1968-432)/2**4 + 128)
print(256 == 2**8)
print(50+50 <= 10*10)
print(99 != 10**2 -1)

    #7
print('#7')
x, y, m, n=2.5, -1.5, 18, 4
print(x + n * y - (x+n) * y)
print(m/n + m%n)
print(5*x - n/5)
print(1-(1-(1-(1-(1-n)))))

    #8
print('#8')
a = (2.5 * 3) /28
b = (4*2) / 30
print(a>b)

    #9
print('#9')
print(3+4.5*2+27/8)
print(True or False and 3<4 or not(5==7))
print(True or (3 < 5 and 6 >= 2))
# print(not True > 'A')         # 문자에 비교연산자
# print(7 % 4 + 3 - 2 / 6 * 'Z') # 문자에 산술연산자
# print('D' + 1 + 'M' % 2 / 3)  # 문자에 산술연산자
print(5.0 / 3 + 3 / 3 )
print(53%21 < 45/18)
print((4 < 6) or True and False or False and (2>3))
print(7 - ( 3 + 8 * 6 + 3) - ( 2 + 5 * 2))

    #10
print('#10')
가변자본 = 15
불변자본 = 30
잉여가치 = 45
이윤율 = 잉여가치 / (불변자본 + 가변자본)
print(이윤율)

    #11
print('#11')
달러노트북 = 780 * 1070
유로노트북 = 650 * 1309
print('달러노트북 %d, 유로노트북 %d' % (달러노트북, 유로노트북))

    #12
print('#12')
pi = 3.14
바깥학생 = pi * 100
안쪽학생 = pi * 90
distance = 바깥학생 - 안쪽학생
print(distance,'미터')

    #13
print('#13')
print("Check out this line ")
# print("//hello there "+ '9'+ 7)

    #16
#파이썬에서는 기본적으로 ++, --는 지원X
n = 3
print(++n)     # +(+n)
print(--n)     # -(-n)
n += 1
print(n)

    #17
print('*** 사칙연산 프로그램 ***')
num1 = int(input('첫번째 정수를 입력하세요'))
num2 = int(input('두번째 정수를 입력하세요'))

print('%d + %d = %d' % (num1,num2,num1+num2))
print('%d - %d = %d' % (num1,num2,num1-num2))
print('%d * %d = %d' % (num1,num2,num1*num2))
print('%d / %d = %.1f' % (num1,num2,num1/num2))


# 난수 생성
import random
print(random.random())  # 0 ~ 1 사이 실수float 출력

print(random.randint(1,10)) #지정한 범위의 정수int 출력