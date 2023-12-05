import random
a_list = [1,2,3,4,5,6,7,8,9]
answer = random.sample(a_list, 3)
# print(answer)

class N_Baseball:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.life = 1
        self.my_answer = [ ]
    
    def number(self):
        print(("%d회" %pitch.life)) #1~9회까지
        print("숫자 3개를 입력해주세요")
        my_number = str(input())
        for i in my_number.split():
            self.my_answer.append(int(i))
        print(self.my_answer) #내 답을 리스트로 표현
    
    def check(self): #체크용
        for i in range(3):
            if self.my_answer[i] in answer: #첫번째 값이 답 안에 있으면
                if self.my_answer.index(self.my_answer[i]) == answer.index(self.my_answer[i]): #내가 제출한 첫번째 값의 인덱싱 값과 답의 인덱싱 값이 같으면
                    self.strike = self.strike + 1
                else:
                    self.ball = self.ball + 1 #내가 제출한 첫번째 값의 인덱싱 값이 답의 인덱싱 값이 다르면
            else:
                pass #아예 없으면
        print("%s Strike, %s Ball" %(self.strike,self.ball))  
        self.life = self.life + 1 #목숨 카운팅
    
    def victory(self): #승리조건
        if self.strike == 3: #승리
            print("축하합니다! 승리하셨습니다!")
        elif self.life >= 10: #패배
            print("패배하셨습니다. 다음 기회를 노려보세요")
            print("답은 %d,%d,%d입니다." %(answer[0],answer[1],answer[2]))

    def reset(self):
        self.my_answer = [ ] ; self.strike = 0 ; self.ball = 0 #리셋

pitch = N_Baseball() #구동
while True:
    pitch.number() #답 제출
    pitch.check()
    pitch.victory()
    if pitch.strike == 3 or pitch.life >= 10:
        break
    pitch.reset()
    



