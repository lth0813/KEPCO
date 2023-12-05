#주말동안 해봅시다!
    #스마트 알람을 개발하는 것을 목표로 해서 나의 일과를 print문으로 작성해본다.
    #작성한 내용 중에서 조건식 구현가능(True/False)구별이 가능한 내용과 그렇지 않은 내용을 구별해본다.
        #ex) 나는 %d를 %s개 먹었다. 나는 몇시에 배가 고프다. (True/False)
#정보
평일 = True
#기상 & 조식 - 7시 30분 기상해서 알람 스위치를 끄고 식사하러 간다. 기상하지 못했을 경우 알람을 10분 뒤로 맞추고 더 잔다.
hour = 7
minu = 30
기상 = False #기상했다면 True , 그렇지 않으면 False
알람 = False  #알람이 켜져있다면 True, 꺼져있다면 False
#기상을 했으나, 알람을 끄지 않은 경우는 고려하지않음.
if 평일:
    if 기상 and 알람 == False:
        print("아침 식사를 하러간다.")
    else:
        while hour >= 7 and minu != 30 or 알람 == False:
            minu = minu +10
            알람 = True
            print('%s분 뒤로 알람을 맞추고 더 잔다.' %10)
            if minu >= 60:
                hour = hour + 1
                minu = 0
            if hour == 8 and minu == 30:
                print('강제로 몸을 일으킨다.')
else:
    print('늦잠을 잔다.')
#오전 수업(평일)
if 평일:
    print('나는 %0.2f시 부터 %0.2f시 까지 오전 수업을 듣는다.' %(9.00,13.00))
else:
    print('방에서 자습한다.')
#중식
print('나는 %0.2f시 부터 %0.2f시 까지 점심 식사를 한다.' %(13.00,14.00))
#오후 수업(평일)
if 평일:
    print('나는 %0.2f시 부터 %0.2f시 까지 오후 수업을 듣는다' %(14.00,17.00))
else:
    print('방에서 자습한다.')
#석식 - 오늘 저녁 메뉴는 맛있다 or 맛이 없고 수중에 돈이 %s만큼 있다.
money = 10000
Tasty = True #맛있다면 True, 그렇지 않다면 False
if Tasty:
    print("식당에서 저녁을 먹는다.")
else:
    if money >= 10000:
        print("밖에 나가서 다른 것을 사 먹는다.")
    else:
        print("편의점에 가서 컵라면을 먹는다.")
#자습 - 오늘 수업 내용을 완벽하게 이해하였다. 
이해 = True #이해하였다면 True, 그렇지 않다면 False
if 평일:
    if 이해:
        print("%s 위주로 공부한다." %"예습")
    else:
        print("%s 위주로 공부한다." %"복습")
else:
    print("주중 내용을 복습하고 다음 내용을 예습한다.")
#취침 - 아직 공부해야할 내용이 남았다.
내용 = True #내용이 남았다면 True, 그렇지 않다면 False
시간 = 0
if 내용:
    while 시간 < 2:
        시간 = 시간 + 1
        print('조금 더 공부한다')
        if 시간 == 2:
            print('내일을 위해 자러간다.')
else:
    print('%s시까지 공부한 뒤 취침한다' %12)
