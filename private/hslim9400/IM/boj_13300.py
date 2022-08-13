N, K = map(int, input().split())
building = [[], []]  # 학생들이 들어갈 건물, 성별로 나눔
for _ in range(6):
    building[0].append([])  # 학년별로 방 생성
    building[1].append([])

for _ in range(N):  # 학생들을 정보에 맞게 넣어줌
    student = list(map(int, input().split()))
    building[student[0]][student[1]-1].append(1)

rooms = 0
for i in range(6):  # 방 개수 세기
    if len(building[0][i]) % K:  # 방별로 학생수를 최대인원으로 나눈 몫을 더하고,
        # 나머지가 있을 경우 1을 더 더함
        rooms += len(building[0][i]) // K + 1
    else:
        rooms += len(building[0][i]) // K
    if len(building[1][i]) % K:
        rooms += len(building[1][i]) // K + 1
    else:
        rooms += len(building[1][i]) // K

print(rooms)