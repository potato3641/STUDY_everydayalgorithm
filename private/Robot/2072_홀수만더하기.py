T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    count = 0
    for i in number:
        if i % 2:
            count += i
    print(f'#{tc} {count}')