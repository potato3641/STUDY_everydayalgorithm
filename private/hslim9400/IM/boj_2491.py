N = int(input())
nums = list(map(int, input().split()))
max_count = 1
dec_count = 1  # 숫자가 한개만 있어도 카운트가 1.
inc_count = 1
for i in range(1, N):
    if nums[i] > nums[i-1]:  # 이전 숫자보다 클 경우 감소 카운트를 초기화한다.
        dec_count = 1
        inc_count += 1
    elif nums[i] < nums[i-1]:  # 작을 경우 증가 카운트를 초기화 한다.
        inc_count = 1
        dec_count += 1
    else:  # 같다면 모두 증가
        inc_count += 1
        dec_count += 1
    if max_count < max(inc_count, dec_count):  # 최대 카운트 갱신
        max_count = max(inc_count, dec_count)
print(max_count)
