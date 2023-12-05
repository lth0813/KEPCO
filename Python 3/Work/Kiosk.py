Menu = {'김밥': {'원조김밥': 2500, '김치김밥': 3000, '참치김밥': 3000},     #k1, k2, k3
        '돈까스': {'돈까스': 7000, '더블돈까스': 9000, '치킨까스': 7500},   #f1, f2, f3
        '분식': {'유부우동': 5000, '쫄면': 6000, '라볶이': 5000},           #s1, s2, s3
        '식사': {'카레덮밥': 6000, '제육덮밥': 6500, '오므라이스': 6500},   #m1, m2, m3
        '국밥': {'갈비탕': 7000, '순대국': 7000, '부대찌개': 7000},         #g1, g2, g3
        '사이드메뉴': {'콜라(250ml)': 1000, '공기밥': 1000, '계란찜': 5000}} #side1, side2, side3

class MenuClass():
    def __init__(self, menu, price): #딕셔너리에서 메뉴와 가격을 저장하기 위한 
        self.menu = menu
        self.price = price

k1 = MenuClass('원조김밥', Menu['김밥']['원조김밥']) #k1 = menu는 원조김밥, price는 2500
k2 = MenuClass('김치김밥', Menu['김밥']['김치김밥'])
k3 = MenuClass('참치김밥', Menu['김밥']['참치김밥'])

f1 = MenuClass('돈까스', Menu['돈까스']['돈까스'])
f2 = MenuClass('더블돈까스', Menu['돈까스']['더블돈까스'])
f3 = MenuClass('치킨까스', Menu['돈까스']['치킨까스'])

s1 = MenuClass('유부우동', Menu['분식']['유부우동'])
s2 = MenuClass('쫄면', Menu['분식']['쫄면'])
s3 = MenuClass('라볶이', Menu['분식']['라볶이'])

m1 = MenuClass('카레덮밥', Menu['식사']['카레덮밥'])
m2 = MenuClass('제육덮밥', Menu['식사']['제육덮밥'])
m3 = MenuClass('오므라이스', Menu['식사']['오므라이스'])

g1 = MenuClass('갈비탕', Menu['국밥']['갈비탕'])
g2 = MenuClass('순대국', Menu['국밥']['순대국'])
g3 = MenuClass('부대찌개', Menu['국밥']['부대찌개'])

side1 = MenuClass('콜라(250ml)', Menu['사이드메뉴']['콜라(250ml)'])
side2 = MenuClass('공기밥', Menu['사이드메뉴']['공기밥'])
side3 = MenuClass('계란찜', Menu['사이드메뉴']['계란찜'])


def MenuPrint():
    for food in ['김밥', '돈까스', '분식', '식사']:
        print(f"|{food:*^13}", end=' ')
    print('|')

    print(f"| 1.{k1.menu:^10}| 7.{f1.menu:^10}|13.{s1.menu:^8}|16.{m1.menu:^10}|") #위에서 만든 클래스로 k1.menu는 원조김밥
    print(f"| 2.{k2.menu:^10}| 8.{f2.menu:^8}|14.{s2.menu:^10}|17.{m2.menu:^10}|")
    print(f"| 3.{k3.menu:^10}| 9.{f3.menu:^9}|15.{s3.menu:^9}|18.{m3.menu:^9}|")

    for food in ['국밥', '사이드']:
        print(f"|{food:*^13}", end=' ')
    print('|')

    print(f"| 4.{g1.menu:^10}|10.{side1.menu:^12}|")
    print(f"| 5.{g2.menu:^10}|11.{side2.menu:^11}|")
    print(f"| 6.{g3.menu:^9}|12.{side3.menu:^11}|")


