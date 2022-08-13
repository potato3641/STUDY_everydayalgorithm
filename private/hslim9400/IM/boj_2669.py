board = [[0]*100 for _ in range(100)]  # 빈 2차원 배열 생성
recs = []
for _ in range(4):
    recs.append(list(map(int, input().split())))

for rec in recs:
    for i in range(min(rec[0], rec[2]), max(rec[0], rec[2])):  # 사각형을 이루는 좌표에 1씩 더해주기
        for j in range(min(rec[1], rec[3]), max(rec[1], rec[3])):
            board[i][j] += 1
ans = 0
for i in range(100):  # 배열에 숫자가 있다면 합집합에 포함
    for j in range(100):
        if board[i][j]:
            ans += 1

print(ans)
