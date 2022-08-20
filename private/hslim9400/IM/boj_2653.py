def next_number(current, prev):
    global numbers
    next_num = prev - current  # 이전 숫자 - 현재 숫자 = 다음 숫자
    if next_num < 0:  # 다음 숫자가 음수라면
        return  # 종료
    numbers.append(next_num)  # 다음 숫자를 목록에 넣어준다.

    next_number(next_num, current)  # 다음 단계 진행


N = int(input())
max_count = 1
ans = [N]
for i in range(N//2, N+1):  # 절반보다 작다면 네 번째가 음수가 될 것
    numbers = [N, i]  # 두 번째 숫자를 i로 설정
    next_number(i, N)
    counts = len(numbers)
    if counts > max_count:  # 숫자 개수를 확인해 갱신한다.
        max_count = counts
        ans = numbers

print(max_count)
print(*ans)
