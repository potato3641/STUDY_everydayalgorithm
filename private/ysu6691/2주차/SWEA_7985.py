import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    
    # 트리 깊이 K에 저장
    K = int(input())

    # 각 자연수를 리스트로 저장
    num_list = list(map(int, input().split()))

    # 각 높이 별 숫자 리스트를 담을 매트릭스(result) 생성
    # ex) K = 3   []
    #            [  ]
    #           [    ]
    result = []
    for k in range(K):
        result.append([])

    # 가장 꼭대기에 위치한 숫자를 max_num에 저장
    # ex) 받은 리스트의 총 길이가 15라면, 리스트의 7번째(15를 2로 나눈 몫) 숫자가 가장 꼭대기에 위치함
    max_num = num_list[len(num_list) // 2]

    # 매트릭스 꼭대기층 채우기
    result[0].append(max_num)

    # 각 층에 들어갈 숫자를 찾을 인덱스 리스트 생성
    idx_list = []
    idx_list.append(len(num_list) // 2) # 찾은 꼭대기 인덱스 추가

    gap = K - 2   # 각 층 별 차이를 구하기 위해 n 변수 생성
                # ex) K = 4            7               
                #               3            11           -> 차이 = 4 = 2^2 = 2^(K-2) -> gap = K - 2
                #            1     5      9      13       -> 차이 = 2 = 2^1 = 2^(K-3) -> gap -= 1
                #           0  2  4  6   8 10  12  14     -> 차이 = 1 = 2^0 = 2^(K-4) -> gap -= 1

    start_idx = 0   # 인덱스 리스트에 숫자가 채워지면서, 중복을 제외하기 위해 k 변수 생성
                    # ex) K = 4
                    #  [7] -> [7, 3, 11] -> [7, 3, 11, 1, 5, 9, 13] -> [7, 3, 11, 1, 5, 9, 13, 0, 2, ...]
                    #   0        1 ~                  3 ~                           7 ~           -> start_idx ~             
                    #   0   1 = 0 * 2 + 1       3 = 1 * 2 + 1                 7 = 3 * 2 + 1       -> start_idx = start_idx * 2 + 1

    height_number = 1   # 매트릭스의 각 높이를 선택해 숫자를 채우기 위해 height_number 변수 생성
                        # ex) K = 4            7                  -> height_number = 0
                        #               3            11           -> height_number = 1
                        #            1     5      9      13       -> height_number = 2
                        #           0  2  4  6   8 10  12  14     -> height_number = 3


    # 층의 높이가 1이면 while문 통과
    while K != 1:

        # 인덱스 리스트의 start_idx번째부터 돌면서 
        # 인덱스 리스트에는 찾은 인덱스를,
        # 반환할 매트릭스에는 각 층에 해당 숫자를 추가
        for idx in idx_list[start_idx:]:
            idx_list.append(idx - 2 ** gap)
            idx_list.append(idx + 2 ** gap)

            result[height_number].append(num_list[idx - 2 ** gap])
            result[height_number].append(num_list[idx + 2 ** gap])

        # 층이 바뀌면서 start_idx, gap, height_number 변경
        start_idx = start_idx * 2 + 1
        gap -= 1
        height_number += 1

        # 반환할 매트릭스의 마지막 층이 채워지면, break
        # height_number = K - 1 와 같은 결과
        if result[K - 1]:
            break

    # 층의 높이만큼 돌면서 첫 번째 출력에만 테스트 번호 출력하고, 나머지는 그대로 출력
    for k in range(K):
        if k == 0:
            print(f'#{t} {max_num}')
        else:
            print(' '.join(map(str, result[k])))


'''
#1 5
2 1
3 7 6 4
#2 1
2 3
'''

