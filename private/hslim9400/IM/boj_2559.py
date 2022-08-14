N, K = map(int, input().split())
temps = list(map(int, input().split()))
new_sum = sum(temps[:K])
max_sum = new_sum

for i in range(1, N-K+1):
    new_sum = new_sum - temps[i-1] + temps[i+K-1]
    if new_sum > max_sum:
        max_sum = new_sum
print(max_sum)
