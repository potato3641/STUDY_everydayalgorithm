
T = int(input())

for test_case in range(T):
    s, e, m = list(map(int, input().split()))

    sun = 0
    while True:
        year = 365 * sun + s  # 365가 가장 크므로 365의 배수를 기준으로 조사
        if ((year-e)%24 == 0) and ((year-m)%29 == 0):  # e, m을 뺐을때 나누어 떨어진다면 답
            break
        sun = sun + 1

    print(f'#{test_case} {year}')