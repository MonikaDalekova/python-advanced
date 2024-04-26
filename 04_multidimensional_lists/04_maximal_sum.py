rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for el in range(rows)]

max_sum = float('-inf')
sub_matrix = []

for row_index in range(rows-2):
    for col_index in range(cols-2):
        first_row = matrix[row_index][col_index:col_index+3] # слайсинга ни дава всички стойности от листа на 1 ред
        second_row = matrix[row_index+1][col_index:col_index+3]
        third_row = matrix[row_index+2][col_index:col_index+3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [first_row, second_row, third_row]
print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix] # за всеки ред от матрицата, разопаковай реда