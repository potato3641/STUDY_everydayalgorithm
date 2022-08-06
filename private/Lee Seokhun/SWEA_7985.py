import sys
from traceback import print_tb
sys.stdin = open("input.txt", "r")
caseNum=int(input())
#완전이진트리의 중위순회를 하는 경우, 한 개씩 건너뛴 요소들이 같은 레벨임을 알게 됨
for i in range(caseNum):
    #현재 케이스의 깊이와 테스트 리스트를 입력받음
    #각 레벨에 해당하는 요소를 담을 리스트를 만듦
    nowCase=int(input())
    nowList=list(map(int,input().split()))
    levelList=[]
    #해당 레벨의 요소를 넣을 배열을 생성하고,
    for k in range(nowCase):
        levelList.append([])
        #앞에서부터 pop을 하면 indexerror가 나므로 뒤에서부터 한개씩 건너뛰어 요소들을 추출함
        for p in range(len(nowList)-1,-1,-2):
            levelList[k].append(str(nowList.pop(p)))
        #거꾸로 담았기 때문에 다시 원래 순서로 바꿔줘야함
        levelList[k].reverse()
    for k in range(nowCase):
        if k==0:
            #최상위 케이스는 1개이므로 1개를 print 해줌
            print("".join(["#",str(i+1)," ",levelList[nowCase-1][0]]))
        else:
            #같은 레벨의 케이스들을 모두 출력함
            print(" ".join(levelList[nowCase-k-1]))