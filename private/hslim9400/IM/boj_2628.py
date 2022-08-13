x, y = map(int, input().split())
N = int(input())

horizontal = [0, x]
vertical = [0, y]

for _ in range(N):
    axis, line = map(int, input().split())
    if axis == 1:
        horizontal.append(line)
    else:
        vertical.append(line)

horizontal.sort()
vertical.sort()
areas = []
for i in range(len(horizontal)-1):
    for j in range(len(vertical)-1):
        areas.append((horizontal[i+1]-horizontal[i]) * (vertical[j+1]-vertical[j]))
print(max(areas))