# N의 소인수에 대해 지수를 1씩 올리며 나누고 나누어 떨어지지 않으면 그 전 숫자를 저장

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    factors = [2, 3, 5, 7, 11]
    ans = []
    for f in factors:
        k = 0                         # factors의 원소를 소인수로 갖지 않을 시 답
        while True:
            k = k + 1
            if N % (f**k) != 0:       # 소인수의 k제곱에 의해 나누어 떨어지지 않을 시 
                ans.append(k-1)       # k-1을 저장
                break
                
    ans = ' '.join(list(map(str, ans)))  # int타입을 문자열로 바꾸어 join후 출력
    print(f'#{test_case} {ans}')