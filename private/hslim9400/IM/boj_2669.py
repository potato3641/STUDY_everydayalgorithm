board = [[0]*100 for _ in range(100)]
recs = []
for _ in range(4):
    recs.append(list(map(int, input().split())))

for rec in recs:
    for i in range(min(rec[0], rec[2]), max(rec[0], rec[2])):
        for j in range(min(rec[1], rec[3]), max(rec[1], rec[3])):
            board[i][j] += 1
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            ans += 1

print(ans)
