N = int(input())
# 스위치 리스트 생성, 문제에 맞춰 1번부터 스위치 불리언의 not연산으로 스위치를 켜고 끌거임
switch = [0] + list(map(bool, (list(map(int, input().split())))))

K = int(input())
students = []
for _ in range(K):
    students.append(list(map(int, input().split())))

for i in range(K):  # 학생 인원수만큼 시행
    student = students[i]
    if student[0] == 1:  # 남자라면
        for j in range(1, N+1):  # 0번째 인덱스는 제외
            if j % student[1] == 0:  # 고른 숫자의 배수 만큼 스위치를 변경
                switch[j] = not switch[j]
    else:  # 여자라면
        switch[student[1]] = not switch[student[1]]  # 고른 숫자 스위치 변경
        scope = 1  # 좌우로 넓혀갈 스코프
        while scope < min(student[1], N + 1 - student[1]):  # 스코프가 끝에 닿을때까지
            if switch[student[1] - scope] == switch[student[1] + scope]:  # 넓힌 스코프가 같다면
                # 스위치 변경
                switch[student[1] - scope], switch[student[1] + scope] = \
                    not switch[student[1] - scope], not switch[student[1] + scope]
            else:
                break
            scope += 1
switch = list(map(int, switch[1:]))
line = 0
while True:
    if line > len(switch) // 20:  # 한 줄에 20개씩 출력
        break
    ans = switch[line*20:line*20+20]
    print(*ans)
    line += 1

