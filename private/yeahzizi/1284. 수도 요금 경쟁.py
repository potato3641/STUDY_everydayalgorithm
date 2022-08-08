T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split()) #map을 사용해서 5개의 변수를 입력 받는다.


    if (W <= R): #월간 사용량이 R리터보다 작거나 같은 경우에는,
        print('#%d'%test_case, min(Q, P*W)) #기본요금 Q와 1리터당 p원에 월간사용량 w를 곱한 값을 비교해서 더 작은 값을 출력한다.
    else: #월간 사용량이 R리터보다 큰 경우에는
        print('#%d'%test_case, min(P*W, (Q + (((W-R)*S))))) 
        #1리터당 p원에 월간사용량 w를 곱한 값과 기본요금 더하기 월간 사용량에서 R리터를 뺀 값에 S원 만큼 곱해진 값을 비교해서 더 작은 값을 출력한다.

    
