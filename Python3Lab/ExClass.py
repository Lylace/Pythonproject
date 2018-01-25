#클래스
#변수와 그에 관련된 함수를 하나의 이름으로 정의한 것
#클래스는 메서드, 속성, 클래스변수, 인스턴스변수로 구성
#생성자와 소멸자등의 멤버도 있음

#클래스 정의
#class 이름:
#   클래스변수
#   생성자
#   함수정의(메서드)

#파이썬에서는 생성자나 메서드 정의 시 암시적으로 첫번째 매개변수가
#self로 되어있음 self는 항상 객체 자기 자신을 가리키는 의미로 사용

#클래스의 멤버변수는 생성자를 통해서 정의
#파이썬에서는 객체로 생성된 후에도 멤버변수를 추가할 수 있음(비추)

class HelloPython:
    def sayHello(self):
        print('Hello, Python!!')

print(HelloPython)
print(type(HelloPython))

# HelloPython.sayHello()
py = HelloPython()
py.sayHello()

class Animal:
    type = '동물' #클래스수준 변수

    def __init__(self, name, age):     #객체 자신을 가리키는 의미로 self
        self.name = name
        self.age = age

    def eat(self):
        print('먹는다')

# 객체선언 및 사용 : 객체명.메서드
# tiger = Animal()
tiger = Animal('', 0)
tiger.eat()      #메서드 호출
print(tiger.type)       #인스턴스 변수
print(Animal.type)      #클래스 변수 (다른 클래스와 공유)

tiger.name = '호랑이'  #생성자를 통해 정의된 인스턴스 변수들
tiger.age = 13
tiger.gender = '수'

print(tiger.name)
print(tiger.age)
print(tiger.gender)

zebra = Animal('얼룩말', 6)
# print(zebra.gender)

#클래스의 상속
# class 클래스명(부모클래스명):
#       클래스정의
class Tiger(Animal):
    def eat(self):
        print('%s는 고기를 먹는다' % (self.name))

class Zebra(Animal):
    def eat(self):
        print('%s는 풀을 먹는다' % (self.name))

t1 = Tiger('호돌이',12)
print(t1.name)
t1.eat()

z1 = Zebra('얼루기', 5)
z1.eat()

animals = [t1, z1]  #객체지향의 다형성을 이용
for ani in animals:
    print(ani.name)
    ani.eat()

class SungJuk:

    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTotal(self):
        tot = self.kor + self.eng + self.mat
        return tot

    def getAverage(self):
        avg = self.getTotal() / 3
        return avg

    def getGrade(self):
        gradelist = '가가가가가양미우수수'
        idx = int(self.getAverage()/10)-1
        return gradelist[idx]
        # avg = self.getAverage()
        # grd = '가'
        # if avg >= 90:
        #     grd = '수'
        # elif avg >= 80:
        #     grd = '우'
        # elif avg >= 70:
        #     grd = '미'
        # elif avg >= 60:
        #     grd = '양'
        # return grd



sj = SungJuk('혜교',99,87,70)

print(sj.getTotal())
print(sj.getAverage())
print(sj.getGrade())

class SungJukVO:

    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


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


sj1 = SungJukVO('혜교',87,76,98)
sjsrv = SungJukService()

print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))
print(sjsrv.getGrade(sj1))