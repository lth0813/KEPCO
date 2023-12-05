#money = False
#if money:
#    print("택시를 타고 간다.")
#else:
#    print("걸어간다.")

#money = int(input())
#if money >= 6000:
#    print("택시를 타고 간다.")
#else:
#    print("걸어간다.")

#money = int(input())
#card = str(input())
#if card == "Y" or money >= 6000:
#    print("택시를 타고간다.")
#else:
#    print("걸어간다")

#pocket = ["card", "money", "paper"]
#if "card" not in pocket:
#    print("걸어간다.")
#else:
#    print("버스를 타고 간다.")

#money = int(input())
#pocket = ['card' , money]
#if money >= 6000:
#    print("택시를 탄다.")
#elif "card" in pocket:
#    print("버스를 탄다.")
#else:
#    print("걸어간다.")

#marks = [90, 47, 77, 63, 52]
#number = 0
#for mark in marks:
#    number = number + 1
#    if mark < 60: continue
#    print("%d번 학생은 합격입니다. 축하합니다." % number)

#sum = 0
#for add in range(1,101):
#    sum = sum + add
#print(sum)

#marks = [90, 47, 77, 63, 52]
#for number in range(len(marks)):
#    if marks[number] < 60:
#        continue
#    print("%d번 학생 합격입니다. 축하합니다" %(number + 1))

for dan in range(2,10):
    for multi in range(1,10):
        print(dan*multi, end=" ")
    print(' ')
