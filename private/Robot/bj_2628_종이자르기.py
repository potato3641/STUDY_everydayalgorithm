# 백준 2628 종이자르기 35분
def max_length(line_lst):
    line_lst.sort()
    line_lst_size = []
    for i in range(len(line_lst) - 1):
        line_lst_size.append(line_lst[i + 1] - line_lst[i])
    return max(line_lst_size)


w, h = map(int, input().split())
n = int(input()) #자를 횟수
w_list = [0, w]
h_list = [0, h]
for tc in range(1, n + 1):
    direction, line = map(int, input().split()) # 0은 가로, 1은 세로, 몇 번 줄
    if direction:
        w_list.append(line)
    else:
        h_list.append(line)

print(max_length(w_list) * max_length(h_list))


