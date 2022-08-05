T = int(input()) # 케이스의 수

for t in range(T):
    N = int(input()) # 입력받은 수
    add_N = N # N을 배수로 처리하기 위해 add_N을 고정시켜 for문 안에서 더해줌
    
    # 현재까지 본 숫자 넣을 딕셔너리 생성
    num_dict = dict()

    while True:
        
        # N을 문자열로 처리해, 각 자릿수를 딕셔너리에 추가
        for n in str(N):

            # 만약 해당 자릿수가 딕셔너리에 없다면, 해당 자릿수 추가
            if num_dict.get(n, -1) == -1:
                num_dict[n] = 1 

            # 만약 해당 자릿수가 딕셔너리에 있다면 패스
            else: 
                pass
        
        # 딕셔너리의 길이가 10(0, 1, 2, ... , 8, 9)이면, break
        if len(num_dict) == 10:
            break

        # N 배수 처리
        N += add_N

    print(f'#{t + 1} {N}')
    