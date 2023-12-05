#초 단위의 시간을 시간,분,초로 변환하기
# def s_change(time):
#     hour = time // 3600
#     min = time % 3600 // 60
#     sec = time % 3600 % 60
#     return print("%d시간 %d분 %d초" %(hour,min,sec))

# print("변환하고자 하는 초를 입력하세요: ", end = '')
# time = int(input())
# s_change(time)

#점수를 입력 받으면 상장을 표시
prizes = [['금상', 90, 1, 1, 20],['은상', 80, 1, 1, 10],['동상', 70, 1, 1, 5],['장려상', 60, 1, 0, 0]]
data = [['장려상', 60, 1, 0, 0],['동상', 70, 1, 1, 5],['은상', 80, 1, 1, 10],['금상', 90, 1, 1, 20]]
print("본인 점수를 입력하세요: ", end = "")
grade = int(input())

def prize(List,grade):
    if grade >= List[1]:
        return List
            
for List in prizes:
    result = prize(List, grade)
    if bool(result) != False:
        break
print(result)

# def prize(grade):
#     if 90 > grade >= 0:
#         for i in range(3):
#             if prizes[i][1] <= grade < prizes[i+1][1]:
#                 print(prizes[i][0])
#                 if prizes[i][2] == True:
#                     print('상장')
#                 if prizes[i][3] == True:
#                     print('도서상품권 %d개' %prizes[i][4])
#     else:
#         print(prizes[3][0])
    
    # if grade >= 90:
    #     print("금상:", "상장, 도서상품권 20개")
    # elif 90 > grade >= 80:
    #     print("은상:", "상장, 도서상품권 10개")
    # elif 80 > grade >= 70:
    #     print("동상:", "상장, 도서상품권 5개")
    # elif 70 > grade >= 60:
    #     print("장려상:", "상장")
    # else:
    #     print("더 노력하세요.")
    
        # def prize(List, score):
        #     if score >= List[1]:
        #         return True
        #
        # print(data[::-1])
        # score = int(input("점수를 입력하세요: "))
        # for idx, List in enumerate(data[::-1]):
        #     if prize(List, score):
        #         print(data[::-1][idx])
        #         break

    # score = int(input("점수를 입력하세요: "))
    # for [rank, min_score, trophy, bonus, qty] in prizes:
    #     if score >= min_score:
    #         print(f"===={rank}====", end=' ')
    #         if qty:
    #             print(f"상품: 문화상품권 {qty}매")
    #         break
