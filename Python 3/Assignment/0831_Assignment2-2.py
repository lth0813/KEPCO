bmenu = """
1.김밥 
2.돈까스 
3.분식
4.식사 
5.국밥 
6.사이드
7.세트 
8.결제

메뉴를 선택해주세요"""
smenu1 = """
1.원조김밥 2500원
2.참치김밥 3000원
3.모듬김밥 5000원
4.취소

주문을 선택해주세요
"""
smenu2 = """
1.돈까스 7000원
2.치즈돈까스 7500원
3.카레돈까스 8000원
4.취소

주문을 선택해주세요
"""
smenu3 = """
1.유부우동 5000원
2.쫄면 6000원
3.라볶이 5000원
4.취소

주문을 선택해주세요
"""
smenu4 = """
1.제육덮밥 6500원
2.김치볶음밥 6500원
3.돼지김치찌개 7000원
4.취소

주문을 선택해주세요
"""
smenu5 = """
1.육개장 7000원
2.설렁탕 7000원
3.부대찌개 7000원
4.취소

주문을 선택해주세요
"""
smenu6 = """
1.콜라 1000원
2.공기밥 1000원
3.계란찜 5000원
4.취소

주문을 선택해주세요
"""
smenu7 = """
1.돈까스 + 떡볶이 + 원조김밥 2줄 + 콜라 16000원
2.돈까스 + 떡볶이 + 쫄면 16000원
3.취소

주문을 선택해주세요
"""
menu_name = [['원조김밥','참치김밥','모듬김밥'],
             ['돈까스','치즈돈까스','카레돈까스'],
             ['유부우동','쫄면','라볶이'],
             ['제육덮밥','김치볶음밥','돼지김치찌개'],
             ['육개장','설렁탕','부대찌개'],
             ['콜라','공기밥','계란찜']]
menu_price = [[2500,3000,5000],
              [7000,7500,8000],
              [5000,6000,5000],
              [6500,6500,7000],
              [7000,7000,7000],
              [1000,1000,5000]]
conti_order = """
1.네
2.아니오
"""
order_list = [ ]
order_list_price = [ ]

