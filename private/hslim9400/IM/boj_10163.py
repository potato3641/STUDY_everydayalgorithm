N = int(input())
recs = [0] * (N+1)
board = [[0]*1001 for _ in range(1001)]

for k in range(1, N+1):
    rec = list(map(int, input().split()))
    for i in range(rec[0], rec[0]+rec[2]):
        for j in range(rec[1], rec[1]+rec[3]):
            board[i][j] = k

for i in range(1001):
    for j in range(1001):
        recs[board[i][j]] += 1
print(*recs[1:])
