def find_position(matrix, element):
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == element:
                return (row_index, col_index)


n = int(input())

matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)
symbol = input()

position = find_position(matrix, symbol)
if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
