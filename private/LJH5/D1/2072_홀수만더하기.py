T = int(input())
for tc in range(1, T+1):
    input_arr = list(map(int, input().split()))
    result = 0
    for i in range(len(input_arr)):
        # 홀수만 더하기
        if input_arr[i] % 2:
           result += input_arr[i]
    print(f'#{tc} {result}')