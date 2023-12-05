        #03장 for문 (while, for)

# for i in 반복 가능 객체(iterable) : 리스트(튜플, 문자열):
# ...수행문장1
# ...수행문장2

        #range함수
#range([시작번호,] 마지막 번호(-1)[, 증가값]) - 기본 시작값은 0, 기본 증가값은 1
    #range(0, 11, 1) = range(11)
# print(list(range(1 , 11)))

# for문으로 1~9까지 출력하기
#for i in range(1,10):
#    print(i)

        #세로형 구구단
# for i in range(1, 10):
#    print("   %d단   " %i)
#    for j in range(1, 10):
#        print("%d * %d = %d"%(i,j,i*j))

        #가로형 구구단        
# for i in list(range(1, 10)):
#     print("    %d단   " %i, end=" ")
# print(" ")
# for i in list(range(1, 10)):
#     for j in range(1, 10):
#         print("%2d *%2d =%2d" %(j,i,i*j), end=" ")
#     print(" ")

        #리스트 컴프리헨션 - 표현식 for 항목 in iterable if conditional
# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num * 3)
# print(result)

# result=list()
# for i in range(1,10):
#     result.append(3*i)
# print(result)

# result = [ i*3 for i in range(1,10)]
# print(result)

# result = [ i*3 for i in range(1,10) if i%2 == 0]
# print(result)

        #while문
            #while (조건):
            #... 수행문1
            #무한루프 - 가급적 for문으로 대체하자. 
            #ex)메뉴(프로그램이 무한 반복)
            
            #while문을 만들때, 먼저 실행시키는 코드와 if로 종료 코드를 만들어놓고 시작하자.
                #실행 코드 (True)
            #while (1):
                #메뉴
            #prompt(menu) = """ """(여러줄 문자열)
                #종료 코드
            #...if (조건)
            #......break
# i=0
# while i<10:
#     i = i + 1
#     print("%2d *%2d = %2d" %(2, i, 2*i))
    
# i=0
# while True:
#     i = i + 1
#     if i >= 10:
#         break
#     print("%2d *%2d = %2d" %(2, i, 2*i))

#dic={ } #dict() / { key1:value1, key2:value2 }

name = input("입력하세요: ") #aba
dic={ }
for key in name: #a b a를 순서대로 key로 대입?
    if key not in dic: #key(a b a)가 dic 안에 없으니까
        dic[key] = 0 #{key : 0}을 추가 a:0 ,b:0 / a가 key안에 있으므로 else 구문으로?
        dic[key] = dic[key] + 1 #증가값 (0+1) a:1 ,b:1
    else:
        dic[key] = dic[key] + 1 #{a:1} -> {a:2}
    print(dic)
for key in dic.keys(): #dic안에 있는 key의 리스트를 만든다.
    print(f'{key}:{dic[key]}', end = ' / ') #key가 [a, b] dic[key]는 value는 (2, 1)
print('[dict]')

#키가 없으면, 키를 만들어야함
