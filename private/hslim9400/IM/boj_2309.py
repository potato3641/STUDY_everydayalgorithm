hobbits = []
for _ in range(9):
    hobbits.append(int(input()))

ans = []
flag = True
for i in range(9):
    if not flag:
        break
    hobbits_8 = hobbits[:i] + hobbits[i+1:]
    for j in range(8):
        hobbits_7 = hobbits_8[:j] + hobbits_8[j+1:]
        total_height = 0
        for k in range(7):
            total_height += hobbits_7[k]
        if total_height == 100:
            ans.append(hobbits_7)
            flag = False
            break

ans = sorted(ans[0])
for i in range(7):
    print(ans[i])