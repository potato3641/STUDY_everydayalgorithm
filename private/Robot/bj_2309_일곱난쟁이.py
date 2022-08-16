# 백준 2309 일곱 난쟁이
nine = [int(input()) for _ in range(9)]
answer = []
for i in range(1 << 9):
    seven = [] # 부분집합 담을 빈 리스트는 여기
    for j in range(9):
        if i & (1 << j): # 여기부터 아직 모르겠다
            seven.append(nine[j])
    if len(seven) == 7 and sum(seven) == 100:
        answer = sorted(seven)
        break # 답 하나만 나오면 되니까
for n in answer:
    print(n)