T = int(input())

for test_case in range(1, T+1):
  
  N, M = list(map(int, input().split()))
  win_nums = []
  buy_nums = []
  win_money = 0
  for i in range(N):
    win_num, money = input().split()
    win_nums.append((win_num, money))  # 당첨번호와 상금을 동시에 저장, 딕셔너리로 될만도?
  
  for i in range(M):  # 얘가 산 복권 번호를 저장
    buy_num = input()
    buy_nums.append(buy_num)

  for i in range(M):  # 모든 당첨번호
    for j in range(N):  # 내가 산 복권
      for k in range(8):  # 모든 번호
        if win_nums[j][0][k] == '*':  # 모든 숫자가 가능하므로
          continue
        if buy_nums[i][k] != win_nums[j][0][k]:  # 하나라도 틀리면 당첨 아님
          break
      else:
        win_money = win_money + int(win_nums[j][1])  # 당첨

  print(f'#{test_case} {win_money}')

    