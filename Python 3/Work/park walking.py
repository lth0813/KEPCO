park =["SOX","OXO","OOO"]
route = ["E 1","S 2","W 1"]	
result = [ ]#2,1
temp_r = [ ]
obstacle =  [ ]
#전체 공원 크기
p_size = [len(park[0]),len(park)]
#시작 지점 좌표
start = [ ]
for i in range(len(park)):
    if "S" in park[i]:
        start.append(park.index(park[i]))
        start.append(park[i].index("S"))
print(start)
#장애물 좌표
for i in range(len(park)):
    if "X" in park[i]:
        ob = [ ]
        ob.append(park.index(park[i]))
        ob.append(park[i].index("X"))
        obstacle.append(ob)
print(obstacle)
#route 계산 (예외 : #1 공원을 벗어났을때)
for i in range(len(route)):
    temp_r.append("".join(list(map(str, route[i]))).split())
print(temp_r)
for i in temp_r: #i = [E2], [S2], [W1]
    for k in range(len(park[0])): #내가 k 줄에 있을때
        print("작동확인0")
        if start[1] == k:
            print("작동확인1")
            if i[0] == 'E': #동쪽으로 이동이면
                if p_size[1]-start[1] >= int(i[1]): #내가 갈 거리가 공원 총 거리보다 작으면
                    print("작동확인5")
                    if len(obstacle) > 0:
                        for j in obstacle:
                            print("작동확인-1")
                            if start[0] == j[0] and len(obstacle) > 0: #장애물이 있으면
                                print("작동확인3")
                                if int(i[1]) < j[1]: #내가 갈 거리가 장애물 위치보다 작으면
                                    print("작동확인4")
                                    start[1] += int(i[1]) # 동쪽방향으로 그 만큼 간다.
                            elif start[0] != j[0] or len(obstacle) == 0: #장애물이 없다면
                                print("작동확인6")
                                start[1] += int(i[1]) # 동쪽방향으로 그 만큼 간다.
                    else:
                        start[1] += int(i[1]) # 동쪽방향으로 그 만큼 간다.
                        print("작동확인L")
                elif i[0] == 'W': #서쪽으로 이동이면
                    if start[0] == j[0]: #장애물이 있으면
                        if start[1]-j[1] > int(i[1]): #이동 거리가 장애물까지의 거리보다 작으면
                            if p_size[1]-(p_size[1]-start[1]) >= int(i[1]): #공원 총 거리를 벗어나지않는다면
                                start[1] -= int(i[1])
                    elif start[0] != j[0] or len(obstacle) == 0: #장애물이 없다면
                        if p_size[1]-(p_size[1]-start[1]) >= int(i[1]): #공원 총 거리를 벗어나지않는다면
                            start[1] -= int(i[1])        
        for m in range(len(park)):
            if start[0] == m: 
                if i[0] == 'N':
                    if start[1] == j[1]: #장애물이 있으면
                        if start[0]-j[0] > int(i[1]):
                            if p_size[0]-(p_size[0]-start[0]) >= int(i[1]):
                                start[0] -= int(i[1])
                    elif start[1] != j[1] or len(obstacle) == 0: #장애물이 없다면
                        if p_size[0]-(p_size[0]-start[0]) >= int(i[1]):
                            start[0] -= int(i[1])                            
                elif i[0] == 'S':
                    if start[1] == j[1]: #장애물이 있으면
                        if int(i[1]) < j[0]:               
                            if p_size[0]-start[0] >= int(i[1]):
                                start[0] += int(i[1])
                    elif start[1] != j[1] or len(obstacle) == 0: #장애물이 없다면
                        if p_size[0]-start[0] >= int(i[1]):
                            start[0] += int(i[1])
print(len(obstacle))
print(start)
