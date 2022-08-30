# 1859. 백만 장자 프로젝트 (D2)
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    answer = 0
    while price:
        high, high_idx = max(price), price.index(max(price))
        for i in range(high_idx):
            answer += high - price[i]
        price = price[high_idx+1:]
    print(f'#{tc} {answer}')
