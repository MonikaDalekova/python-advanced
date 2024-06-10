n = int(input())
health = 100
maze = [[x for x in input()] for el in range(n)]
r, c = None, None

movements = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}


for row in range(n):
    for col in range(n):
        if maze[row][col] == "P":
            r, c = row, col

while True:
    move = input()

    if not (0 <= r + movements[move][0] < n and 0 <= c + movements[move][1] < n):
        continue

    maze[r][c] = "-"
    r += movements[move][0]
    c += movements[move][1]

    if maze[r][c] == "X":
        print("Player escaped the maze. Danger passed!")
        maze[r][c] = "P"
        break

    elif maze[r][c] == "H":
        health = min(100, health + 15)

    elif maze[r][c] == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            maze[r][c] = "P"
            break

    maze[r][c] = "P"

print(f"Player's health: {health} units")
for row in maze:
    print(*row)