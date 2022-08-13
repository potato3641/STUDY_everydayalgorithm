num = [str(i) for i in range(1, int(input())+1)]
str_num = []

for i in num:
    word = i
    if '3' or '6' or '9' in i:
        if '3' in i and '6' in i:
            word = word.replace('3', '-')
            word = word.replace('6', '-')
        elif '3' in i and '9' in i:
            word = word.replace('3', '-')
            word = word.replace('9', '-')
        elif '6' in i and '9' in i:
            word = word.replace('6', '-')
            word = word.replace('9', '-')
        elif word == '33' or word == '333':
            word = word.replace('3', '-')
        elif word == '66' or word == '666':
            word = word.replace('6', '-')
        elif word == '99' or word == '999':
            word = word.replace('9', '-')
        elif '3' in word:
            word = '-'
        elif '6' in word:
            word = '-'
        elif '9' in word:
            word = '-'

    str_num.append(word)

print(' '.join(str_num))
