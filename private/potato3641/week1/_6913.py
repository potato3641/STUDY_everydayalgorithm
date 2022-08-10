import sys
sys.stdin = open("input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
for test_case in range(1, T + 1):
    N, M = map(int,input().split()) # N, M 받기
    max_num = 0
    max_cnt = 0
    for i in range(N): # 라인 수 N만큼 돌려서
        line = list(map(int,input().split()))
        if sum(line) > max_num: # 라인 합이 최대값보다 크다면
            max_num = sum(line) # 최대값 갱신
            max_cnt = 1 # 최대값의 수 갱신
        elif sum(line) == max_num: # 최대값과 같다면
            max_cnt += 1 # 최대값의 수 추가
    print(f'#{test_case} {max_cnt} {max_num}')