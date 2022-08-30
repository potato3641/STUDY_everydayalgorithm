# 백준 10163 색종이 53점..?
# 4:30부터 5:01
# [1] 53점
# matrix = [[0] * 1001 for _ in range(1001)]
# papers = list(range(1, int(input()) + 1)) # [1, 2]
# count = [0] * len(papers)
# maxr = 0
# maxc = 0
# # 색종이 올리기
# for tc in range(len(papers)):
#     xc, xr, w, h = map(int, input().split()) # 좌하단좌표, 너비, 높이
#     if xc + h - 1 > maxc:
#         maxc = xc + h - 1
#     if xr + w -1 > maxr:
#         maxr = xr + w -1
#     for i in range(h): # 10
#         for j in range(w): # 10
#             matrix[xr+i][xc+j] = papers[tc]
# # 면적 세기
# for i in papers: # [1, 2, 3]
#     for j in matrix: # [[1, 1, 1, 1, 1]]
#         count[i-1] += j.count(i)
#     print(count[i-1])
# # [2] for문 하나 줄여서 100점
# matrix = [[0] * 1001 for _ in range(1001)]
# papers = list(range(1, int(input()) + 1)) # [1, 2]
# count = [0] * len(papers)
# maxr = 0
# maxc = 0
# # 색종이 올리기
# for tc in range(len(papers)):
#     xc, xr, w, h = map(int, input().split()) # 좌하단좌표, 너비, 높이
#     if xc + h - 1 > maxc:
#         maxc = xc + h - 1
#     if xr + w -1 > maxr:
#         maxr = xr + w -1
#     for i in range(h): # 10
#         matrix[xr+i][xc:xc+w] = [papers[tc]] * w
# # 면적 세기
# for i in papers: # [1, 2, 3]
#     for j in matrix: # [[1, 1, 1, 1, 1]]
#         count[i-1] += j.count(i)
#     print(count[i-1])
# [3] 1차원 리스트로 만들기
arr = [0] * 1001 * 1001
papers = int(input()) # 색종이의 수
for tc in range(papers):
    xc, xr, w, h = map(int, input().split())
    for i in range(h):
        arr[(xr + i) * 1001 + xc:(xr + i) * 1001 + xc + w] = [tc+1] * w
for i in range(papers):
    print(arr.count(i+1))


