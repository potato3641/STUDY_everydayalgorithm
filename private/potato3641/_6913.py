import sys
sys.stdin = open("input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    max_num = 0
    max_cnt = 0
    for i in range(N):
        line = list(map(int,input().split()))
        if sum(line) > max_num:
            max_num = sum(line)
            max_cnt = 1
        elif sum(line) == max_num:
            max_cnt += 1
    print(f'#{test_case} {max_cnt} {max_num}')