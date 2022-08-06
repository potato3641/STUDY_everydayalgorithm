from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')

'''
사람마다 받는 리스트의 숫자를 합하면 푼 문제의 개수이다.
푼 문제의 개수 리스트를 만들고 최대값의 숫자를 세어 출력
'''

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

