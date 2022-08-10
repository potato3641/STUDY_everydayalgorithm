import sys
sys.stdin = open("_7532input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    S, E, M = map(int,input().split())
    line = [i*365+S for i in range(24*29)]
    # 365 24 29의 공배수를 구하기 위한 365의 배수 연도 리스트
    # 365의 배수들에 S가 더해짐
    basket1 = [i for i in line if not ((i-E)%24 or (i-M)%29)]
    # 24와 29의 공배수인 경우만 담기
    # line에서 각각 E와 M을 빼고 24와 29로 나눠서 나머지가 둘 다 0인 경우만
    print(f'#{test_case} {basket1[0]}')