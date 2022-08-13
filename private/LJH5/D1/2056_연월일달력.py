T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    # value list의 index[0]는 마지막 일, index[1]은 마지막 일로 끝나는 월
    day_dict = {
        'end_28': [28, [2]], 
        'end_30': [30, [4, 5, 9, 11]], 
        'end_31': [31, [1, 3, 5, 7, 8, 10, 12]]
        }
    
    end_list = list(day_dict.keys()) # day_dict의 key 값을 저장

    time = input()

    year = int(time[:4])
    month = int(time[4:6])
    day = int(time[6:])

    if year == 0:   # 0년이면 -1 
        print(f'#{test_case}', -1)
        break
    for i in range(len(day_dict)):
        if month in day_dict[end_list[i]][1]: #index[1]에서 해당하는 월이 있는 곳을 찾음 
            if 1 <= day <= day_dict[end_list[i]][0]: # 일이 1~마지막 일 사이에 있는 지 확인
                print('#%d %04d/%02d/%02d' %(test_case, year, month ,day)) #빈자리는 앞에 영을 채우는 형태로 출력
                break
            else: # 일이 1~마지막 일을 벗어나면
                print(f'#{test_case}', -1)
                break
    else:# day_dict에서 해당하는 월을 찾지 못하면 1~12를 벗어남
        print(f'#{test_case}', -1)