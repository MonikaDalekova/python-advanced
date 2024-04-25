rows, columns = [int(el) for el in input().split(', ')]
matrix = []
sums = []

for i in range(rows):
    inner_lest = [int(el) for el in input().split()]
    matrix.append(inner_lest)

for col_index in range(columns):
    sum_el = 0
    for row_index in range(rows):
        sum_el += matrix[row_index][col_index]
    sums.append(sum_el)
for el in sums:
    print(el)