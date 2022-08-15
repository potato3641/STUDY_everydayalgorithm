board = []
for _ in range(5):  # 빙고 보드 생성
    board.append(list(map(int, input().split())))

checks = []
for _ in range(5):  # 숫자가 들어오는 순서대로
    checks.extend(list(map(int, input().split())))

count = 0
while True:  # 한 사이클당 숫자 한개
    check = checks[count]
    bingo = 0
    cross_bingo_1 = 0  # 대각선빙고는 for문 밖에서 체크
    cross_bingo_2 = 0
    for i in range(5):  # 빙고보드에 있다면 체크 후 0으로 변경
        for j in range(5):
            if board[i][j] == check:
                board[i][j] = 0
    for i in range(5):  # 빙고를 확인하는 곳
        ver_bingo = 0
        hor_bingo = 0
        for j in range(5):
            ver_bingo += board[j][i]  # 세로 빙고
            hor_bingo += board[i][j]  # 가로 빙고
            if i == j:
                cross_bingo_1 += board[i][j]  # 대각빙고 두개
            if i == 4 - j:
                cross_bingo_2 += board[i][j]
        if ver_bingo == 0:  # 한줄을 체크 후 가로, 세로가 해당되면 빙고 + 1
            bingo += 1
        if hor_bingo == 0:
            bingo += 1
    if cross_bingo_1 == 0:  # 보드를 모두 체크 후 대각선 빙고가 있다면 빙고 + 1
        bingo += 1
    if cross_bingo_2 == 0:
        bingo += 1
    if bingo > 2:  # 빙고 개수가 3 이상이라면 종료
        break
    count += 1  # 없다면 다음 숫자
print(count + 1)
