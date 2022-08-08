# ex) N = 5일 때, 가능한 경우의 수
# 5C1 + 5C2 + 5C3 + 5C4 + 5C5 = 5 + 10 + 10 + 5 + 1 = 31
# ['word1','word2','word3','word4','word5'] -> [0, 1, 2, 3, 4]

# 0 1 2 3 4               

# 01 02 03 04                
#    12 13 14
#       23 24
#          34
        
# 012 013 014 023 024 034    
#             123 124 134 
#                     234
                                
# 0123 0124 0134 0234         
#                1234 

# 01234

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    
    # 단어 개수 N에 저장
    N = int(input())

    # 단어들 word_list에 저장
    word_list = []
    for n in range(N):
        word = input()
        word_list.append(word)

    # 인덱스 저장할 매트릭스 생성
    idx_list = []
    for n in range(N):
        idx_list.append([])

    # ex) N = 5
    #     idx_list = [[],[],[],[],[]]

    for n in range(N):
        idx_list[0].append(str(n))

    # ex) N = 5
    #     idx_list = [[0, 1, 2, 3, 4],[],[],[],[]]  

    # 각 리스트가 채워질 때마다 k를 추가해, k = N-1이 되면 break
    k = 0

    while True:

        for idx in idx_list[k]:                             # 만약 N = 5, k = 1 이면,
            for idx_1 in idx_list[0]:                       # idx_list[k] = ['01', '02', '03', '04', '12', '13', '14', '23', '24', '34']
                if int(idx[-1]) < int(idx_1):               # idx_list[0] = ['0', '1', '2', '3', '4']
                    idx_list[k+1].append(idx + idx_1)       # idx_list[k+1] = ['012', '013', '014', '023', '024', '034', '123', '124', '134', '234']

        k += 1

        if k == N - 1:
            break

    # ex) N = 5:
    #     idx_list: [['0', '1', '2', '3', '4']
    #                ['01', '02', '03', '04', '12', '13', '14', '23', '24', '34']
    #                ['012', '013', '014', '023', '024', '034', '123', '124', '134', '234']
    #                ['0123', '0124', '0134', '0234', '1234']
    #                ['01234']]

    # 각 단어의 조합으로 한 세트를 완성했을 때, count에 1 추가
    count = 0

    # idx_list의 각 경우의 수를 돌게 함
    for i in range(len(idx_list)):
        for j in range(len(idx_list[i])):

            # 찾은 알파벳을 넣을 리스트 생성
            alphabet_list = []
                                                               # ex) word_list = ['abc','def','ghi','jkl','mno'] / idx_list[1][2]: k = 0, 3
            for k in idx_list[i][j]:                           #     word_list의 0번째와 3번째를 리스트로 변환해 추가
                alphabet_list += list(word_list[int(k)])       #     alphabet_list = ['a', 'b', 'c', 'j', 'k', 'l']
            alphabet_set = set(alphabet_list)                  #     중복을 제거하기 위해 셋으로 변환
     
            # 셋의 길이가 26이 되면, count에 1 추가
            if len(alphabet_set) == 26:
                count += 1

    print(f'#{t} {count}')




