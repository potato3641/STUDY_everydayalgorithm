from string import ascii_lowercase
import sys
sys.stdin = open('sample_input.txt', 'r')
'''
단어를 입력받아 모든 단어 세트를 만들고
알파벳을 하나하나 넣어가며 단어 세트가 
모든 알파벳을 포함하는지 확인
'''
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

    '''
    단어들로 만들 수 있는 모든 조합 만들기
    [1, 2]으로 만든다 치면
    [[]]
    [[], []] 자기 자신을 복사
    [[], [1]] 첫 원소를 복사한 곳에 추가 
    [[], [1], [], [1]] 다시 자신을 복사
    [[], [1], [2], [1, 2]] 두번째 원소를 복사한 곳에 추가
    반복하면 모든 조합을 찾을 수 있다.
    '''
    for word in words: 
        for i in range(len(word_sets)):
            word_sets.append(word_sets[i]+[word])

    
    for word_set in word_sets: #단어세트를 선택
        for alp in alps: #알파벳을 선택
            for word in word_set: #단어세트 내에서
                if alp in word:
                    break #알파벳이 있으면 다음 알파벳
            else:
                break #알파벳이 없으면 다음 단어세트
        else:
            ans = ans + 1 #모든 알파벳을 확인하면 답+1
            

        
        
    print(ans)
