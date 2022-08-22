def concat(dice, bottom):  
    global dice_map
    bottom_idx = dice.index(bottom)  # 아랫면 주사위의 인덱스를 이용해
    top = dice[dice_map[bottom_idx]]  # 윗면주사위의 숫자를 찾음
    sides = []
    for k in range(6):
        # 드러나는 면(옆면)들을 저장
        if dice[k] == bottom or dice[k] == top:
            continue
        sides.append(dice[k])
    return max(sides), top  # 여기서 윗면이 다음 주사위의 아랫면이 됨
    # 드러나는 면들 중 가장 큰 숫자가 정면


N = int(input())
dices = []
dice_map = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}  # 반대 위치의 주사위 인덱스
for _ in range(N):
    new_dice = list(map(int, input().split()))
    dices.append(new_dice)
max_sum = 0
for i in range(6):
    sums = 0
    bottom = dices[0][i]  # 바닥위치의 주사위 번호를 저장
    for j in range(N):
        front, bottom = concat(dices[j], bottom)
        sums = sums + front
    if sums > max_sum:  # 최댓값 갱신
        max_sum = sums

print(max_sum)
