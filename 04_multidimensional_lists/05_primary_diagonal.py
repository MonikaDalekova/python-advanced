number_of_rows_and_cols = int(input())

matrix = []

for ros in range(number_of_rows_and_cols):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)
sum_el = 0
for index in range(number_of_rows_and_cols):
    sum_el += matrix[index][index]

print(sum_el)