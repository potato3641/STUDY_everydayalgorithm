import sys
sys.stdin = open("_6808input.txt", "r")
def factorial(line, mine):
    n = len(line) # 길이는 자동 계산됨
    basket = []
    if n == 1:
        return line # 끝단은 그대로 반환
    else:
        for i in line:
            target = set() # { i }
            target.add(i)
            withouts = list(set(line)-target) # i를 제외한 리스트. list.pop(i)
            for j in factorial(withouts, mine): # i를 제외한 리스트 순회 : j
                newbasket = []
                newbasket.append(i) # i 추가
                if type(j) == type(0): # 제일 마지막 단이면 int이고 아니면 list
                    newbasket.append(j) # (단일) j 추가
                else:
                    newbasket += j # (다수) j 추가
                basket.append(newbasket) # i + j 추가
        if len(line) == len(mine): # basket에 순열,9가 저장되어 있을 때
            wcnt, lcnt = 0, 0
            for i in basket:
                w = 0
                l = 0
                for j in range(len(i)):
                    if mine[j] > i[j]: # 이기면
                        w += mine[j] + i[j] # 규영이 점수 추가
                    else:
                        l += mine[j] + i[j] # 은영이 점수 추가
                if w > l: # 승패 판단
                    wcnt += 1
                else:
                    lcnt += 1
            return wcnt, lcnt # 승패 결과 반환
        return basket # 순열, 8 이하일 경우 재귀
T = int(input())
for test_case in range(1, T + 1):
    mine = list(map(int,input().split())) # 규영이 카드
    your = list(set([i+1 for i in range(18)]) - set(mine)) # 은영이 카드
    w, l = factorial(your, mine) # 조합 계산해서 승리, 패배 횟수 반환
    print(f'#{test_case} {w} {l}')
    