#2차원 배열 = 리스트 안에 리스트 
ary = [[],[],[],[],[]]
# 1  2  3  4  5
# 6  7  8  9 10
#11 12 13 14 15
#16 17 18 19 20
#21 22 23 24 25

# cnt = 0
# for i in range(5):
#     for j in range(5):
#         cnt = cnt + 1
#         ary[i].append(cnt)
# print(ary)

#형태로 출력하기 위해서 배열에 저장하고 배열에 저장된 내용을 출력

#배열을 90도 회전해보자.
#21 16 11  6  1
#22 17 12  7  2
#23 18 13  8  3
#24 19 14  9  4
#25 20 15 10  5

# cnt = 0
# for i in range(5):
#     cnt = cnt + 1
#     for j in range(4,-1,-1):
#         ary[i].append((j*5)+cnt)
# print(ary)
# for i in range(5):
#     for j in range(5):
#         print("%2d"%(ary[i][j]),end=' ')
#     print()


#배열을 달팽이식으로 해보자.
ary = [[],[],[],[],[]]
cnt = 0
while len(ary[1]) < 2:
    if len(ary[0]) < 4:
        cnt = cnt + 1
        ary[0].append(cnt) #첫 줄 1,2,3,4,5 -> cnt 수치는 현재 5
    elif len(ary[0]) == 4:
        for i in range(5):
            cnt = cnt + 1
            ary[i].append(cnt)
    elif len(ary[0]) == 5 and len(ary[4]) < 5:
        cnt = cnt + 1
        ary[4].append(cnt)
    elif len(ary[4]) == 5:
        for j in range(3,0,-1):
            cnt = cnt + 1
            ary[j].append(cnt)
ary[4].reverse()
for k in range(1,4):
    ary[1].insert(1,k+cnt)
    if 
        cnt = cnt + 1
        ary[k].insert(3,cnt+3):
        
# ary[1].reverse()

print(ary)

# 1  2  3  4  5 - 0.0 / 0.1 / 0.2 / 0.3 / 0.4
#16 17 18 19  6 - 1.0 / 1.1 / 1.2 / 1.3 / 1.4
#15 24 25 20  7 - 2.0 / 2.1 / 2.2 / 2.3 / 2.4
#14 23 22 21  8 - 3.0 / 3.1 / 3.2 / 3.3 / 3.4
#13 12 11 10  9 - 4.0 / 4.1 / 4.2 / 4.3 / 4.4

# i가 0 1 2 3 4 j가 4 3 2 1 0
# i가 1 2 3 j가 3 2 1
# 마지막은 2.2
