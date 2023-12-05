result1 = [19, 15, 6]
result2 = [67, 0, 55]
result3 = [5, 15, 0]

name1 = ["may", "kein", "kain", "radi"]
name2 = ["kali", "mari", "don"]
name3 = ["may", "kein", "kain", "radi"]

yearning1 = [5, 10, 1, 3]
yearning2 = [11, 1, 55]
yearning3 = [5, 10, 1, 3]

photo1 = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
photo2 = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
photo3 = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

def solution(name,yearning,photo):
    m_point = { } ; point = [ ] ; score = 0
    for i in range(len(name)):
        m_point[name[i]] = yearning[i] #딕셔너리에 각 이름에 맞는 점수 저장
    for List in photo:
        for j in range(len(name)):
            if name[j] in List: #이름이 각 사진에 있는지 확인
                score =+ m_point[name[j]]
                point.append(score)
            else:
                pass
        
solution(name1,yearning1,photo1)
