# 별, 동그라미, 네모, 세모 : 4, 3, 2, 1
def fight(a, b):
    a_dict = {
        4: 0, 3: 0, 2: 0, 1: 0
        }
    b_dict = {
        4: 0, 3: 0, 2: 0, 1: 0
        }
    for i in a:
        a_dict[i] += 1
    for i in b:
        b_dict[i] += 1
    cnt = 0
    for i in range(4, 0, -1):
        if a_dict[i] == 0 and b_dict[i] == 0:
            cnt += 1 # 이걸 안 쓰면 모양이 한 개일때 return 값이 없다.
            continue
        elif a_dict[i] > b_dict[i]:
            return 'A'
        elif a_dict[i] < b_dict[i]:
            return 'B'
        elif a_dict[i] == b_dict[i]: # 하나만 같을 때가 아니라 전부가 같을 때
            cnt += 1
    if cnt == 4:
        return 'D'

N = int(input()) #총 라운드
for tc in range(1, N+1):
    len_Aa, *Aa = map(int, (input().split()))
    len_Bb, *Bb = map(int, (input().split())) # int, list

    print(fight(Aa, Bb))