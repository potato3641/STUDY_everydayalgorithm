from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')

alps = list(ascii_lowercase)
T = int(input())
for test_case in range(T):

    N = int(input())
    words = []
    word_sets = [[]]
    ans = 0

    for _ in range(N):
        word = input()
        words.append(word)

    for word in words:
        for i in range(len(word_sets)):
            word_sets.append(word_sets[i]+[word])

    
    for word_set in word_sets:
        for alp in alps:
            for word in word_set:
                if alp in word:
                    break
            else:
                break
        else:
            ans = ans + 1    
            

        
        
    print(ans)
