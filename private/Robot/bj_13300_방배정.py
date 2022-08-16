# 백준 13300 방배정
n, k = map(int, input().split())
room = {
    '1 1':0, '1 2':0, '1 3':0, '1 4':0, '1 5':0, '1 6':0,
    '0 1':0, '0 2':0, '0 3':0, '0 4':0, '0 5':0, '0 6':0,
}
person = [input() for _ in range(n)]
for i in person:
    room[i] += 1
count = 0
for j in room.values():
    if j % k:
        count += (j // k + 1)
    else:
        count += j // k
print(count)

