'''
숫자리스트에서 한개를 추출해서 가장 앞에 두고 나머지를 재귀설정
숫자가 한개만 있다면 자신을 돌려주며 재귀를 종료한다.
'''


def permutation(cards):
  if len(cards) == 1:  # 숫자가 한개라면 재귀 종료
    return [cards]
  permutations = []
  for i in range(len(cards)):
    for perm in permutation(cards[:i] + cards[i+1:]):  # 한개를 제외한 나머지 숫자들로 만든 순열을 불러온다.
      element = [cards[i]] + perm  # 추출한 숫자를 가장 앞에 두고 나머지를 붙인게 순열 한개
      permutations.append(element)

  return permutations


T = int(input())

for test_case in range(1, T+1):
  
  total_cards = list(range(1, 19))
  cards1 = list(map(int, input().split()))
  cards2 = list(set(total_cards)-set(cards1))

  permutations = permutation(cards2)  # 순열 생성, 9!개
  win_count = 0
  lose_count = 0

  for perm in permutations:  # 하나하나 열어본다
    point1 = [0] * 9  # 점수저장 리스트
    point2 = [0] * 9
    for i in range(9):  # i마다 라운드 진행행
     if cards1[i] > perm[i]:  # 이긴 쪽이 점수 합을 가져감
        point1[i] = cards1[i] + perm[i]
      else:
        point2[i] = cards1[i] + perm[i]

    if sum(point1) > sum(point2):  # 이기면 승수+1
      win_count = win_count + 1
    else:
      lose_count = lose_count + 1

  print(win_count, lose_count)
