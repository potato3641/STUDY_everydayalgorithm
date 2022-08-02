from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(T):

    K = int(input())
    tree = []
    num_list = list(map(int, input().split()))
    for _ in range(K):
        tree.append([])
    
    for i in range(len(num_list)):
        for j in range(K-1, 0, -1):
            if (i+1) % (2**j) == 0:
                tree[j].append(num_list[i])
                break
        else:
            tree[0].append(num_list[i])    


    for i in range(K-1, -1, -1):
        print(' '.join(list(map(str, tree[i]))))