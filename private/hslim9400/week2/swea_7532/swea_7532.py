from re import S


T = int(input())

for test_case in range(T):
    s, e, m = list(map(int, input().split()))

    sun = 0
    while True:
        year = 365 * sun + s
        if ((year-e)%24 == 0) and ((year-m)%29 == 0):
            break
        sun = sun + 1

    print(f'#{test_case} {year}')