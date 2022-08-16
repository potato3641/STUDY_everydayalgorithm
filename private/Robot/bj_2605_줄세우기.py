students = list(range(1, int(input())+1)) # 학생 수, []로 적으면 [range(1, n)]이라고 출력 됨
number = list(map(int, input().split()))
answer = []
for i in range(len(students)):
    student = students.pop(0)
    answer.insert(i-number[i], student) # 리스트.insert(인덱스, 인자)
print(*answer)