while True:
    print(bmenu)
    total = sum(order_list_price)
    total_menu = ', '.join(order_list)
    last_order = """
주문하신 메뉴는 %s이며 현재 총 금액은 %d원입니다.
결제를 진행하시겠습니까?
""" %(total_menu, total)
    receipt = []
    receipt.append(order_list)
    receipt.append(order_list_price)
    cnt = 0
    choice = int(input())
    if choice == 1:
        print(smenu1)
    elif choice == 2:
        print(smenu2)
    elif choice == 3:
        print(smenu3)
    elif choice == 4:
        print(smenu4)
    elif choice == 5:
        print(smenu5)
    elif choice == 6:
        print(smenu6)
    elif choice == 7:
        print(smenu7)
    elif choice == 8:
        print(last_order)
        print(conti_order)
        ynchoice = int(input())
        if ynchoice == 1:
            print("""
결제 수단을 선택해주세요
1. 현금
2. 카드
""")
            ccchoice = int(input())
            if ccchoice == 1:
                print("""
현금을 투입해주세요
""")
                cash = int(input())
                if cash == total:
                    print("""
결제가 완료되었습니다
""")
                    order_list = [ ]
                    order_list_price = [ ]
                    print("""
영수증을 받으시겠습니까?

1. 네
2. 아니오
""")
                    rchoice = int(input())
                    if rchoice == 1:
                        a = list(map(str,receipt[1]))
                        print("""
메뉴명 : %s
각 가격 : %s원
총합 : %d원
"""%(",".join(receipt[0]),",".join(a),sum(receipt[1])))
                        receipt = [ ]
                        continue
                    elif rchoice == 2:
                        print("""
처음 화면으로 돌아갑니다.
""")
                        continue
                elif cash > total:
                    print("""
결제가 완료되었습니다
잔돈 %d원을 반환합니다.
""" %(cash - total))
                    order_list = [ ]
                    order_list_price = [ ]
                    print("""
영수증을 받으시겠습니까?

1. 네
2. 아니오
""")
                    rchoice = int(input())
                    if rchoice == 1:
                        a = list(map(str,receipt[1]))
                        print("""
메뉴명 : %s
각 가격 : %s원
총합 : %d원
"""%(",".join(receipt[0]),",".join(a),sum(receipt[1])))
                        receipt = [ ]
                        continue
                    elif rchoice == 2:
                        print("""
처음 화면으로 돌아갑니다.
""")
                        continue
                elif cash < total:
                    print("""
금액이 부족합니다. 투입 금액인 %d를 반환합니다.
처음 화면으로 돌아갑니다.
""" %cash)
                    continue
            elif ccchoice == 2:
                print("""
카드로 결제가 완료되었습니다. 카드를 챙겨주십시오
""") 
                order_list = [ ]
                order_list_price = [ ]
                print("""
영수증을 받으시겠습니까?

1. 네
2. 아니오
""")
                rchoice = int(input())
                if rchoice == 1:
                    a = list(map(str,receipt[1]))
                    print("""
메뉴명 : %s
각 가격 : %s원
총합 : %d원
"""%(",".join(receipt[0]),",".join(a),sum(receipt[1])))
                    receipt = [ ]
                    continue
                elif rchoice == 2:
                    print("""
처음 화면으로 돌아갑니다.
""")
                    continue
        elif ynchoice == 2:
            print("""
취소하였습니다. 처음화면으로 돌아갑니다.
""")
            continue
    elif choice == 9:
        break #잠시 멈추기 용도
    else:
        print("""
잘못된 입력입니다. 처음화면으로 돌아갑니다.
""")
        continue
    schoice = int(input())
    if choice == 1 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[0][0])
        order_list.append(menu_name[0][0])
        order_list_price.append(menu_price[0][0])
        continue
    elif choice == 1 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[0][1])
        order_list.append(menu_name[0][1])
        order_list_price.append(menu_price[0][1])
        continue
    elif choice == 1 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[0][2])
        order_list.append(menu_name[0][2])
        order_list_price.append(menu_price[0][2])
        continue
    if choice == 2 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[1][0])
        order_list.append(menu_name[1][0])
        order_list_price.append(menu_price[1][0])
        continue
    elif choice == 2 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[1][1])
        order_list.append(menu_name[1][1])
        order_list_price.append(menu_price[1][1])
        continue
    elif choice == 2 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[1][2])
        order_list.append(menu_name[1][2])
        order_list_price.append(menu_price[1][2])
        continue
    if choice == 3 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[2][0])
        order_list.append(menu_name[2][0])
        order_list_price.append(menu_price[2][0])
        continue
    elif choice == 3 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[2][1])
        order_list.append(menu_name[2][1])
        order_list_price.append(menu_price[2][1])
        continue
    elif choice == 3 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[2][2])
        order_list.append(menu_name[2][2])
        order_list_price.append(menu_price[2][2])
        continue
    elif choice == 3 and schoice == 4:
        print("취소하였습니다. 처음 화면으로 돌아갑니다.")
        continue
    if choice == 4 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[3][0])
        order_list.append(menu_name[3][0])
        order_list_price.append(menu_price[3][0])
        continue
    elif choice == 4 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[3][1])
        order_list.append(menu_name[3][1])
        order_list_price.append(menu_price[3][1])
        continue
    elif choice == 4 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[3][2])
        order_list.append(menu_name[3][2])
        order_list_price.append(menu_price[3][2])
        continue
    elif choice == 4 and schoice == 4:
        print("취소하였습니다. 처음 화면으로 돌아갑니다.")
        continue
    if choice == 5 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[4][0])
        order_list.append(menu_name[4][0])
        order_list_price.append(menu_price[4][0])
        continue
    elif choice == 5 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[4][1])
        order_list.append(menu_name[4][1])
        order_list_price.append(menu_price[4][1])
        continue
    elif choice == 5 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[4][2])
        order_list.append(menu_name[4][2])
        order_list_price.append(menu_price[4][2])
        continue
    elif choice == 5 and schoice == 4:
        print("취소하였습니다. 처음 화면으로 돌아갑니다.")
        continue
    if choice == 6 and schoice == 1:
        print("%s을(를) 선택하였습니다." %menu_name[5][0])
        order_list.append(menu_name[5][0])
        order_list_price.append(menu_price[5][0])
        continue
    elif choice == 6 and schoice == 2:
        print("%s을(를) 선택하였습니다." %menu_name[5][1])
        order_list.append(menu_name[5][1])
        order_list_price.append(menu_price[5][1])
        continue
    elif choice == 6 and schoice == 3:
        print("%s을(를) 선택하였습니다." %menu_name[5][2])
        order_list.append(menu_name[5][2])
        order_list_price.append(menu_price[5][2])
        continue
    elif choice == 6 and schoice == 4:
        print("취소하였습니다. 처음 화면으로 돌아갑니다.")
        continue
    if choice == 7 and schoice == 1:
        print("세트1을(를) 선택하였습니다.")
        order_list.append("세트1")
        order_list_price.append(16000)
        continue
    elif choice == 7 and schoice == 2:
        print("세트2을(를) 선택하였습니다.")
        order_list.append("세트2")
        order_list_price.append(16000)
        continue
    elif choice == 7 and schoice == 3:
        print("취소하였습니다. 처음 화면으로 돌아갑니다.")
        continue
    else:
        print("잘못된 입력입니다. 처음화면으로 돌아갑니다.")
        continue
