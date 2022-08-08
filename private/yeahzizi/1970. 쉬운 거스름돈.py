T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dict_money = {"50000": 0, "10000": 0, "5000":0, "1000":0, "500":0, "100":0, "50":0, "10":0} 
    #for문을 통해 딕셔너리 key 값에 맞는 value 값을 찾는다.

    for money in dict_money.keys(): #딕셔너리의 키 값들을 for문 안에서 반복되도록 넣는다.
       dict_money[money] = str(n // int(money)) #처음에 입력받은 n 값을 딕셔너리의 키 값들로 나눈 정수 몫들이 딕셔너리의 value 값으로 들어가게 한다.
       n %= int(money) #다른 value 값을 구하기 위해, 나머지를 구해서 다시 for문을 돌린다.

    print('#%d'%test_case)
    print(" ".join(dict_money.values())) #공백과 딕셔너리의 value 값을 같이 출력한다.