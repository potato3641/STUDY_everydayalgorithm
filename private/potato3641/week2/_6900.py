import sys
sys.stdin = open("_6900input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    lotto_case = []
    lotto = []
    for i in range(N):
        lotto_case.append(list(input().split()))
    for i in range(M):
        lotto.append(input())
    money = 0 # 당첨금
    for nums in lotto: # 로또용지 순회
        for j in range(len(lotto_case)):
            cnt = 0 # 로또 번호 당첨 횟수 카운터
            for i in range(8):
                if nums[i] == lotto_case[j][0][i] or lotto_case[j][0][i] == '*':
                # 로또 번호가 동일하거나 *인 경우만 카운터 늘림
                    cnt += 1
            if cnt == 8: # 모두 당첨된 경우만 당첨금 누적
                money += int(lotto_case[j][1])
    print(f'#{test_case} {money}')
