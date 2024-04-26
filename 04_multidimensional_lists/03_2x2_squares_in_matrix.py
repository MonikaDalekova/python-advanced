rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for el in range(rows)]

count_equal_symbols = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        first_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index+1]
        below_el = matrix[row_index+1][col_index]
        diagonal_el = matrix[row_index+1][col_index+1]
        if first_el == next_el == below_el == diagonal_el:
            count_equal_symbols += 1
print(count_equal_symbols)