def permutation(cards):
  if len(cards) == 1:  # 재귀 종료 조건
    return [cards]
  permutations = []
  '''
  [1,2,3]로 순열을 만들고 싶다면
  1을 뽑아서 앞에 두고 [2,3]로 순열을 만든다.
  [2,3]에서 2를 뽑고 3을 반환하면 [1,2,3]
  3을 뽑고 2를 반환하면 [1,3,2]
  처음으로 돌아가 2를 뽑고 [1,3]으로 순열을 만들면
  [2,1,3], [2,3,1]. 3에 대해서도 시행하면 두개가 더
  나와서 총 여섯개의 순열을 만들 수 있다.
  '''
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

  permutations = permutation(cards2)  # 모든 순열 생성
  win_count = 0
  lose_count = 0

  for perm in permutations:
    point1 = [0] * 9  # 점수 저장용
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
