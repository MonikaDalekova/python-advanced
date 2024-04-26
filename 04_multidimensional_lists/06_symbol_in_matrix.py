n = int(input())

matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)
symbol = input()
position = None
for row_index in range(n):
    if position:
        break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            break
if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")



