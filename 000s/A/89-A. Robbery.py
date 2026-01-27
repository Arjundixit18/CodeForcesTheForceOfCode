n, m, k = map(int, input().split())
a = list(map(int, input().split()))

odd_sum = 0
even_sum = 0

for i in range(n):
    if i % 2 == 0:
        odd_sum += a[i]
    else:
        even_sum += a[i]

max_pattern_remove = 2 * min(odd_sum, even_sum)
max_operations = m * k

print(min(max_pattern_remove, max_operations))
