def concat(dice, bottom):
    global dice_map
    bottom_idx = dice.index(bottom)
    top = dice[dice_map[bottom_idx]]
    sides = []
    for k in range(6):
        if dice[k] == bottom or dice[k] == top:
            continue
        sides.append(dice[k])
    return max(sides), top


N = int(input())
dices = []
dice_map = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
for _ in range(N):
    new_dice = list(map(int, input().split()))
    dices.append(new_dice)
max_sum = 0
for i in range(6):
    sums = 0
    bottom = dices[0][i]
    for j in range(N):
        front, bottom = concat(dices[j], bottom)
        sums = sums + front
    if sums > max_sum:
        max_sum = sums

print(max_sum)
