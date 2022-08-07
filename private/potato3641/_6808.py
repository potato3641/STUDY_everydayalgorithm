import sys
sys.stdin = open("_6808input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    mine = list(map(int,input().split()))
    your = list(set([i+1 for i in range(18)])-set(mine))
    