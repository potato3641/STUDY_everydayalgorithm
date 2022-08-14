R, C = map(int, input().split())
target = int(input())
board = [[0]*C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
r, c = 0, 0
count = 1

ans = [0]
for _ in range(R*C):  # 달팽이
    board[r][c] = count
    if count == target:  # 표적 번호를 받으면 종료, 문제는 (1,1)이 기준이기 때문에 1씩 더한다.
        ans = [r+1, c+1]
    if (0 <= r+dr[d] < R) and (0 <= c+dc[d] < C) and (board[r+dr[d]][c+dc[d]]) == 0:
        pass
    else:
        d = (d + 1) % 4
    r = r + dr[d]
    c = c + dc[d]
    count += 1
print(*ans)