class Kiosk():

    def __init__(self) -> None:     # admin, user, guest   사용자 / 필요요소를 담은 틀(O) #이거뭐임?
        self.total = 0
        self.money = 0
        self.history = [ ]  # [menu, price, quantity]
        self.cart_dic= {1: ('김밥', '원조김밥'), 7: ('돈까스', '돈까스'), 13: ('분식', '유부우동'), 16 : ('식사', '카레덮밥'),
                        2: ('김밥','김치김밥'), 8: ('돈까스', '더블돈까스'), 14: ('분식','쫄면'), 17 : ('식사', '제육덮밥'),
                        3: ('김밥', '참치김밥'), 9: ('돈까스', '치킨까스'), 15: ('분식', '라볶이'), 18 : ('식사', '오므라이스'),
                        4: ('국밥', '갈비탕'), 10: ('사이드메뉴', '콜라(250ml)'), 5: ('국밥','순대국'), 11 : ('사이드메뉴','공기밥'),
                        6: ('국밥', '부대찌개'), 12: ('사이드메뉴','계란찜')}
    
    #2주문받기
    def order(self, qty=0):                            #입력(X)
        while True:
            menu = input("메뉴 숫자를 입력하세요: ")    #메뉴선택
            if 0 < int(menu) and int(menu) <= 18:
                while True:
                    qty = input("주문 수량을 입력하세요: ") #주문수량
                    if 0 < int(qty):
                        break
                break

            if (not menu) or menu == '0': #not menu는 뭐지? 왜 int가 아닌 str 0 임?
                menu = '0'
                break
        return menu, qty                               # 출력(메뉴이름, 주문수량) #메뉴 1, qty 2
    
    def cart(self, menu, qty):                           # 입력(메뉴이름, 주문수량) #메뉴 1, qty 2
        (category, food) = self.cart_dic[int(menu)]      # self.cart_dic의 키 1(메뉴)의 밸류인 '김밥'과 '원조김밥'이 각각 category와 food로 들어감
        # if food in [ x[0] for x in self.history ]:    #만약 '원조김밥'이 [x의 0번값] [원조김밥, 2500, 1]
        for hist in self.history:                        #self.history는 빈 리스트 [ ]
            if hist[0] == food:                          #만약 hist의 첫번째 값이 위에서 입력된 food = '원조김밥'이라면
                hist[-1] = hist[-1] + int(qty) #수량추가    #hist의 마지막 값은 hist 마지막 값 + 본인이 적은 qty 수량 값이다.
                break
        else:                                              #for문에 else가 어떻게 작동함? #내일 물어보기
            self.history.append([ food, Menu[category][food], int(qty)])    #self.history에 food('원조김밥'), Menu의 category('김밥')안의 food('원조김밥')의 밸류인 2500, 그리고 입력한 수량

        self.total = self.total + (int(Menu[category][food]) * int(qty))    #self.total(0)은 0 + 위와 같이 2500 * 입력한 수량 = 2500
        print(self.history) # [원조김밥, 2500, 1]

    def cash_card(self):                                                  # 입력(X)
        while True:
            menu = input("==============\n==    결재선택    ==\n== [C]ash or car[D]  ==\n") #메뉴 = input
            if menu == 'c':
                self.money = int(input("돈을 입력하세요: "))               #현금결재시 금액입금 #self.money는 입력한 금액
                break
            elif menu == 'd':
                self.money = 0
                break
        return menu      #이거는 이상한거 쳤을때 다시 메뉴 보여주는거?       # 현금(c) / 카드(d)
    
    def receipt(self, select):                                            # 입력값: 현금(c) / 카드(d)
        if sum([ int(x[-2])*int(x[-1]) for x in self.history ]) == self.total : #self.history = ['원조김밥',2500,1]니까 2500 * 1이 되고 이게 self.total이랑 같으면?
            print("\n"*3)
            print("===================================================")
            print("=============     종합  영수증     ================")
            print("===================================================")
            for [menu, price, quantity] in self.history: #self.history = ['원조김밥',2500,1] #이거 작동 원리는?
                print(f"==  {menu:^10}  {price}원 X {quantity}개   {price*quantity:^8}원    ==")
            if select == 'c':
                print(f"==             입금 : {self.money:^12}원             ==") #self.money는 내가 입력한 금액 2500
            print(f"==             총액 : {self.total:^12}원             ==") #self.total은 2500
            if select == 'c':
                print(f"==             잔액 : {self.money-self.total:^12}원             ==") #2500 - 2500 = 0원
            print("===================================================")
        else:
            print("총 금액 오류입니다!!!")


        
run = Kiosk()

#1 메뉴출력
MenuPrint()
#2 주문받기
while True:
    (menu, qty) = run.order() #이게 뭐임?
    if menu == '0':
#3 결재선택
        select = run.cash_card() #이건 뭐임?
#4 영수증출력
        run.receipt(select)
        break
    run.cart(menu, qty) #주문 뭐 했는지 보여주는 거
