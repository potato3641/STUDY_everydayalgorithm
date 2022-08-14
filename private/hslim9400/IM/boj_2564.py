def find_coord(place):
    global c, r
    if place[0] == 1:
        coord = place[1]
    elif place[0] == 4:
        coord = place[1] + c
    elif place[0] == 2:
        coord = (c-place[1]) + c + r
    else:
        coord = (r-place[1]) + 2*c + r
    return coord


c, r = map(int, input().split())
N = int(input())
stores = []
for _ in range(N):
    stores.append(list(map(int, input().split())))
me = list(map(int, input().split()))
my_coord = find_coord(me)
dist_sum = 0

for i in range(N):
    store = find_coord(stores[i])
    dist_1 = abs(my_coord - store)
    dist_2 = 2*c + 2*r - dist_1
    dist_sum += min(dist_1, dist_2)
print(dist_sum)
