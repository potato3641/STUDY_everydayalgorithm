T = int(input())

for test_case in range(1, T+1):
  
  N, M = list(map(int, input().split()))
  win_nums = []
  buy_nums = []
  win_money = 0
  for i in range(N):
    win_num, money = input().split()
    win_nums.append((win_num, money))
  
  for i in range(M):
    buy_num = input()
    buy_nums.append(buy_num)

  for i in range(M):
    for j in range(N):
      for k in range(8):
        if win_nums[j][0][k] == '*':
          continue
        if buy_nums[i][k] != win_nums[j][0][k]:
          break
      else:
        win_money = win_money + int(win_nums[j][1])

  print(f'#{test_case} {win_money}')

    