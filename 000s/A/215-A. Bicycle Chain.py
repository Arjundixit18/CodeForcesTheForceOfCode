n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

max_ratio = 0
count = 0

for ai in a:
    for bj in b:
        if bj % ai == 0:          # ratio must be integer
            ratio = bj // ai

            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

print(count)
