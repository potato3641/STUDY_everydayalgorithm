import sys
sys.stdin = open("_7985input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
def tri(line, n, lvl):
    target = 2**(n-1)-1
    if n < lvl:
        return
    if n == lvl:
        return [line[target]]
    if len(line) == 1:
        return [line[0]]
    return tri(line[:target], n-1, lvl) + tri(line[target+1:], n-1, lvl)
for test_case in range(1, T + 1):
    K = int(input())
    k = K + 0
    line = list(map(int,input().split()))
    print(f'#{test_case} ', end='')
    for i in range(K,0,-1):
        rst = tri(line, K, i)
        for j in range(len(rst)):
            print(f'{rst[j]} ',end='')
        print()