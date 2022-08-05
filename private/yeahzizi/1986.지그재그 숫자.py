T = int(input())  

for test_case in range(1, T + 1):  #test를 여러번 진행할 반복문을 만든다.(range는 뒷숫자에서 -1 만큼 가져오기 때문에 입력받은 T에 +1해서 가져온다.)
    n = int(input())               #반복문 안에, 문제에서 요구한 숫자 n을 입력 받는다.
    total = 0                      #나중에 결과로 나올 total은 0에서 시작한다.

    for i in range(1, n +1):       #앞에서 입력받은 숫자 n번만큼 계산할 반복문을 만든다.
        if i % 2 == 0:             #i를 2로 나눈 나머지가 0이면(짝수이면) total에서 i만큼 뺀다.
            total -= i
        else:                      #그게 아니라면(i를 2로 나눈 나머지가 1이면-홀수이면) total에서 i만큼 더한다.
            total += i

    print('#%d %d'%(test_case, total))  #반복문이 완료된 뒤, %d 문자열 포맷팅 방식을 이용해 테스트 횟수와 최종값을 출력한다.