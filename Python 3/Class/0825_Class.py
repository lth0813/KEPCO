#숙제
a = 'hobby'
print(a.lower())
print(a.count('b'))
print(a.find('b'))
print(a.find('b')+a[2:].find('b')+1)

print(a.split('b'))

#참(true, 1) / 거짓(false, 0) - p.106
    #조건 -> 참, 거짓 판별
        #숫자형 -> 참 : 0이 아닌 숫자형 / 거짓 : 0
        #자료형 -> 참 : 거짓을 제외한 나머지 / 거짓 : ""(빈 문자열)
    #비교연산자 - p.126
        #< , > , == , != , >= , <=
print(1>2)
#변수 - p.111
    #저장공간(Memory) -> =(assignment)
    #변수 만들기 -> 변수명 = 값
    #[:] -> 리스트 전체
word="hobby"
a=word
print(a is "hobby")

a=[1,2,3]
b=a
print(b)
print(a is b)
a[1]=4
print(b)
print(a is b)

a=[1,2,3]
b=a[:]
print(a is b)
a[1]=4
print(b)
print(a is b)
    #위쪽 예시(b=a)는 원본을 그대로 사용하는 것이고, 아래쪽 예시(b=a[:])는 복사본을 사용한다.
        #변수 복사
    #a='hobby' / b=a -> a is b = true -> id(a) == id(b)
        #깊은 복사 (copy모듈)
    #b=a[:] / b=copy(a) -> a is b = false -> id(a) != id(b)
#리스트 자료형 - p.77
    #리스트 안에는 어떠한 자료형도 포함할 수 있다.
odd = [1,3,5,7,9]
    #리스트 인덱싱 -> odd[idx]
    #리스트 슬라이싱 -> odd[1:3]
    #append / sort / reverse / insert / remove / pop / count / extend
words = "hobhy"
words_list = list(words)
print(words_list)
words_list[3]='b'
print(words_list)
    #어떻게 문자열로?
print("".join(words_list))

#문제!
    #Q1 = '1 2 3 4 5 6' > 합을 구하라!
    #Q2 = 'Hello Python!'을 !nohtyP olleH > 역순으로 출력하라
    #Q3 = '3 a 7 21 z x u b d 0 b b b 2 1 1 1'을 char, int 각각으로 분류(정렬)하시오
#Q1
print(1+2+3+4+5+6)
#Q2.1
print('Hello Python!'[::-1])
#Q2.2
Q2="Hello Python!"
Q2a=list(Q2)
Q2a.reverse()
print("".join(Q2a))
#Q3
Q3 = '3 a 7 21 z x u b d 0 b b b 2 1 1 1 '
Q31 = Q3.split()
print(list(Q31))
Q31.sort()
print(Q31)
Q31[0]=int(Q31[0])
Q31[1]=int(Q31[1])
Q31[2]=int(Q31[2])
Q31[3]=int(Q31[3])
Q31[4]=int(Q31[4])
Q31[5]=int(Q31[5])
Q31[6]=int(Q31[6])
Q31[7]=int(Q31[7])
Q32=[]
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q32.append(Q31.pop())
Q31.sort()
Q32.sort()
Q31.extend(Q32)
print(Q31)
    #char = '                011112237abbbbduxz'
    #int : 011123721 / char : 'abbbbduxz' or '                abbbbduxz'
    #int : 0 1 2 3 7 21 / char : a b d u x z
#sorted()
print(Q3.split())
print(set(Q3.split()))
print(list(set(Q3.split())))
print(list(set("bbbbbbbbbb")))
#() - 튜플, {} - 집합, [] - 리스트 - p.89
a = 3
b = 5
a,b = b,a
print(a)
print(b)

a = 3
b = 4
temp = b
b = a
a = temp
print(a)
print(b)
    #튜플의 요소는 변화 불가능, 리스트는 가능
b=[2,3]
a=(1,b)
b[0] = 1
print(a)
    #하지만 리스트를 요소로 가지면 리스트 안의 요소는 변화가 가능한듯?
    
#주말동안 해봅시다!
    #스마트 알람을 개발하는 것을 목표로 해서 나의 일과를 print문으로 작성해본다.
    #작성한 내용 중에서 조건식 구현가능(True/False)구별이 가능한 내용과 그렇지 않은 내용을 구별해본다.
        #ex) 나는 %d를 %s개 먹었다. 나는 몇시에 배가 고프다. (True/False)
