# 2056. 연월일 달력 D1 정답률:62.97

test_case = int(input())
for i in range(test_case): # 테스트 케이스만큼 반복
    date = input() 
    year = date[0:4] # 슬라이싱으로 연월일 나눠서 변수에 담기
    month = date[4:6]
    day = date[6:]
    if 0 < int(month) < 13: # 달의 유효성 검사
        if int(month) == 2: # 2월이라면
            if 0 < int(day) < 29: # 1~28일까지 유효하고 아니면 -1
                print(f'#{i+1} {year}/{month}/{day}')
            else:
                print(f'#{i+1} -1')
        elif int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12 : # 31일까지인 달/or로 될까 했는데 되네요
            if 0 < int(day) < 32:
                print(f'#{i+1} {year}/{month}/{day}')
            else:
                print(f'#{i+1} -1')
        elif int(month) in [4, 6, 9, 11]: # 30일까지인 달 / in [] 라고 써도 되나 했는데 되는군요
            if 0 < int(day) < 31:
                print(f'#{i+1} {year}/{month}/{day}')
            else:
                print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1') #달이 유효하지 않으면 -1 출력
