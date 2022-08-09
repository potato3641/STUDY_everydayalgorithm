def permutation(cards):
  if len(cards) == 1:
    return [cards]
  permutations = []
  for i in range(len(cards)):
    for perm in permutation(cards[:i] + cards[i+1:]):
      element = [cards[i]] + perm
      permutations.append(element)

  return permutations

T = int(input())

for test_case in range(1, T+1):
  
  total_cards = list(range(1, 19))
  cards1 = list(map(int, input().split()))
  cards2 = list(set(total_cards)-set(cards1))

  permutations = permutation(cards2)
  win_count = 0
  lose_count = 0

  for perm in permutations:
    point1 = [0] * 9
    point2 = [0] * 9
    for i in range(9):
      if cards1[i] > perm[i]:
        point1[i] = cards1[i] + perm[i]
      else:
        point2[i] = cards1[i] + perm[i]

    if sum(point1) > sum(point2):
      win_count = win_count + 1
    else:
      lose_count = lose_count + 1

  print(win_count, lose_count)
