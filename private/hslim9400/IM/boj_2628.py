x, y = map(int, input().split())
N = int(input())

horizontal = [0, x]  # 가로 축
vertical = [0, y]  # 세로 축

for _ in range(N):
    axis, line = map(int, input().split())  # 축과 선을 저장
    if axis == 1:
        horizontal.append(line)  # 축이 1이라면 세로로 자름, 즉 가로로 나뉘어 짐
    else:
        vertical.append(line)

horizontal.sort()  # 구간으로 나눌 것이므로 정렬해줌 [0, 100, 20]이런 식이면 안됨
vertical.sort()
areas = []
for i in range(len(horizontal)-1):
    for j in range(len(vertical)-1):  # 정렬한 가로길이와 높이들을 곱해 넓이를 저장
        areas.append((horizontal[i+1]-horizontal[i]) * (vertical[j+1]-vertical[j]))
print(max(areas))  # 최댓값을 출력
