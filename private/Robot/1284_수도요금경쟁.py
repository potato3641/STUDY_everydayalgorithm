#1284 수도 요금 경쟁 (D2)
test_case = int(input())

for i in range(test_case): # 테스트 케이스만큼 반복, i는 0, 1, 2, ...
    p, q, r, s, w = map(int, input().split()) # 빈칸 기준으로 나눈 리스트를 int로
    a = p * w # A사 수도요금
    b = 0 # B사 수도요금을 넣을 변수
    if w <= r: # 사용한 물의 양이 기준보다 적을 때
        b = q # q만큼만 지불하면 된다.
    else: # 사용한 물의 양이 기준보다 많을 때
        b = q + (w-r) * s # q요금에 초과사용량을 더한다.
    print(f'#{i+1} {min(a, b)}') # a와 b 중에 더 작은 값을 출력

        