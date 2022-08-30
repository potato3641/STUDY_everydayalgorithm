# 백준 2578 빙고 9:16-10:30 / 10:15~
# arr = [list(map(int, input().split())) for _ in range(5)]
# check = []
# bingo = 0
# answer = 0
# # [1] 철수 빙고판은 이차원 리스트로, 사회자 숫자는 1차원리스트로 만든다.
# for _ in range(5):
#     check2 = list(map(int, input().split()))
#     check += check2
# # [2] 사회자 숫자를 들고 빙고판을 돌면서 같으면 0으로 표시
# num = 0
# while num < 25:
#     answer += 1
#     for i in range(5):
#         if check[num] in arr[i]:
#             for j in range(5):
#                 if arr[i][j] == check[num]:
#                     arr[i][j] = 0
# # [3] 0을 그렸을 때, 빙고인지 확인
#                     if sum(arr[i]) == 0:
#                         bingo += 1
#                     if sum(list(map(list, zip(*arr)))[j]) == 0:
#                         bingo += 1
#                     if i == j and arr[1][1] == arr[2][2] == arr[3][3] == arr[4][4] == arr[0][0]:
#                         bingo += 1
# # 이게 한 번 되면 모든 순간에 카운트 되서 안 되네
#                     if arr[1][3] == arr[2][2] == arr[3][1] == arr[4][0] == arr[0][4]:
#                         bingo += 1
#                     if bingo == 3:
#                         print(answer)
#                         num = 25
#                     break
#         else:
#             continue #break가 아니라 continue
#         if num == 25:
#             break
#     else:
#         num += 1

def check_bingo(n):
    cnt = 0
    for r in range(5):
        if bingo[r] == [0] * 5:
            cnt += 1
            if cnt > 2:
                return cnt
        if list(map(list, zip(*bingo)))[r] == [0] * 5:
            cnt += 1
            if cnt > 2:
                return cnt
    for r in range(5):
        if bingo[r][r] == 0:
            continue
        else:
            break
    else:
        cnt += 1
        if cnt > 2:
            return cnt

    for r in range(5):
        if bingo[r][4-r] == 0:
            continue
        else:
            break
    else:
        cnt += 1
        if cnt > 2:
            return cnt
    return cnt


bingo = [list(map(int, input().split())) for _ in range(5)]
# zip_bingo = list(map(list, zip(*bingo)))
number = [] # 사회자 번호 리스트
for _ in range(5):
    number += list(map(int, input().split()))
answer = 0
for num in number:
    for i in range(5):
        if num in bingo[i]:
            idx = bingo[i].index(num)
            bingo[i][idx] = 0
        else:
            continue
    if check_bingo(num) > 2:
        answer = number.index(num) + 1
        break
print(answer)

