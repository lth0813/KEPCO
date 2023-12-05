# a = int(input())
# b = int(input())
# print((a+b),(a*b))

# class Cal():
#     def grade(self,first,second,third):
#         self.first = first
#         self.second = second
#         self.third = third
#     def add(self):
#         return print(self.first + self.second + self.third)
#     def aver(self):
#         return print(((self.first + self.second + self.third)/3))
# run = Cal()
# run.grade(int(input()),int(input()),int(input()))
# run.add
# run.aver()

class mcm():
    def __init__(self):
        self.m = 0
        self.cm = 0
        self.number = 0
    def choice(self):
        print("1. m to cm\n2. cm to m")
        self.number = int(input())
    def mtocm(self):
        print("변환하고자 하는 m의 수를 입력하세요.")
        self.m = int(input())
        print(self.m*100,'cm')
    def cmtom(self):
        print("변환하고자 하는 cm의 수를 입력하세요.")
        self.cm = int(input())
        print(self.cm//100,'m')
run = mcm()
run.choice()
while True:
    if run.number == 1:
        run.mtocm()
    elif run.number == 2:
        run.cmtom()
    break
