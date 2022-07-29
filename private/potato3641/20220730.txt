'''
사전지식) 비트와 아스키코드에 대한 이해가 필요
8bit짜리 세 글자 abc가 있음. ( ord(’a’) = 97, ord(’b’) = 98, ord(’c’) = 99 )
24bit짜리 버퍼에 위의 세 글자 0b01100001 0b01100010 0b01100011가 들어가서
6bit 011000 010110 001001 100011 이렇게 잘려서
base64 기반 6bit짜리 네 글자 YWJj가 된 것을 다시 원복하는 문제
'''
T = int(input())
base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# 문제에 주어진 표-1을 미리 저장
for test_case in range(1, T + 1):
    ecdstr = input()                           # 암호문 받기
    print(f'#{test_case}',end=' ')
    for i in range(len(ecdstr)//4):            # 제약사항에서 문자열 길이가 4의 배수인
																							 # 것을 이용해서 for문도 1/4배로 줄임 
        line = ecdstr[i*4:i*4+4]               # 버퍼가 24bit이므로 1byte 문자를
																							 # 3덩어리씩 잘라냄 (3*8bit)
        bitline = 1                            # 0b 00000000 00000000 00000001
        for i in range(4):                     #      1byte   2byte    3byte
            bitline <<= 6                      # 다음 데이터를 받기 위해서
																							 # 비트를 왼쪽으로 6bit씩 밀어냄
            bitline += base64.index(line[i])   # 24bit 데이터를 6bit씩 표에 대입/변환
        print(chr((bitline>>16) & 255),end='') # 1byte를 빼서 아스키코드값 변환/출력
#																			 bitline # 0b aaaaaaaa bbbbbbbb cccccccc
#																	 bitline>>16 # 0b 00000000 00000000 aaaaaaaa
# 									       (bitline>>16) & 255 # 0b 00000000 00000000 aaaaaaaa
        print(chr((bitline>>8) & 255),end='')  # 2byte를 빼서 아스키코드값 변환/출력
#																			 bitline # 0b aaaaaaaa bbbbbbbb cccccccc
#   															  bitline>>8 # 0b 00000000 aaaaaaaa bbbbbbbb
# 									        (bitline>>8) & 255 # 0b 00000000 00000000 bbbbbbbb
        print(chr(bitline & 255),end='')       # 3byte를 빼서 아스키코드값 변환/출력
#																			 bitline # 0b aaaaaaaa bbbbbbbb cccccccc
# 									             bitline & 255 # 0b 00000000 00000000 cccccccc
    print() # 줄바꿈