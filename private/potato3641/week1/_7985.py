import sys
sys.stdin = open("_7985input.txt", "r")
T = int(input())
# 주석나중에쓸꺼임
def tri(line, n, lvl): # 중위 순회 트리 레벨 별 추출하는 함수
    target = 2**(n-1)-1 # 한 라인의 루트 위치 계산
    if n < lvl: # 트리 전체보다 레벨이 높으면 중단
        return
    if n == lvl: # 트리 전체와 레벨이 같으면 트리 루트 반환
        return [line[target]]
    if len(line) == 1: # 트리가 루트 하나면 루트 반환
        return [line[0]]
    return tri(line[:target], n-1, lvl) + tri(line[target+1:], n-1, lvl)
    # 루트 기준으로 왼쪽, 오른쪽 트리에서 해당 레벨 재귀 탐색하기
for test_case in range(1, T + 1):
    K = int(input())
    k = K + 0 # 넌 왜있니
    line = list(map(int,input().split()))
    print(f'#{test_case} ', end='')
    for i in range(K,0,-1): # K부터 1까지 탐색
        rst = tri(line, K, i) # i레벨 트리 탐색
        for j in range(len(rst)): # i레벨 트리 출력
            print(f'{rst[j]} ',end='')
        print()