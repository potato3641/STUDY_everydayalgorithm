# 전체 케이스 개수를 받는다.
T = int(input()) 

# 첫 케이스 = 1을 선언하고 이하 while 문으로 T만큼 돌린다.
case_count = 1
while case_count <= T:

    # 파리가 놓일 판의 크기와, 때릴 파리채의 사이즈 값을 받는다.
    wide, size = map(int,input().split())

    # 파리가 판의 각각의 칸에 몇마리씩 있는지 받는다.
    fly_ground = []
    
    for i in range(wide):
        input_line = list(map(int,input().split()))
        fly_ground += [input_line]
    
    # 좌표, 잡은 파리 생성, 딕셔너리로 설정 (이는 추후 설명할 심화과정을 위함임)
    hit_fly = {}

    # (0,0)의 좌표부터 파리채가 때리는 범위가 판을 넘어가지 않는 좌표를 설정
    for x in range(int(wide-size)+1):
        for y in range(int(wide-size)+1):

            # 파리채가 잡은 파리의 수를 카운트 하는 변수 생성
            hit_count = int(0)

            # 파리패로 생성된 2차원의 각 위치에서 잡은 파리수를 모두 더함
            for r in range(size):
                for c in range(size):
                    hit_count += int(fly_ground[x+r][y+c])

            # 딕셔너리 hit_fly의 key값은 (x,y) 좌표, value는 잡은 파리의 수
            hit_fly[(x, y)] = hit_count
    
    # 파리를 가장 많이 잡을 수 있는 포인트의 시작점
    best_point = max(hit_fly, key=hit_fly.get)
    # 파리를 가장 많이 잡은 케이스의 value
    max_hit = max(hit_fly.values())

    #양식에 맞게 출력 후 케이스 카운트 +1, 다시 while 반복
    print(f'#{case_count} {max_hit}')
    case_count += 1
