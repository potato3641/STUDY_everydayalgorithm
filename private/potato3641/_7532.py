import sys
sys.stdin = open("_7532input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    S, E, M = map(int,input().split())
    line = [i*365+S for i in range(24*29)]
    basket1 = [i for i in line if not ((i-E)%24 or (i-M)%29)]
    print(f'#{test_case} {basket1[0]}')