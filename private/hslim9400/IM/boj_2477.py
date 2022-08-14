N = int(input())
bounds = []
for _ in range(6):
    bounds.append(list(map(int, input().split())))
x = []
y = []
'''
참외밭은 ㄱ자 모양을 돌려서 만든 모양으로 큰 사각형에서 빼버릴 작은 사각형이 긴 선분의 반대편에 위치한다.
또한 긴 길이는 긴 길이끼리, 빠질 사각형을 이루는 길이는 얘네끼리 이웃한다.
가로, 세로 길이 중 긴 길이를 찾아서 묶어주고 이와 이웃하지 않는 인덱스를 찾아 곱하면 
빠질 사각형의 넓이가 된다.
'''
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