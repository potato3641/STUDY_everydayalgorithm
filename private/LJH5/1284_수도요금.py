T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # P: A사의 1L당 요금
    # Q: B사의 R리터 이하 요금
    # R: B사의 월간 정액제 양
    # S: B사의 R초과 1L당 요금
    # W: 월간 사용하는 수도의 양
    data_list = ['P', 'Q', 'R', 'S', 'W']
    input_list = list(map(int, input().split()))
		# 예시) {'P': 9, 'Q': 100, 'R': 20, 'S': 3, 'W': 10}
    data_dict = dict(zip(data_list, input_list)) 
		
		# 변수 선언 및 초기화
    company_a = 0
    company_b = 0

		# A회사의 요금
    company_a = data_dict.get('P') * data_dict.get('W')    
    # 월간 사용 수도의 양에 따라 달라지는 B회사 요금 처리
    check_company_b = data_dict.get('W') - data_dict.get('R')
    if check_company_b <= 0:
        company_b = data_dict.get('Q')
    else:
        company_b = data_dict.get('Q') + check_company_b*data_dict.get('S')

    # 적은 회사의 요금 출력
    if company_a <= company_b:
        print(f'#{test_case} {company_a}')
    else:
        print(f'#{test_case} {company_b}')