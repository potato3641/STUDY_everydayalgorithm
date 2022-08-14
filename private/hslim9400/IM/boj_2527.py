for test_case in range(4):
    x_1, y_1, p_1, q_1, x_2, y_2, p_2, q_2 = list(map(int, input().split()))
    # d의 조건, 한개라도 해당할 경우 사각형끼리 닿을 수 없다.
    if (x_1 > p_2) or (x_2 > p_1) or (y_1 > q_2) or (y_2 > q_1):
        ans = 'd'
    # c의 조건, 가로, 세로좌표가 하나씩 같으면 한점에서 접한다. 네 가지 경우.
    elif ((x_1 == p_2) or (x_2 == p_1)) and ((y_1 == q_2) or (y_2 == q_1)):
        ans = 'c'
    # b의 조건, d와 c가 아니면서 하나라도 같다면 선으로 접한다.
    elif (x_1 == p_2) or (x_2 == p_1) or (y_1 == q_2) or (y_2 == q_1):
        ans = 'b'
    # 전부 해당 안되면 a다.
    else:
        ans = 'a'
    print(ans)
