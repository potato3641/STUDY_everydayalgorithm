import sys
sys.stdin = open("_9480input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
def ncr(line, n):
    basket = []
    if n == len(line):
        return [''.join(line)]
    if n == 1:
        return line
    elif n > 1:
        cnt = 1
        for i in range(len(line)):
            basket.append([line[i]])
        while cnt < n:
            newbasket = []
            for j in range(len(basket)):
                for i in range(len(line)):
                    if line[i] not in basket[j]:
                        target = sorted(basket[j]+[line[i]])
                        if target not in newbasket:
                            newbasket.append(target)
            basket = newbasket[:]
            cnt += 1
        return basket
for test_case in range(1, T + 1):
    N = int(input())
    word = []
    for i in range(N):
        word.append(input())
    rst = 0
    for i in range(1, N+1):
        ncrs = ncr(word,i)
        for j in ncrs:
            if len(set(list(''.join(j)))) == 26:
                rst += 1
    print(f'#{test_case} {rst}')
        
