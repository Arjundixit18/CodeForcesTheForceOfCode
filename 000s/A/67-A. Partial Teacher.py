n = int(input())
s = input().strip()

# Everyone gets 1 toffee initially
toffees = [1] * n

# Move from left to right
for i in range(n - 1):
    if s[i] == 'R':
        toffees[i + 1] = toffees[i] + 1
    elif s[i] == '=':
        toffees[i + 1] = toffees[i]

# Move from right to left
for i in range(n - 2, -1, -1):
    if s[i] == 'L':
        if toffees[i] <= toffees[i + 1]:
            toffees[i] = toffees[i + 1] + 1
    elif s[i] == '=':
        toffees[i] = max(toffees[i], toffees[i + 1])

print(*toffees)
