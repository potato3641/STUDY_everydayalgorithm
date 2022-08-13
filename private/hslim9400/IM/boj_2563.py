N = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())  # 사각형 꼭지점 좌표를 저장
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] += 1  # 사각형에 해당하는 부분이 0이 아니면 됨

area = 0
for i in range(100):
    for j in range(100):
        if board[i][j] != 0:  # 0이 아니라면
            area += 1  # 종이가 있는 부분
print(area)