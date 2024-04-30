def valid_indices(row, col):
    return {row, col}.issubset(valid_size)


def add_option(row, col):
    if valid_indices(row, col):
        matrix[row][col] += value
    else:
        print("Invalid coordinates")


def sub_option(row, col):
    if valid_indices(row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")


rows = int(input())
matrix = [[int(x) for x in input().split()] for el in range(rows)]
valid_size = range(rows)

while True:
    command = input().split()

    if command[0] == "END":
        break
    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if command[0] == "Add":
        add_option(row, col)
    elif command[0] == "Subtract":
        sub_option(row, col)

for row in matrix:
    print(*row, sep=' ')
