# 14692 통나무 자르기
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    winner = 'Alice'
    if n % 2:
        winner = 'Bob'
    print(f'#{tc} {winner}')