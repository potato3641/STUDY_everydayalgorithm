n = int(input())
# 1 ~ n까지
for i in range(1, n+1):
    cnt = 0
    # len(str(i))은 i의 자릿수, 자릿수 만큼 반복
    for j in range(len(str(i))):
        # i를 문자열로 바꿈, 앞에서부터 가져옴
        # 3, 6, 9이면 cnt 증가
        if '3' in str(i)[j] or '6' in str(i)[j] or '9' in str(i)[j]:
            cnt += 1
    if cnt > 0:
        # 3 6 9의 개수만큼 - 출력
        print('-'*cnt, end=' ')
    else:
        print(i, end=' ')