#본인의 이름을 입력 받아서 -> a 부터 z 까지 알파벳이 몇개 쓰였는지 출력하는 프로그램 작성

name = list(str(input()))
name2 =list(set(name)) #[l, i, m, t, a, e, h, w, n]
name2.sort()
while True:
    if len(name2) == 0:
        break
    else:
        print(name2[0],'=', name.count(name2[0]))
        name2.pop(0)

# alpha = list("abcdefghijklmnopqrstuvwxyz")
# name = list(str(input())) # l i m t a e h w a n
# # for e in alpha:
# #     cnt = 0
# #     name.count(e)
# #     for n in name:
# #         if e in name:
# #            if e == n:
# #                cnt = cnt + 1 #증가식
# #     print(e, ':', cnt)

# for e in alpha:
#     if name.count(e) != 0:
#         print(e, ':', name.count(e), end=" / ")
#문제점
    #없는 알파벳도 다 확인해야한다.

