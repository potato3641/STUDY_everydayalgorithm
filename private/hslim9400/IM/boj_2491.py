N = int(input())
nums = list(map(int, input().split()))
max_count = 1
dec_count = 1
inc_count = 1
for i in range(1, N):
    if nums[i] > nums[i-1]:
        dec_count = 1
        inc_count += 1
    elif nums[i] < nums[i-1]:
        inc_count = 1
        dec_count += 1
    else:
        inc_count += 1
        dec_count += 1
    if max_count < max(inc_count, dec_count):
        max_count = max(inc_count, dec_count)
print(max_count)
