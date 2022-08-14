for test_case in range(4):
    x_1, y_1, p_1, q_1, x_2, y_2, p_2, q_2 = list(map(int, input().split()))
    if (x_1 > p_2) or (x_2 > p_1) or (y_1 > q_2) or (y_2 > q_1):
        ans = 'd'
    elif ((x_1 == p_2) or (x_2 == p_1)) and ((y_1 == q_2) or (y_2 == q_1)):
        ans = 'c'
    elif (x_1 == p_2) or (x_2 == p_1) or (y_1 == q_2) or (y_2 == q_1):
        ans = 'b'
    else:
        ans = 'a'
    print(ans)
