# 백준 1244 스위치 켜고 끄기 10:30-11:39 70분
T = int(input()) # 스위치 개수
status = list(map(int, input().split())) # 스위치 온 오프 상태
# 0 1 0 1 0 0 0 1
# 0 1 1 1 0 1 0 1
# 1 0 0 0 1 1 0 1
student = int(input()) # 학생 수
for tc in range(student):
    gender, number = map(int, input().split()) # 성별 남1 여2, 받은 수
    # 1 3
    # 남학생일 때
    if gender == 1:
        for i in range(1, T // number + 1):
            if status[number * i - 1]:
                status[number * i - 1] = 0
            else:
                status[number * i - 1] = 1
    # 여학생일 때
    else:
        # 가운데는 무조건 변경
        if status[number - 1]:
            status[number - 1] = 0
        else:
            status[number - 1] = 1
        # 0 1 1 1 0 1 0 1
        # 0 1 0 1 0 1 0 1
        # 대칭으로 같으면 변경
        i = 1 # 대칭 검사할 인덱스
        while number - i and number + i - 1 < T and status[number - 1 - i] == status[number - 1 + i]:
            if status[number - 1 - i]:
                status[number - 1 - i] = status[number - 1 + i] = 0
            else:
                status[number - 1 - i] = status[number - 1 + i] = 1
            i += 1
# 한 줄에 스무개씩 출력
for i in range(T // 20 + 1): # 0, 1, 2
    print(*status[20 * i:20 * i + 20]) # 0:20 20:40

