import sys
sys.stdin = open("input.txt", "r")
caseNum=int(input())
for i in range(caseNum):
    #사람 수 N과 문제 수 M을 입력받음
    N,M=map(int,input().split())
    #가장 많이 푼 문제 수와, 1등한 사람의 수를 각각 변수로 만듦
    MaxCase=0
    MaxCount=0
    for k in range(N):
        #푼 문제(1)의 개수를 세고
        nowVal=list(map(str,input().split())).count("1")
        #푼 문제 수가 maxcase보다 크다면, maxcase에 넣고 1등 사람수를 초기화
        if nowVal>MaxCase:
            MaxCase = nowVal
            MaxCount = 1
        #푼 문제수가 maxcase와 같다면, 1등 사람수에 추가
        elif nowVal==MaxCase:
            MaxCount +=1
    print("".join(["#",str(i+1)," ",str(MaxCount)," ",str(MaxCase)]))