#03장 if문 - p.121
money = False
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')
#비교 연산자 - > , < , == , != , >= , <=
#논리 연산자 - or , and , not / (조건) or (조건) , (조건) and (조건) , not (조건)
    # a = 8; b = 5
    # if ((a == 8) or (b == 4)):

#문자열도 대소비교 가능(아스키코드)
print('a' < 'b')

#문자열을 비교할땐 길이로 하는 편
print(len('임태환') >= len('채현수'))

#p.129 1분코딩
pocket = ['paper', 'cellphone', 'money','card']
if 'card' not in pocket:
    print('걸어가라')
else:
    print('버스를 타고 가라')

#elif
money = 2500
pocket = ['paper', 'cellphone', money, 'card']
if (money in pocket) and (money >= 6000): #택시 - card(o) or money >= 6000
    print('택시를 타고 가라')
elif ('card' in pocket) or (1600 <= money < 6000): #버스 - card(o) or 1600 <= money < 6000
    print("버스를 타고 가라")
else:
    print("걸어간다")
#조건을 역으로 - 특정 조건을 먼저 배제하고 작업하는 것이 더 유용할 때도 있다.
if ('card' not in pocket) and (money < 1600):
    print('걸어간다')
elif (money < 6000):
    print('버스를 타고 간다')
else:
    print('택시를 타고 간다')
#'money'를 문자열으로 먼저 T/F를 파악한 뒤 money(int열)을 변수로 쓰는 것도 가능.

#변수명 / 변수명() - 함수명, 클래스명
#남이 쉽게 식별하게 할 수 있도록 하고, 재귀함수 및 3중 for문은 가급적 쓰지 않도록 하자.
