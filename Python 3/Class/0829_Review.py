#for문
    #기본모습 : for 변수 in 리스트(튜플, 문자열):
    #               수행문장 1 <- 리스트안에 있는 요소를 순서대로 변수에 대입.
    #range함수 : range(시작, 마지막, 증가값) -> 기본 시작값은 0이며 기본 증가값은 1이다.(아무것도 넣지 않았을 때)
    #리스트 컴프리헨션 : 포현식 for 항목 in iterable if conditional
    #                  ex)result = [num*3 for num in a]

#while문
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

#딕셔너리
    #기본모습 : {Key1: Value1, Key2: Value2}
    #추가 : dic[key] = value
    #제거 : del dic[key] - key의 value값 삭제
    
    #key를 사용해 value 얻기
        #dic = {key : value} - dic[key] >> value
    #중복되는 key 값이 있다면 무작위로 하나만 남는다. 또한 리스트는 key 값으로 사용할 수 없다.
    
    #딕셔너리 관련 함수
        #dic.keys() - dic의 key들을 리턴한다.
            #ex) for i in dic.keys()
            #       print(i) : 1, 2, 3
        #dic.values() - dic의 value들을 리턴한다.
        #dic.items() - dic의 key와 value의 쌍을 튜플로 묶어서 리턴한다.
        #dic.clear() - 딕셔너리안의 모든 요소를 삭제한다.
        #dic.get('key') - dic의 key에 대응되는 value값을 리턴한다.
        #key in dic - dic안에 key가 있는지 표시한다. (True/False)
        
