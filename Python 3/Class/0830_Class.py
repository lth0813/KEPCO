# #리스트 : 리스트 in 리스트
#     #[ [    ],[    ],[    ] ]
# #3중 for문
#     #포켓몬빵 700원, 아.아 3100원, 컵라면 1200원
# cash = int(input())
# bread = 700
# coffee = 3100
# ramen = 1200
# result = []
# total = 0 ; cnt = 0
# for i in range(1,(cash//bread)+1):
#     for j in range(1,(cash//coffee)+1):
#         for k in range(1,(cash//ramen)+1):
#             changes = cash - ((i*700) + (j*3100) + (k*1200))
#             total = total + 1
#             if (i*700) + (j*3100) + (k*1200) <= cash:
#                 if 0 <= cash - ((i*700) + (j*3100) + (k*1200)) < 700:
#                     cnt = cnt + 1
#                     print("빵 : %2d개 / 커피 : %2d개 / 컵라면 : %2d개 / 잔돈 : %3d원" %(i,j,k,changes))
#                     result.append([cnt, i, j, k, changes])
# print(total)
# print(result) # = [[1, 1, 1, 2, 0], [2, 2, 1, 1, 500]]
# print([List[4] for List in result]) # 0, 500
# print([List[0] for List in result]) # 1, 2

# sort_result = { }
# for List in result: #[1, 1, 1, 2, 0] 와 [2, 2, 1, 1, 500]을 차례대로 List에 대입
#     if List[-1] not in sort_result: # 0이 sort_result에 없으니까
#         sort_result[List[-1]] = [ ] # 0이 key가 되고, value 값이 [ ] 된다. {0:[ ]} 
#     print(List)
#     sort_result[List[-1]].append(tuple(List)) #sort_result[List[-1]](0의 value) = [ ]이니까 여기에 List = [1, 1, 1, 2, 0]를 튜플 형식으로 추가
#                                               #sort_result = {0: ([1, 1, 1, 2, 0])} 상태가 된다.
# print(sort_result)

# Key_list = list(sort_result.keys()) #Key_list = [0, 500] (sort_result의 키를 전부 불러와서 리스트로 만들고)
# Key_list.sort() #sort를 해서 [0, 500]가 된다.

# for key in Key_list: #0, 500을 차례대로 key에 투입하고 
#     for List in sort_result[key]: #sort_result[0](0의 key = 튜플(1, 1, 1, 2, 0)) 가져오고 그거를 차례대로 List로
#         print(List) #List는 (1, 1, 1, 2, 0)
#         print(f'[{List[0]}] 포켓몬빵을 {List[1]}개 구매하고', end=',')
#         print(f'컵라면을 {List[2]}개 구매하고', end=',')
#         print(f'커피를 {List[3]}개 구매해서 잔돈이 {List[4]}만큼 남았습니다.')
        
# bingo = [[1,2,3,4,5],
#          [6,7,8,9,10],
#          [11,12,13,14,15],
#          [16,17,18,19,20],
#          [21,22,23,24,25]]

# for line in bingo:
#     for number in line:
#         print("%2d" %number, end = ' / ')
#     print()

ary = [[], [], [], [], []]
# for i in range(25):
#     print((i+1), end=' ')
#     if i % 5 == 4:
#         print()

# cnt = 0
# for i in range(5):
#     for j in range(5):
#         cnt = cnt + 1
#         print('%2d'%(cnt), end=' ')
#     print()

cnt=0
for i in range(5):                      #빈 리스트를 가져올 index
    for j in range(5):                  #반복 수
        cnt = cnt + 1                   #1~25
        ary[i].append(cnt)              #ary[0] 일 때, 첫번째 빈 리스트를 가져와서 [1,2,3,4,5]를 넣고 그 후 5번 반복
        print('%2d'%(cnt), end=' ')
    print()      

print(ary)

for i in range(5):                          #i = 0 ~ 4
    for j in range(5):                      #j = 0 ~ 4
        print("%2d"%(ary[i][j]),end = ' ')  #ary[0]이 [1,2,3,4,5]니까 여기서 [0]에 위치한 1을 가져온다. 그 후 4까지 반복해서 1 ~ 5 출력 후
    print()                                 #print문으로 줄을 바꾼뒤 ary[1] - 1 ~ 4로 반복
    
