T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxkill = 0
    for r in range(n-(m-1)):
        for c in range(n-(m-1)):
            count = 0
            for i in range(m):
                for j in range(m):
                    count += arr[r+i][c+j]
            if count > maxkill:
                maxkill = count
    print(f'#{tc} {maxkill}')