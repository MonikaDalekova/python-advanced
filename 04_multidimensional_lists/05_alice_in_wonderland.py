n = int(input())
matrix = []

tea_bags = 0
alice_position = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice_position = [row, col]
            matrix[row][col] = "*"

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

alice_path = []

while tea_bags < 10:
    command = input()
    step = commands[command] # Alice moves to next position
    row_pos = alice_position[0] + step[0]
    col_pos = alice_position[1] + step[1]

    if row_pos < 0 or row_pos >= n or col_pos < 0 or col_pos >= n:
        break
    if matrix[row_pos][col_pos] == "R":
        matrix[row_pos][col_pos] = "*"
        break
    if matrix[row_pos][col_pos] != "*.":
        tea_bags += int(matrix[row_pos][col_pos])
    matrix[row_pos][col_pos] = "*"
    alice_position = [row_pos, col_pos]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn\'t make it to the tea party.")
[print(*row) for row in matrix]