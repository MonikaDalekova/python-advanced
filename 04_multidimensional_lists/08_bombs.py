#1
size = int(input())
matrix = [[int(x) for x in input().split()] for el in range(size)]
bomb_coordinates = ((int(x) for x in el.split(',')) for el in input().split()) # правим го в tuple, защото няма да ги променяме

directions = (
    (-1, 0), # up
    (1, 0), # down
    (0, -1), # left
    (0, 1), # right
    (-1, 1), # top right
    (-1, -1), # top left
    (1, -1), # down left
    (1, 1), # down right
    (0, 0) # current
)
for row, col in bomb_coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions: #определяме кои са цифрите на тези координати
        r, c = row + x, col + y

        if 0 <= r < size and 0 <= c < size:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0\

alive_cells = [num for row in range(size) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]

#2
size = int(input())
matrix = [[int(x) for x in input().split()] for el in range(size)]
bomb_coordinates = ((int(x) for x in el.split(',')) for el in input().split()) # правим го в tuple, защото няма да ги променяме


for row, col in bomb_coordinates:
    bomb_value = matrix[row][col]

    if bomb_value <= 0:
        continue

    for x in range(-1, 2):
        for y in range(-1, 2):
            r, c = row + x, col + y

            if 0 <= r < size and 0 <= c < size:
                matrix[r][c] -= bomb_value if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(size) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
