#초기 개수를 입력받는 숫자는 inputNum으로 정함
inputNum=int(input())
#각 숫자마다 답안을 print하기 위해 for문 사용
for i in range(inputNum):
#각 순서에 해당하는 숫자는 nowNum으로 정함
    nowNum=int(input())
#각 숫자에 해당하는 개수를 리스트로 만듦(각각 2,3,5,7,11 순서대로 개수에 해당함)
    countList=[0,0,0,0,0]
#해당 리스트에 해당하는 실제 숫자도 구분하기 위해 리스트를 생성함
    realNum=[2,3,5,7,11]
#5개이므로 range(5)의 범위를 지님
    for p in range(5):
#만약 현재 target 에 해당하는 숫자로 나눠진다면
        if nowNum%realNum[p]==0:
#target 개수를 추가하고
            countList[p]=1
#nowNum을 해당 숫자로 나눔
            nowNum=nowNum/realNum[p]
#while문에서 해당 숫자로 나눠지지 않을 때까지
            while nowNum%realNum[p]==0:
#해당 숫자로 나누고
                nowNum=nowNum/realNum[p]
#리스트에서 개수를 1씩 증가시킴
                countList[p]+=1
#나눠지지 않는다면 다음 숫자로 넘어감
        else:
            None
#f-string을 통해 모든 숫자를 한번에 출력
    print(f'#{i+1} {countList[0]} {countList[1]} {countList[2]} {countList[3]} {countList[4]}')