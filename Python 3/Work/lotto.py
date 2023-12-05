#로또 프로그램 
"1.구매"
"2.당첨금 확인"
"3.추첨"
import random
bonus = []
class lottery():
    def __init__(self):
        self.lotto = [ ]
        self.a_number = [ ]
        self.first_cnt = 0
        self.second_cnt = 0
        self.third_cnt = 0
        self.fourth_cnt = 0
        self.fifth_cnt = 0
        self.bag = [ ]
        self.check_list = [ ]
#첫화면
    def start(self):
        startmenu = int(input("1.구매하기\n2.현재 가지고 있는 복권 확인하기\n3.추첨하기\n4.당첨 확인하기\n5.당첨금 확인하기\n0.초기화\n"))
        if startmenu == 1:
            self.buy()
        elif startmenu == 2:
            print("총 %d장\n" %len(self.bag),self.bag)
        elif startmenu == 3:
            self.shuffle()
        elif startmenu == 4:
            self.check()
        elif startmenu == 5:
            self.money()
        elif startmenu == 0:
            self.bag = [ ]; self.first_cnt = 0; self.second_cnt = 0; self.third_cnt = 0; self.fourth_cnt = 0; self.fifth_cnt = 0; self.total_price = 0; self.ott_money = 0
#구매 - 원하는 수량(최대5 추가하기)
    def buy(self):
        auto = int(input("1.자동\n2.수동\n"))
        qty = int(input("구매하려는 수량을 입력하세요(최대5): "))
        for _ in range(qty):
            if auto == 1:
                a_list = list(range(1,46))
                self.lotto = random.sample(a_list, 6)
                self.lotto.sort()
                # print("발권되었습니다.")
                # print(self.lotto)
                self.bag.append(self.lotto)
            if auto == 2:
                print("1~45의 숫자 6개를 중복없이 띄어쓰기(공백)으로 구분하여 입력해주세요: ")
                self.lotto = [*map(int,input().split())]
                self.lotto.sort()
                # print("발권되었습니다.")
                # print(self.lotto)
                self.bag.append(self.lotto)
#추첨
    def shuffle(self):
        self.a_number = random.sample(list(range(1,46)), 7)
        bonus.append(self.a_number.pop())
        self.a_number.sort()
        print("이번 회차 당첨번호는",self.a_number,"입니다.")
        print("보너스 번호는",bonus[0],"입니다.")
#당첨확인 - bag [[],[],[]]
    def check(self):
        for i in self.bag: #i는 로또 한장
            for j in i: #j는 로또 한장의 숫자
                if j in self.a_number:
                    self.check_list.append("O")
                elif j in bonus:
                    self.check_list.append("B")
            if len(self.check_list) == 6 and "B" not in self.check_list:
                self.first_cnt += 1
                # print("1등")
            elif len(self.check_list) == 6 and "B" in self.check_list:
                self.second_cnt += 1
                # print("2등")
            elif len(self.check_list) == 5 and "B" not in self.check_list:
                self.third_cnt += 1
                # print("3등")
            elif len(self.check_list) == 4 and "B" not in self.check_list:
                self.fourth_cnt += 1
                # print("4등")
            elif len(self.check_list) == 3 and "B" not in self.check_list:
                self.fifth_cnt += 1
                # print("5등")
            # else:
            #     # print("낙첨되었습니다.")
            self.check_list = [ ]
#당첨금 지급
    def money(self):
        self.total_price = len(self.bag) * 1000
        print("총 판매액 %d원" %self.total_price)
        print("판매자 수익 %d원" %(self.total_price/2))
        print("5등 당첨자 수 %7d명, 5등 당첨금 : 총 %15d원" %(self.fifth_cnt,self.fifth_cnt*5000))
        print("4등 당첨자 수 %7d명, 4등 당첨금 : 총 %15d원" %(self.fourth_cnt,self.fourth_cnt*50000))
        self.ott_money = int((self.total_price/2) - (self.fifth_cnt*5000+self.fourth_cnt*50000))
        #Zerodivision error, if self.third_cnt == 0: %d는 0 당첨금은 총으로 계산 1~3등 반복
        if self.third_cnt == 0:
            print("3등 당첨자 수 %7d명, 3등 당첨금 : 각 %15d원" %(0,0))
        else:
            print("3등 당첨자 수 %7d명, 3등 당첨금 : 각 %15d원" %(self.third_cnt,((((self.ott_money/2)*0.125)/self.third_cnt))))
        if self.second_cnt == 0:
            print("2등 당첨자 수 %7d명, 2등 당첨금 : 각 %15d원" %(0,0))
        else:
            print("2등 당첨자 수 %7d명, 2등 당첨금 : 각 %12d원" %(self.second_cnt,((((self.ott_money/2)*0.125)/self.second_cnt))))
        if self.first_cnt == 0:
            print("1등 당첨자 수 %7d명, 1등 당첨금 : 각 %12d원" %(0,0))
        else:
            print("1등 당첨자 수 %7d명, 1등 당첨금 : 각 %12d원" %(self.first_cnt,((((self.ott_money/2)*0.75)/self.first_cnt))))
run = lottery()
while True:
    run.start()
