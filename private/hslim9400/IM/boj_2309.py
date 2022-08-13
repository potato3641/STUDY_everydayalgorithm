hobbits = []  # 난쟁이 배열
for _ in range(9):
    hobbits.append(int(input()))

ans = []
flag = True
for i in range(9):  # 아홉명 중 한명을 골라
    if not flag:
        break
    hobbits_8 = hobbits[:i] + hobbits[i+1:]  # 뺀다
    for j in range(8):  # 여덟명중 한명을 더 골라
        hobbits_7 = hobbits_8[:j] + hobbits_8[j+1:]  # 뺀다
        total_height = 0  # 일곱명의 키를 합할 변수
        for k in range(7):
            total_height += hobbits_7[k]
        if total_height == 100:  # 합해서 100이 된다면
            ans.append(hobbits_7)
            flag = False  # 종료
            break

ans = sorted(ans[0])  # 정렬하여 출력
for i in range(7):
    print(ans[i])