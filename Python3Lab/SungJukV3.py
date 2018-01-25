# 성적 계산 프로그램 V3
# 이름name, 국어kor, 영어eng, 수학mat, 총점tot, 평균avg, 학점grd
# getTotal, getAverage, getGrade
# 리스트 자료구조를 이용한다
name_list = []
kor_list = []
eng_list = []
mat_list = []

tot_list = []
avg_list = []
grd_list = []

fmt = '이름 : %s, 국어 : %d, 영어 : %d, 수학 : %d, 총점 : %d, 평균 : %.2f, 학점 : %s'


def getTotal_list(i):
    tot = kor_list[i] + eng_list[i] + mat_list[i]
    return tot

def getAverage_list(i):
    avg = getTotal_list(i)/3
    return avg

def getGrade_list(i):
    avg = getAverage_list(i)
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return grd

print('-- 성적 처리 프로그램 v3 --')
# i = 0
while True:
    idx = len(name_list)

    name_list.append(input('이름을 입력하세요 '))
    kor_list.append(int(input('국어점수를 입력하세요 ')))
    eng_list.append(int(input('영어점수를 입력하세요 ')))
    mat_list.append(int(input('수학점수를 입력하세요 ')))

    tot_list.append(getTotal_list(idx))
    avg_list.append(getAverage_list(idx))
    grd_list.append(getGrade_list(idx))

    print('지금 입력된 점수입니다')
    print(fmt % (name_list[idx], kor_list[idx], eng_list[idx], mat_list[idx], tot_list[idx], avg_list[idx], grd_list[idx]))

#     user_input = input('''그만하시려면 q를, 지금까지 입력된 자료를
# 보려면 a를, 추가 입력 하시려면 0을 입력하세요''')

    # if user_input[0].lower() == 'q':
    #     break
    # elif user_input[0].lower() == 'a':
    #     print('지금까지 입력된 자료들입니다')
    #     for j in range(0,i+1):
    #         print(fmt % (name_list[j], kor_list[j], eng_list[j], mat_list[j], tot_list[j], avg_list[j], grd_list[j]))
    # else:
    #     i += 1

    is_exit = input('계속 하시겠습니까?(y/n) ')
    if is_exit == 'n':
        print(idx+1, '명의 학생의 성적이 입력되었습니다.')
        break

print('프로그램 종료')
