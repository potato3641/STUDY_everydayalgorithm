w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# 가로, 세로를 독립적으로 확인해도 되는데 길이의 두배만큼 움직이면 원위치로 돌아오고, 바라보는 방향도 같다.
# 따라서 이로 나눈 나머지만큼만 시행해도 결과가 같다.
w_move = t % (2*w)
h_move = t % (2*h)
dw = [1, -1]  # 움직일 방향
dh = [1, -1]
d = 0

for _ in range(w_move):  # 1차원 달팽이
    p = p + dw[d]
    if p == w:  # 벽을 보면 돌아선다.
        d = 1
    elif p == 0:
        d = 0
d = 0
for _ in range(h_move):
    q = q + dh[d]
    if q == h:
        d = 1
    elif q == 0:
        d = 0
print(p, q)
