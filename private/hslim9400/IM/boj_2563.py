N = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] += 1

area = 0
for i in range(100):
    for j in range(100):
        if board[i][j] != 0:
            area += 1
print(area)