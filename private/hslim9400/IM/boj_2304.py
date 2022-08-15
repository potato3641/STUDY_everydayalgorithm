N = int(input())
pillars = []
heights = []
max_height = 0
for _ in range(N):
    pillar = list(map(int, input().split()))
    pillars.append(pillar)
    height = pillar[1]
    if height > max_height:
        max_height = height

pillars.sort(key=lambda x: x[0])
for i in range(N):
    if pillars[i][1] == max_height:
        max_pillar = i
        break
lefts = pillars[:max_pillar+1]
rights = pillars[max_pillar:]
current = lefts[0][1]
area = 0
for i in range(1, len(lefts)):
    if current >= lefts[i][1]:
        area += (lefts[i][0] - lefts[i-1][0]) * current
    else:
        area += (lefts[i][0] - lefts[i-1][0]) * current
        current = lefts[i][1]
rights = rights[::-1]
current = rights[0][1]
for i in range(1, len(rights)):
    if current >= rights[i][1]:
        area += abs(rights[i][0] - rights[i-1][0]) * current
    else:
        area += abs(rights[i][0] - rights[i-1][0]) * current
        current = rights[i][1]
area = area + max_height
print(area)