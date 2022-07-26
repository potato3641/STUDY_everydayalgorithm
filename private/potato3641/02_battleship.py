import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea, thfv, *val):
    pass
    h, v = index
    if len(val) != 1:
        val = 1
    else:
        val = val[0]
    if thfv:
        sea[h][v:v+3] = [val,val,val]
    else:
        sea[h][v] = val
        sea[h+1][v] = val
        sea[h+2][v] = val

def is_ship(index, sea, thfv):
    pass
    h, v = index
    if thfv:
        if sea[h][v] or sea[h][v+1] or sea[h][v+2]:
            return True
    else:
        if sea[h][v] or sea[h+1][v] or sea[h+2][v]:
            return True
    return False
def get_ship_coord(index, thfv):
    h, v = index
    if thfv:
        return {(h,v),(h,v+1),(h,v+2)}
    else:
        return {(h,v),(h+1,v),(h+2,v)}
def view_info(arr):
    for i in arr:
        print(i)
def view_info_tf(arr):
    for i in arr:
        print('[', end='')
        for j in i:
            if j:
                print(' ■',end='')
            else:
                print(' □',end='')
        print(' ]')

############## 보드 크기 N, 배 수량 S ################
N = 6
S = 2
if N**2/5 < S*3:
    input('배는 해역의 20% 이상을 차지할 수 없습니다.')

player_sea = [[0] * N for _ in range(N)]  # 플레이어의 해역
player_attacked = [[False] * N for _ in range(N)] # 플레이어의 공격 위치 기록
player_ship_info = set()

computer_sea = [[0] * N for _ in range(N)]  # 컴퓨터의 해역
computer_sea_prev = [[0] * N for _ in range(N)]  # 컴퓨터의 해역
computer_attacked = [[False] * N for _ in range(N)]  # 컴퓨터의 공격 위치 기록
computer_ship_info = set()

round = 1  # 게임 라운드

player_ship_cnt = 0
# 1. 게임 준비
while True:
    pass
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_loc = tuple(map(int,input('배를 위치시킬 시작점을 고르세요. : ').split()))
    player_tf = bool(int(input('가로로 위치시키려면 1, 아니면 0을 입력하세요. : ')))
    # 1-2) 범위를 벗어난 시작점을 고른 경우
    for i in range(2):
        if player_loc[i] < 0 or player_loc[i] > (N-2):
            print('-----해당 위치에는 배를 둘 수 없습니다.-----')
        else:
            break
    if not is_ship((player_loc[0]-1, player_loc[1]-1),player_sea,player_tf):
        set_ship((player_loc[0]-1, player_loc[1]-1),player_sea,player_tf)
        player_ship_info.add(((player_loc[0]-1, player_loc[1]-1),player_tf))
        player_ship_cnt += 1
    if player_ship_cnt >= S:
        break

computer_ship_cnt = 0
while True:
# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
    computer_loc = (random.randrange(0,(N-2)), random.randrange(0,(N-2)))
    computer_tf = random.choice([True, False])
    if not is_ship(computer_loc,computer_sea,computer_tf):
        set_ship(computer_loc,computer_sea,computer_tf)
        set_ship(computer_loc,computer_sea_prev,computer_tf)
        computer_ship_info.add((computer_loc,computer_tf))
        computer_ship_cnt += 1
    if computer_ship_cnt >= S:
        break
# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
# 2. 라운드 진행
while True:
    pass
    # 2-1) 플레이어 공격
    print()
    print('-'*100)
    print('< Information Board >')
    print(f'플레이어의 해역 : ')
    view_info(player_sea)
    print(f'플레이어의 공격 기록 : ')
    view_info_tf(player_attacked)
    print('-'*100)
    print()
    # 2-2) 플레이어의 공격 위치 선택
    player_target = (-1, -1)
    while True:
        cont_flag = False
        player_target = tuple(map(int,input('공격할 위치를 선택하세요. "x y" : ').split()))
        for i in range(2):
            if player_target[i] < 1 or player_target[i] > N:
                print('\n해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해 주세요.')
                cont_flag = True
                break
        if cont_flag: continue
        if player_attacked[player_target[0]-1][player_target[1]-1]:
            print('\n이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요.')
            continue
        else:
            break
    print(f'\n<{round}라운드 결과!>')
    if computer_sea[player_target[0]-1][player_target[1]-1]:
    # 2-3) 플레이어의 공격이 성공한 경우
        for coord, tf in computer_ship_info:
            if (player_target[0]-1, player_target[1]-1) in get_ship_coord(coord, tf):
                set_ship(coord,computer_sea,tf,0)
                computer_ship_cnt -= 1
        player_attacked[player_target[0]-1][player_target[1]-1] = True
        print(f'플레이어는 컴퓨터의 해역 {player_target[0]}, {player_target[1]} 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.')
        print(f'컴퓨터의 배는 {computer_ship_cnt}개 남았습니다.')
        if not computer_ship_cnt:
            print(f'컴퓨터의 해역 : ')
            view_info(computer_sea_prev)
            print(f'게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!')
            break
    # 2-4) 플레이어의 공격이 실패한 경우
    else:
        print(f'플레이어는 컴퓨터의 해역 {player_target[0]}, {player_target[1]} 칸을 공격하였으나, 공격에 실패하였습니다!')
        player_attacked[player_target[0]-1][player_target[1]-1] = True
    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    computer_target_list = [[] for _ in range(N)]
    for i in range(N):
        computer_target_list[i].append(i)
        for j in range(N):
            if not computer_attacked[i][j]:
                computer_target_list[i].append(j)
    tlrow = random.randrange(0,N)
    while len(computer_target_list[tlrow]) < 2:
        tlrow = random.randrange(0,N)
    tlcol = random.randrange(1,len(computer_target_list[tlrow]))
    computer_target = tlrow, computer_target_list[tlrow][tlcol]
    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[computer_target[0]][computer_target[1]]:
        for coord, tf in player_ship_info:
            if (computer_target[0], computer_target[1]) in get_ship_coord(coord, tf):
                set_ship(coord,player_sea,tf,0)
                player_ship_cnt -= 1
        computer_attacked[computer_target[0]][computer_target[1]] = True
        print(f'컴퓨터는 플레이어의 해역 {computer_target[0]+1}, {computer_target[1]+1} 칸을 공격하였고, 플레이어의 배는 피격되었습니다.')
        print(f'플레이어의의 배는 {player_ship_cnt}개 남았습니다.')
        if not player_ship_cnt:
            print(f'게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!')
            break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    else:
        print(f'컴퓨터는 플레이어의 해역 {computer_target[0]+1}, {computer_target[1]+1} 칸을 공격하였으나, 공격에 실패하였습니다!')
        computer_attacked[computer_target[0]][computer_target[1]] = True
    round += 1
