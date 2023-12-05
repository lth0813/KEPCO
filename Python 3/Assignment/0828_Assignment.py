# for문 없이 1~9까지 출력하기 int(0~9)
i=0
for _ in [1,2,3,4,5,6,7,8,9]:
    print(i+1); 
    i=i+1
#구구단
number = 0
number = number+1
print(2, '*', number, '=', number*2) #print("%d * %d = %d" % (2, i, 2*i))
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)
number = number+1
print(2, '*', number, '=', number*2)

dan = 2
number = 0
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
number = number + 1
print(f"{dan} * {number} = {dan * number}")
#포맷함수 / f string 익숙해지기
number = 0
for _ in range(1,10):
    number = number + 1
    print(("%d * %d = %d" % (2, number, number*2)))
    
#특정 점수를 입력했을때 학점으로 변환
score = int(input("Enter your score: "))
if score >= 90:
    grade = 'A'
if 90 > score >= 80:
    grade = 'B'
if 80 > score >= 70:
    grade = 'C'
if 70 > score >= 60:
    grade = 'D'
if score < 60:
    grade = 'E'
print(grade)
#elif 사용, 역순으로 뒤집기

input("age: ")
age: 23
print(3>5)
print("%d"%(3>5))
print(f"{3>5}")
Bool = 3 in [2,4,6]
print("f{Bool}")
print(f"{Bool}")
