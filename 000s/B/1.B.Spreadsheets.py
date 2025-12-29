def number_to_column(n):
    result = ""
    while n > 0:
        n -= 1
        result = chr(n % 26 + ord('A')) + result
        n //= 26
    return result


def column_to_number(s):
    num = 0
    for ch in s:
        num = num * 26 + (ord(ch) - ord('A') + 1)
    return num


n = int(input())

for _ in range(n):
    cell = input().strip()

   
    if cell[0] == 'R' and 'C' in cell:
        r_index = cell.find('R')
        c_index = cell.find('C')

        row = int(cell[r_index + 1:c_index])
        col = int(cell[c_index + 1:])

        col_letters = number_to_column(col)
        print(col_letters + str(row))

   
    else:
        i = 0
        while cell[i].isalpha():
            i += 1

        col_part = cell[:i]
        row_part = cell[i:]

        col_number = column_to_number(col_part)
        print(f"R{row_part}C{col_number}")
