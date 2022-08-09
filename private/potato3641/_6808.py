import sys
sys.stdin = open("_6808input.txt", "r")
def factorial(line, mine):
    n = len(line)
    basket = []
    if n == 1:
        return line
    else:
        for i in line:
            target = set()
            target.add(i)
            withouts = list(set(line)-target)
            for j in factorial(withouts, mine):
                newbasket = []
                newbasket.append(i)
                if type(j) == type(0):
                    newbasket.append(j)
                else:
                    newbasket += j
                basket.append(newbasket)
        if len(line) == len(mine):
            wcnt, lcnt = 0, 0
            for i in basket:
                w = 0
                l = 0
                for j in range(len(i)):
                    if mine[j] > i[j]:
                        w += mine[j] + i[j]
                    else:
                        l += mine[j] + i[j]
                if w > l:
                    wcnt += 1
                else:
                    lcnt += 1
            return wcnt, lcnt
        return basket
T = int(input())
for test_case in range(1, T + 1):
    mine = list(map(int,input().split()))
    your = list(set([i+1 for i in range(18)]) - set(mine))
    w, l = factorial(your, mine)
    print(f'#{test_case} {w} {l}')
    