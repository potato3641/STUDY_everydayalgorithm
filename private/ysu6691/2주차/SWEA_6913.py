import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):

    # 사람 수와 문제 수를 각각 N, M에 저장
    N, M = map(int, input().split())

    # 문제 풀이 여부 담을 매트릭스 생성
    solve_matrix = []

    # 사람 수 만큼 돌면서, 각 사람마다의 점수를 리스트에 저장
    # 저장한 리스트를 매트릭스에 저장
    for n in range(N):
        solve_list = list(map(int, input().split()))
        solve_matrix.append(solve_list)

    # 최고 점수를 저장할 변수 생성
    max_score = 0

    # 각 점수를 확인하고, 최고 점수를 갱신
    for person in solve_matrix:
        if sum(person) >= max_score:
            max_score = sum(person)    
            
    # 1등인 사람 수를 저장할 변수 생성
    max_people = 0

    # 매트릭스를 돌면서, 최고점수에 해당하는 사람 수를 갱신
    for person in solve_matrix:
        if sum(person) == max_score:
            max_people += 1

    print(f'#{t} {max_people} {max_score}')


'''
#1 1 3
#2 4 4
#3 4 3
#4 1 0
'''