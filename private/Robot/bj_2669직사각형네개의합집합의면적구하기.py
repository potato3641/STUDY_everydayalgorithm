matrix = [[0] * 101 for _ in range(101)]
maxydc = 0 # 가로
maxydr = 0 # 세로
count = 0
for _ in range(4):
    xdc, xdr, ydc, ydr = map(int, input().split())
    if ydc > maxydc:
        maxydc = ydc
    if ydr > maxydr:
        maxydr = ydr
    for i in range(xdr, ydr):
        for j in range(xdc, ydc):
            matrix[i][j] = 1
for i in range(maxydr+1):
    for j in range(maxydc+1):
        if matrix[i][j]:
            count += 1
print(count)
