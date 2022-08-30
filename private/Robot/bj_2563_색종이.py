# 백준 2563. 색종이
arr = [0] * 100 * 100
papers = int(input()) # 색종이의 수
for tc in range(papers):
    xc, xr = map(int, input().split()) # 시작점 (3, 7) (15, 7) (5, 2)
    for i in range(10):
        arr[(xr + i) * 100 + xc:(xr + i) * 100 + xc + 10] = [1] * 10
print(arr.count(1))

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr[3:6] = [0] * 3
# print(arr)