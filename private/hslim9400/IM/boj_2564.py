def find_coord(place):  # 1차원 위치를 반환할 함수
    global c, r
    if place[0] == 1:  # 북쪽을 기준으로 동, 남, 서로 오른쪽으로 길을 펼칠 예정
        coord = place[1]  # 북쪽은 제자리에 박는다.
    elif place[0] == 4:  # 동쪽은 북쪽 길이를 더하고 동쪽 위치를 반환.
        coord = place[1] + c
    elif place[0] == 2:  # 남쪽은 북, 동쪽 길이를 더하고 남쪽에서 뺀 길이를 반환.
        coord = (c-place[1]) + c + r  # 오른쪽으로 펼치면 남쪽은 반대에서 출발하기 때문
    else:
        coord = (r-place[1]) + 2*c + r  # 서쪽은 북, 동, 남쪽 길이를 더하고 서쪽에서 뺀 길이를 반환.
    return coord


c, r = map(int, input().split())
N = int(input())
stores = []
for _ in range(N):
    stores.append(list(map(int, input().split())))
me = list(map(int, input().split()))
my_coord = find_coord(me)  # 나의 1차원 좌표를 찾는다.
dist_sum = 0  # 출력할 최종 거리 합

for i in range(N):
    store = find_coord(stores[i])  # 상점의 1차원 좌표를 찾는다.
    dist_1 = abs(my_coord - store)  # 1차원 좌표상의 거리
    dist_2 = 2*c + 2*r - dist_1  # 반대로 가면 둘레에서 첫 거리를 빼면 된다.
    dist_sum += min(dist_1, dist_2)  # 둘 중 작은 값이 최소 거리이다.
print(dist_sum)
