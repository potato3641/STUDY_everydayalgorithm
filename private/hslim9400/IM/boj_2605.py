N = int(input())
nums = list(map(int, input().split()))
students = []  # 답으로 낼 리스트

for i in range(N):
    if nums[i] == 0:  # 0일경우 맨 뒤에
        students.append(i+1)
    else:  # 아닐경우 그만큼 앞에 넣어준다.
        students = students[:-nums[i]] + [i+1] + students[-nums[i]:]
print(*students)