import sys
sys.stdin = open("input.txt", "r")
caseNum=int(input())
for i in range(caseNum):
    thisNum=int(input())
    #입력받는 단어 리스트와, 가능한 단어장의 경우를 담는 리스트를 만듦
    wordList=[]
    outputList=[]
    #가능한 단어장의 경우를 찾는 함수를 만듦
    def findSet(inputWord,checkList):
        #아직 포함하지 않는 단어를 찾음
        for q in range(len(checkList)):
            nowCheckList=checkList[:]
            #단어가 아직 포함되지 않았다면
            if nowCheckList[q]==0:
                #하나의 단어로 이어붙이고 리스트에 포함했다고 1로 표시함
                addWord=inputWord+wordList[q]
                nowCheckList[q]=1
                #중복을 제외하고 길이가 26이면 모든 알파벳이 들어가 있으므로
                if len(set(addWord))==26:
                    #결과리스트에 추가함
                    outputList.append(nowCheckList)
                #변화된 단어와 체크리스트를 포함하여 다시 찾기 시작
                findSet(addWord,nowCheckList)
    #wordlist에 단어 입력
    for k in range(thisNum):
        nowWord=input()
        wordList.append(nowWord)
    
    for w in range(thisNum):
        #첫 단어와, 체크리스트를 생성하여 함수에 넣어 탐색 시작
        targetWord=wordList[w]
        targetList=[0]*thisNum
        targetList[w]=1
        findSet(targetWord,targetList)
        #결과리스트에도 겹치는 배열들이 있기 때문에 set을 사용하여 중복을 제거한 리스트의 길이를 답으로 제출
    print("".join(["#",str(i+1)," ",str(len(set(list(map(tuple,outputList)))))]))