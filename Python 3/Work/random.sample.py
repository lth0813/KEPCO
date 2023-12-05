# random.sample()을 구현해보자
import random
def randomsample():
    a_list = [ ] ; bonus_n = [ ]
    while len(a_list) < 7:
        number = random.randint(1, 45)
        if number not in a_list:
            a_list.append(number)
        else:
            print("작동확인")
            continue
    bonus_n.append(a_list.pop())
    a_list.sort()
    print("이번주 당첨번호는",a_list,", 보너스 번호는 %d입니다." %bonus_n[0])
randomsample()
