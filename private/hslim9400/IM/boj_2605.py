N = int(input())
nums = list(map(int, input().split()))
students = []

for i in range(N):
    if nums[i] == 0:
        students.append(i+1)
    else:
        students = students[:-nums[i]] + [i+1] + students[-nums[i]:]
print(*students)