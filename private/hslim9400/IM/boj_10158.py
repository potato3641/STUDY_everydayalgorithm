w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

w_move = t % (2*w)
h_move = t % (2*h)
dw = [1, -1]
dh = [1, -1]
d = 0

for _ in range(w_move):
    p = p + dw[d]
    if p == w:
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
