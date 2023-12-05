o_cate = ['    김밥    ','   돈까스   ','    분식    ','    식사    ','    국밥    ','   사이드   ','   세트   ']
o_menu = [[' 1.원조김밥 ','  4.돈까스  ',' 7.유부우동 ',' 10.제육덮밥',' 13.육개장  ','  16.콜라   ',' 19.세트1 '], #0 . 0 ~ 6
        [' 2.참치김밥 ','5.치즈돈까스','   8.쫄면   ',' 11.볶음밥  ',' 14.설렁탕  ',' 17.공기밥  ',' 20.세트2 '],   #1 . 0 ~ 6
        [' 3.모듬김밥 ','6.카레돈까스','  9.라볶이  ',' 12.김치찌개',' 15.부대찌개',' 18.계란찜  ','          ']]   #2 . 0 ~ 6
#메뉴판 정렬용
cate = [i.strip() for i in o_cate]
menu_name = [list(i.strip() for i in o_menu[0]),list(j.strip() for j in o_menu[1]),list(k.strip() for k in o_menu[2])]
#정렬용에서 공백 지우기
menu = [[1,4,7,10,13,16,19],[2,5,8,11,14,17,20],[3,6,9,12,15,18]]
price = [[2500, 7000, 5000, 6500, 7000, 1000, 16000],
         [3000, 7500, 6000, 6500, 7000, 1000, 16000],
         [5000, 8000, 5000, 7000, 7000, 5000]]
cart = { } ; cart_p = { }
last_order = [ ] ; last_quantity = [ ] ; last_price = [ ] ; total_price = [ ]
while True:
    for i in range(7):
        print("{0:^7}".format(o_cate[i]), end='|')
    print()
    for i in range(3):
        for j in range(7):
            print("{0:^7}".format(o_menu[i][j]),end='|')
        print()
    print()
    print("원하시는 메뉴의 번호를 선택해주세요:",end='')
    m_choice = int(input())
    while m_choice > 0:
        print("주문하신 메뉴의 수량을 입력해주세요:",end='')
        q_choice = int(input())
        break
    while True:
        if m_choice in menu[0]:
            order = menu[0].index(m_choice)
            if menu[0][order] not in cart:
                cart[menu[0][order]] = [menu_name[0][order]],[price[0][order]]
                cart_p[menu[0][order]] = [q_choice]
            else:
                quantity = cart_p[menu[0][order]]
                quantity.append(q_choice)
        elif m_choice in menu[1]:
            order = menu[1].index(m_choice)
            if menu[1][order] not in cart:
                cart[menu[1][order]] = [menu_name[1][order]],[price[1][order]]
                cart_p[menu[1][order]] = [q_choice]
            else:
                quantity = cart_p[menu[1][order]]
                quantity.append(q_choice)
        elif m_choice in menu[2]:
            order = menu[2].index(m_choice)
            if menu[2][order] not in cart:
                cart[menu[2][order]] = [menu_name[2][order]],[price[2][order]]
                cart_p[menu[2][order]] = [q_choice]
            else:
                quantity = cart_p[menu[0][order]]
                quantity.append(q_choice)
        break
    if m_choice == 0: #주문 목록 확인 및 결제(영수증)
        print("주문목록")
        for j in range(len(cart.keys())): #만약 3이라면 j는 0 1 2
            order = list(cart.keys()) #[1,2,5]
            last_order.append(cart[order[j]]) #last_order는 빈 리스트 [ ]
            last_quantity.append(sum(cart_p[order[j]]))
        for k in range(len(cart.keys())): #2 : 0,1
            print("%s" %''.join(last_order[k][0]),"%s원" %''.join(map(str,last_order[k][1])),"%d개" %last_quantity[k]) #주문서 형식
            last_price.append(last_order[k][1][0])
            total_price.append(last_price[k]*last_quantity[k])
        print("총 금액 : %d원" %sum(total_price))
        print()
        print("결제 수단을 선택해주세요.\n현금 : [C]ash\n카드 : Car[D]")
        while True: #결제 과정
            ynchoice = str(input())
            if ynchoice == "C":
                print("현금을 투입해주세요")
                cash = int(input())
                if cash == sum(total_price):
                    print("결제가 완료되었습니다")
                    for k in range(len(cart.keys())): #영수증
                        # print("{0:^7}".format(o_menu[i][j]),end='|')
                        print("%-6s" %"".join(last_order[k][0]),"{0:>8}".format(("%s원" %"".join(map(str,last_order[k][1])))),"%d개" %last_quantity[k])
                    print("{0:>30}".format("총 금액 : %d원") %sum(total_price))
                    #장바구니 리셋
                    cart = { } ; cart_p = { } ; last_order = [ ] ; last_quantity = [ ] ; last_price = [ ] ; total_price = [ ]
                elif cash > total_price[0]:
                    print("결제가 완료되었습니다.\n잔돈 %d원을 챙겨가세요." %(cash - sum(total_price)))
                    for k in range(len(cart.keys())): #영수증
                        print("%s" %''.join(last_order[k][0]),"%s원" %''.join(map(str,last_order[k][1])),"%d개" %last_quantity[k])
                    print("총 금액 : %d원" %sum(total_price))
                    cart = { } ; cart_p = { } ; last_order = [ ] ; last_quantity = [ ] ; last_price = [ ] ; total_price = [ ]
                elif cash < total_price[0]:
                    print("금액이 부족합니다. 투입 금액인 %d를 반환합니다.\n처음 화면으로 돌아갑니다." %cash)
                break
            elif ynchoice == "D":
                print("결제가 완료되었습니다. 카드와 영수증을 챙겨가세요")
                for k in range(len(cart.keys())): #영수증
                        print("%s" %''.join(last_order[k][0]),"%s원" %''.join(map(str,last_order[k][1])),"%d개" %last_quantity[k])
                print("총 금액 : %d원" %sum(total_price))
                cart = { } ; cart_p = { } ; last_order = [ ] ; last_quantity = [ ] ; last_price = [ ] ; total_price = [ ]
                break
            elif ynchoice != "C" and ynchoice != "D":
                print("잘못선택하였습니다. 다시 선택해주세요")
                continue
