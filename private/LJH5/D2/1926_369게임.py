# 3 6 9일 때 - 출력
# 두개이면 -- 출력

n = int(input())
# 1 ~ n까지
for i in range(1, n+1):
    # len(str(i))은 i의 자릿수, 자릿수 만큼 반복
    cnt = 0
    # 원본 값을 보호
    tmp = i
    for _ in range(len(str(i))):
        # 10으로 나눈 나머지 3 6 9이면 cnt 증가
        if tmp % 10 == 3 or tmp % 10 == 6 or tmp % 10 == 9:
            cnt += 1
        # 10으로 나눈 몫
        tmp //= 10
    if cnt > 0:
        # 3 6 9의 개수만큼 - 출력
        print('-'*cnt, end=' ')
    else:
        print(i, end=' ')