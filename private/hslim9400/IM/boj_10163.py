N = int(input())
recs = [0] * (N+1)  # 답으로 낼 리스트
board = [[0]*1001 for _ in range(1001)]  # 빈 배열 생성

for k in range(1, N+1):
    rec = list(map(int, input().split()))
    for i in range(rec[0], rec[0]+rec[2]):  # 사각형의 좌표에 해당하면 해당 사각형 번호를 덮어씌움
        for j in range(rec[1], rec[1]+rec[3]):
            board[i][j] = k

for i in range(1001):  # 어떤 사각형이 있는지 확인
    for j in range(1001):
        recs[board[i][j]] += 1  # 해당 사각형의 개수(넓이)를 증가시켜줌
print(*recs[1:])
