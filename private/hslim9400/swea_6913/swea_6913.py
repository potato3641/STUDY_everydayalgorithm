from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(T):
    
    N, M = list(map(int, input().split()))
    scores = []
    for i in range(N):
        score = sum(list(map(int, input().split())))
        scores.append(score)

    max_score = max(scores)
    winners = scores.count(max_score)

    print(winners, max_score)

