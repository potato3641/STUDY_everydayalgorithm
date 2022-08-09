import sys
sys.stdin = open("_6900input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    lotto_case = [[] for _ in range(N)]
    lotto = []
    for i in range(N):
        lotto_case[i] = list(input().split())
    for i in range(M):
        lotto.append(input())
    money = 0
    for nums in lotto:
        for j in range(len(lotto_case)):
            cnt = 0
            for i in range(8):
                if nums[i] == lotto_case[j][0][i] or lotto_case[j][0][i] == '*':
                    cnt += 1
            if cnt == 8:
                money += int(lotto_case[j][1])
    print(f'#{test_case} {money}')
