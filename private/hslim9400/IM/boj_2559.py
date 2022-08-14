N, K = map(int, input().split())
temps = list(map(int, input().split()))
new_sum = sum(temps[:K])  # 첫구간 합을
max_sum = new_sum  # 초기 최댓값으로 설정

for i in range(1, N-K+1):  # 이후 구간합
    # 이전 구간의 첫 숫자를 빼고 이번 구간의 뒷 숫자를 합한다.
    new_sum = new_sum - temps[i-1] + temps[i+K-1]
    if new_sum > max_sum:  # 최댓값 갱신
        max_sum = new_sum
print(max_sum)
