# from itertools import count
# 1288. 새로운 불면증 치료법 D2 정답률:81.94

# test_case = int(input('테스트 케이스의 수를 입력하세요.:'))

# for x in range(test_case): #테스트 케이스의 수만큼 반복
#     number = input('숫자를 입력하세요.:') # 스트링이어야 리스트로 하나씩 분절 가능 (int는 안 된다.)
#     num_list = list(number) # 0부터 9까지 모을 메인리스트, 첫번째로 입력받은 숫자를 미리 넣어둠
#     count = 2 # 다음으로 N의 배수인 번호를 만들어야 함

#     while len(num_list) < 10:    # 몇 번 반복할 지 모르니까 while문, 메인리스트에 10개의 숫자가 담길 때까지 반복하고
#         num = list(str(int(number)*count)) #처음 받은 숫자는 스트링이었으니까 int로 바꿔서 배수로 곱한 뒤 다시 스트링으로 만들어서 리스트로 분절
#         count += 1 #곱하는 수는 2, 3, 4로 늘어나니까 1씩 늘려주고

#         for j in range(len(num)): # 메인 리스트에 담을 수 있도록 숫자를 하나씩 뽑아서
#             num_list.append(num[j]) # 메인 리스트에 넣어준다.
#             num_list = sorted(list(set(num_list))) #반복되는 수는 없앤다.        

#     print(f'#{(x+1)} {(count-1)*int(number)}') # while문이 끝나는 시점에서 결과를 프린트한다.

test_case = int(input()) # 제출할 때는 괄호 비워둬야 함

for x in range(test_case): 
    number = input() 
    num_list = list(number) #이건 메인 리스트에 바로 넣는 거임
    count = 2 

    while len(num_list) < 10:    
        num = str(int(number)*count) #스트링 자체도 인덱스가 있기 때문에 리스트로 만들지 않아도 된다.
        count += 1 

        for j in range(len(num)):
            num_list.append(num[j]) 
            num_list = list(set(num_list)) # 내가 보려고 sort 해놨던 거 결과값엔 필요없으니까 제거

    print(f'#{(x+1)} {(count-1)*int(number)}')