N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_score = [a[1:].count(4 - i) for i in range(4)]  # a와 b의 패의 개수를 4번부터 저장
    b_score = [b[1:].count(4 - i) for i in range(4)]
    for i in range(4):  # 승패 조건, 4번부터 개수가 많은 쪽이 승리
        if a_score[i] > b_score[i]:
            print('A')
            break
        elif a_score[i] < b_score[i]:
            print('B')
            break
    else:
        print('D')