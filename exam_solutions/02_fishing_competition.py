n = int(input())
fishing_area = [[int(x) if x.isdigit() else x for x in input()] for el in range(n)]
passages = 0
r, c = None, None
for row in range(n):
    for col in range(n):
        if fishing_area[row][col] == "S":
            r, c = row, col
            fishing_area[r][c] = "-"

movements = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    command = input()

    if command == "collect the nets":
        break

    r += movements[command][0]
    c += movements[command][1]

    r = (r + len(fishing_area)) % len(fishing_area)
    c = (c + len(fishing_area)) % len(fishing_area)

    current_char = fishing_area[r][c]

    if current_char != "-" and current_char != "W" and current_char != "S":
        passages += int(current_char)
        fishing_area[r][c] = "-"
    elif fishing_area[r][c] == "W":
        passages = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{r},{c}]")
        exit(0)

fishing_area[r][c] = "S"

if passages >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - passages} tons of fish more.")
if passages > 0:
    print(f"Amount of fish caught: {passages} tons.")
[print(*row, sep='') for row in fishing_area]

# size = int(input())
#
# matrix = []
# my_pos = []
# total_fish = 0
# directions = {"up": (-1, 0),
#               "down": (1, 0),
#               "right": (0, 1),
#               "left": (0, -1)}
#
# for row in range(size):
#     line = list(input())
#     matrix.append(line)
#
#     if "S" in line:
#         my_pos = [row, line.index("S")]
#         matrix[row][my_pos[1]] = "-"
#
# command = input()
#
# while command != "collect the nets":
#     next_row = my_pos[0] + directions[command][0]
#     next_col = my_pos[1] + directions[command][1]
#
#     next_row = (next_row + len(matrix)) % len(matrix)
#     next_col = (next_col + len(matrix)) % len(matrix)
#
#     symbol = matrix[next_row][next_col]
#
#     if symbol.isdigit():
#         total_fish += int(symbol)
#         matrix[next_row][next_col] = "-"
#     elif symbol == "W":
#         print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
#               f"Last coordinates of the ship: [{next_row},{next_col}]")
#         exit(0)
#     my_pos = [next_row, next_col]
#
#     command = input()
#
# matrix[next_row][next_col] = "S"
#
# if total_fish >= 20:
#     print("Success! You managed to reach the quota!")
# else:
#     print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - total_fish} tons of fish more.")
#
# if total_fish > 0:
#     print(f"Amount of fish caught: {total_fish} tons.")
#
# [print(*row, sep='') for row in matrix]