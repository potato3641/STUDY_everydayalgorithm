T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    fly_arr = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    # x는 파리채가 갈수 있는 영역
    for r in range(n - m + 1):
        for c in range(n - m + 1):
            sum_fly = 0
            # 파리채 영역 안을 이동하면서 잡기
            for dr in range(m):
                for dc in range(m):
                    sum_fly += fly_arr[r+dr][c+dc]
            if max_fly < sum_fly:
                max_fly = sum_fly
    print(f'#{tc} {max_fly}')