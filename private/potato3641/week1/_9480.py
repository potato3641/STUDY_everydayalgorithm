import sys
sys.stdin = open("_9480input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
def ncr(line, n): # nCr 개의 조합 추출
    basket = []
    if n == len(line): # 전체 조합은 통짜 하나임
        return [''.join(line)]
    if n == 1: # 1개씩 조합은 그 자체임
        return line
    elif n > 1: # 위에 둘 다 아니라면...
        cnt = 1 # n 대체용도
        for i in range(len(line)): # 2개 이상이니 바스켓 안의 리스트 초기화 겸 1단계 실행
            basket.append([line[i]])
        while cnt < n:
            newbasket = [] # 단계별 중복 제거를 위한 초기화
            for j in range(len(basket)): # basket 안의 원소 갯수만큼
                for i in range(len(line)): # line 안의 원소 갯수만큼
                    if line[i] not in basket[j]: # basket에 line이 들어있나?
                        target = sorted(basket[j]+[line[i]]) # 안되면 넣고 정렬돌리기 ( 중복 체크용 )
                        if target not in newbasket: # 해당 값이 이미 추가된 값인가?
                            newbasket.append(target) # 아니라면 넣기
            basket = newbasket[:] # 깊은 복사
            cnt += 1
        return basket
for test_case in range(1, T + 1):
    N = int(input())
    word = []
    for i in range(N):
        word.append(input())
    rst = 0
    for i in range(1, N+1):
        ncrs = ncr(word,i) # 조합 구해오세요
        for j in ncrs: 
            if len(set(list(''.join(j)))) == 26: # 조합이 a-z의 수량 26개?
                rst += 1
    print(f'#{test_case} {rst}')