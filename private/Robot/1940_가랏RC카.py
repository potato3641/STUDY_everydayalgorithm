# 1940. 가랏! RC카! (D2)
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    speed = 0
    answer = 0
    for i in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0
        answer += speed
    print(f'#{tc} {answer}')