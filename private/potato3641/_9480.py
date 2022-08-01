import sys
sys.stdin = open("_9480input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
def nCr(n, r):
    def fact(n):
        if n <= 1:
            return 1
        return fact(n-1) * n
    return fact(n)/(fact(r)*fact(n-r))
for test_case in range(1, T + 1):
    N = int(input())
    word = []
    for i in range(N):
        word.append(input())
    cnt = 0
    rst = 0
    while cnt <= N:
        basket = []
        if not cnt:
            for i in range(len(word)):
                basket.append(word[i])
        else:
            for i in range(len(word)):
                for j in range(len(word)):
                    if j > i:
                        basket.append(word[i])
            for i in range(len(word)-cnt+1):
                basket.append(word[i])
                for j in range(len(word)):
                    if word[j] not in basket[i]:
                        basket[i].append(word[j])
        print(basket, end='')
        for i in basket:
            if len(set(i)) == 26:
                rst += 1
        cnt += 1
    print(f'#{test_case} {rst}')
        
