# 두 수 비교
# def compare():
#     a = int(input("첫번째 숫자를 입력하세요: "))
#     b = int(input("두번째 숫자를 입력하세요: "))
#     if a > b:
#         print(a, "\na가 b보다 %s만큼 큽니다."%(a-b))
#     elif a == b:
#         print("a와 b는 같은 숫자입니다.")
#     else:
#         print(b, "\nb가 a보다 %s만큼 큽니다."%(b-a))
# compare()

# 세 수 중 가장 큰 수 찾기
# def tricompare():
#     a = int(input("첫번째 숫자를 입력하세요: "))
#     b = int(input("두번째 숫자를 입력하세요: "))
#     c = int(input("세번째 숫자를 입력하세요: "))  
#     if a > b and a > c: #a가 가장 큰 수
#         print("a가 가장 큰 수 입니다.")
#     elif a < b and b > c: #b가 가장 큰 수
#         print("b가 가장 큰 수 입니다.")
#     else: # a > b and a < c or a < b and b < c: c가 가장 큰 수
#         print("c가 가장 큰 수 입니다.")
# tricompare()

# max 함수의 기본 구조
# def max():
#     max = int(input("숫자를 입력하세요: "))
#     a = int(input("두번째 숫자를 입력하세요: "))
#     if a > max:
#         max = a
#     a = int(input("세번째 숫자를 입력하세요: "))
#     if a > max:
#         max = a
#     print("가장 큰 수는 %d 입니다." %max)
# max()    

# 매개변수
def myMax(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    print(max)
myMax(1, 3, 6, 200, 18239, 29012522, 76120, 20123875)

#07장.
    #이터레이터, 제네레이터
    #타입 어노테이션
    
    #코딩테스트 Lv. 1 - 순서도(Lv. 0)
#08장.
    #정규 표현식
import re
data = """
park 800905-1049118
kim  700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
