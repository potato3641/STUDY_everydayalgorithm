T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #화폐 딕셔너리를 만들기, 돈의 금액과 개수를 리스트로 만듬
    money_dict = {
        '오만원': [50000, 0], 
        '만원': [10000, 0], 
        '오천원': [5000, 0], 
        '천원': [1000, 0], 
        '오백원': [500, 0], 
        '백원': [100, 0], 
        '오십원': [50, 0], 
        '십원': [10, 0] 
    }

    won_list = list(money_dict.keys())  #화폐 단위를 저장한 리스트
    

    money = int(input()) # 금액 입력받음
    for i in range(len(money_dict)):
        won = money_dict.get(won_list[i])[0] #나누는 금액의 단위
        
        cnt = money // won  # 화폐의 개수
        money_dict.get(won_list[i])[1] = cnt

        money %= won # 남은 돈

        if money <= 0:  # 남은 돈이 0원이 되면 반복 중단
            break
    
    cnt_list = [] # 화폐의 개수 저장할 리스트
    for i in money_dict.values():
        cnt_list.append(i[1])

    print(f'#{test_case}')
    print(*cnt_list)        #print(*[1, 2, 3]) -> 1 2 3 으로 출력됨