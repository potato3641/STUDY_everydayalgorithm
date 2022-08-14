N = int(input())
bounds = []
for _ in range(6):
    bounds.append(list(map(int, input().split())))
x = []
y = []

for i in range(3):
    x.append(bounds[2*i][1])
    y.append(bounds[2*i + 1][1])
max_x_idx = x.index(max(x))  # 가로 중 긴 놈을 찾는다.
max_y_idx = y.index(max(y))  # 세로 중 긴 놈을 찾는다. 이 두 인덱스는 인접해있음.
matches = {(0, 0): (3, 4), (1, 0): (4, 5),  # 인접한 긴 선의 인덱스와 먼 짧은 애들 인덱스
           (1, 1): (5, 0), (2, 1): (0, 1),
           (2, 2): (1, 2), (0, 2): (2, 3)}
min_idx1, min_idx_2 = matches[max_x_idx, max_y_idx]

total_area = max(x)*max(y) - bounds[min_idx1][1]*bounds[min_idx_2][1]
print(N * total_area)