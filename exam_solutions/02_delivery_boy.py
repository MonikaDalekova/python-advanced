n, m = [int(x) for x in input().split()]

matrix = []
starting_pos = []

directions = {"up": (-1, 0),
              "down": (1, 0),
              "right": (0, 1),
              "left": (0, -1)}

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)

    if "B" in row_data:
        starting_pos = [row, row_data.index("B")]
        # matrix[my_pos[0]][my_pos[1]] = "-"

current_pos = starting_pos

while True:
    command = input()

    current_row_index, current_col_index = current_pos
    row_move, col_move = directions[command]
    next_row, next_col = current_row_index + row_move, current_col_index + col_move

    if not (0 <= next_row < n and 0 <= next_col < m):
        matrix[starting_pos[0]][starting_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    symbol = matrix[next_row][next_col]

    if symbol == "*":
        continue

    current_pos = [next_row, next_col]

    if symbol == "P":
        matrix[next_row][next_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif symbol == "A":
        matrix[next_row][next_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif symbol == "-":
        matrix[next_row][next_col] = "."

[print(*row, sep='') for row in matrix]