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

#2
rows = int(input())
matrix = [[int(x) for x in input().split()] for el in range(rows)]

valid_range = range(0, rows - 1)

command = input()
while command != "END":
    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    if action == 'Add':
        if row in valid_range and col in valid_range:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        if row in valid_range and col in valid_range:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input()

[print(*row, sep=' ') for row in matrix]
