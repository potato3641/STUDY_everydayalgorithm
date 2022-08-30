# 백준 2477 참외밭 11:10~
k = int(input()) # 참외개수
w = [] # 최대 가로용
h = [] # 최대 세로용
all_lst = [] # 모든 둘레 정보
stack = [] # 작은 길이 계산용
min_w = 0, 0 # 작은 길이값
for tc in range(6):
    direction, length = map(int, input().split()) # 1 60
    # 1 오른쪽으로 2 왼쪽으로 3 아래로 4 위로

# [1] 큰 네모가 될 변 구하기
    if direction == 1 or direction == 2:
        w.append(length)
    else:
        h.append(length)
# [2] 작은 네모를 구하기 위해 자료 저장
    all_lst.append((direction, length))

# [3] 작은 네모가 될 변 구하기
# 원래 자료 보존을 위해 같은 리스트를 하나 더 만들어준다.
for i in all_lst:
    stack.append(i)
# [3-1] 앞 순서의 방향과, 뒷 순서의 방향을 비교해 오른쪽으로 꺽은 것 색출
for _ in range(5):
    pre2 = stack.pop() # 3, 30
    pre1 = stack.pop()
    if (pre1[0], pre2[0]) in [(1, 3), (2, 4), (3, 2), (4, 1)]:
        min_w = pre1[1], pre2[1]
        break # 답을 찾으면 뒤도 보지 말고 탈출
    else: # 아니면 앞에 걸 다시 넣어줘서 그 앞에 거랑 비교해야함
        stack.append(pre1)
# [3-2] 5번의 방향 전환 중에 답이 없을 때, 맨 마지막 것과 맨 처음 것도 비교해야 함
else:
    min_w = all_lst[0][1], all_lst[-1][1]

# [4] 큰 네모의 크기 구하기
big_square = max(w) * max(h)
# [5] 작은 네모 구하기
sm_square = min_w[0] * min_w[1]
# [6] 잊지 말고 참외 곱하기
answer = (big_square - sm_square) * k
print(answer)