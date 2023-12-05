#자판기 만들어보기
# 1. 돈을 투입한다. 2. 메뉴를 보여주고 선택한다. 3. 돈이 초과하면 음료주고 잔돈 반환. 4. 돈이 딱 맞으면 음료 주기. 5. 돈이 모자라면 잔돈 반환.
# 3 - 1 음료 개수가 모자라면 품절 표시 후 잔돈 반환.

coffee = 4 #600원
coke = 4 #900원
while True:
    menu = """
1. 커피 - 600원
2. 콜라 - 900원
3. 선택안함
4. 자판기 종료

현재 잔량 : 커피 %d개, 콜라 %d개

메뉴를 선택해주세요""" %(coffee, coke)
    if coffee == 0 and coke == 0:
        print("현재 모든 물품이 품절입니다. 자판기를 종료합니다.")
        break
    else:
        if coffee == 0:
            menu = """
1. 커피 - 600원 (품절)
2. 콜라 - 900원
3. 선택안함
4. 자판기 종료

현재 잔량 : 커피 %d개, 콜라 %d개

메뉴를 선택해주세요""" %(coffee, coke)
        if coke == 0:
            menu = """
1. 커피 - 600원
2. 콜라 - 900원 (품절)
3. 선택안함
4. 자판기 종료

현재 잔량 : 커피 %d개, 콜라 %d개

메뉴를 선택해주세요""" %(coffee, coke)
    print(menu)
    choice = int(input())
    if choice == 3:
            print("선택 시간이 초과되었습니다. 다시 선택해주세요.") 
            continue
    if choice == 4:
            print("자판기를 종료합니다.")
            break
    print("""
돈을 투입해주세요.""")
    cash = int(input())
    if choice == 1 and coffee == 0:
            print("커피는 현재 품절 상태입니다. 잔돈 %d원을 반환합니다" %cash)
    elif choice == 1 and cash > 600:
            coffee = coffee - 1
            print("주문하신 커피 나왔습니다. 잔돈 %d원을 반환합니다." %(cash - 600))
    elif choice == 1 and cash == 600:
            coffee = coffee - 1
            print("주문하신 커피 나왔습니다.")
    elif choice == 1 and cash < 600:
            print("금액이 부족합니다. 잔돈 %d원을 반환합니다." %cash)
    if choice == 2 and coke == 0:
            print("콜라는 현재 품절 상태입니다. 잔돈 %d원을 반환합니다" %cash)
    elif choice == 2 and cash > 900:
            coke = coke - 1
            print("주문하신 콜라 나왔습니다. 잔돈 %d원을 반환합니다." %(cash-900))
    elif choice == 2 and cash == 900:
            coke = coke - 1
            print("주문하신 콜라 나왔습니다.")
    elif choice == 2 and cash < 900:
            print("금액이 부족합니다. 잔돈 %d원을 반환합니다." %cash)


