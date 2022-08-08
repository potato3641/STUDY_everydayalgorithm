a = [1,2,3,4]
combs = [[]]
for n in a:
    for i in range(len(combs)):
        combs.append(combs[i]+[n])

print(combs)
