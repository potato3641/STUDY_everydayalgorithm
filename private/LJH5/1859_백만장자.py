T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    profit = 0
    n = int(input())
    sale_price = [] # 매매가를 저장할 리스트
    sale_price = list(map(int, input().split()))

    for _ in range(len(sale_price)):
        tmp = max(sale_price)   # 최고 매매가 찾기
        index = sale_price.index(tmp)   # 최고 매매가 위치 찾기
        buy_sum = sum(sale_price[0:index])  #구입 금액 = 최고 매매가 앞 매매가 다 더하기
        sale_sum = sale_price[index]*index  #판매 금액 = 최고매매가 * 앞 일수
        profit += (sale_sum - buy_sum)  #이익은 판매 금액 - 구입 금액
        del sale_price[:index+1]    #계산한 부분은 삭제

        if sale_price == []:    # 모든 매매를 진행했으면 
            break               # 반복문 탈출
    print(f'#{test_case} {profit}')