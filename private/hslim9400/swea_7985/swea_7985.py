from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')

'''
ㅁㄴㅇㄹ
트리에서 뽑아낸 숫자 리스트를 살펴보면
가장 위의 숫자가 가운데, 그 숫자를 기준으로 리스트를
나눴을때 그 아래의 숫자들 중 가장 위의 숫자가 다시 가운데로
가는 규칙이 있다.
'''
T = int(input())
for test_case in range(T):

    K = int(input())
    tree = []
    num_list = list(map(int, input().split())) 
    for _ in range(K):
        tree.append([])
    
    '''
    2의 k-1제곱부터 나눗셈을 하여 트리 가장 위의 숫자가
    될 수 있는지부터 판별 트리 리스트의 0번째 리스트가 
    트리의 가장 아랫단이다.
    '''
    for i in range(len(num_list)):
        for j in range(K-1, 0, -1): 
            if (i+1) % (2**j) == 0:
                tree[j].append(num_list[i])
                break
        else:
            tree[0].append(num_list[i])    


    for i in range(K-1, -1, -1):
        print(' '.join(list(map(str, tree[i]))))