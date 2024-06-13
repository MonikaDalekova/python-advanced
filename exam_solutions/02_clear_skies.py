n = int(input())
airspace = [[x for x in input()] for el in range(n)]
initial_armor_value = 300
r, c = None, None  # current position coordinates

for row in range(n):
    for col in range(n):
        if airspace[row][col] == "J":
            r, c = row, col

enemies = 4

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while enemies > 0 and initial_armor_value > 0:
    step = input()
    airspace[r][c] = "-"

    r += directions[step][0]
    c += directions[step][1]

    if airspace[r][c] == "E":
        if enemies == 1:
            airspace[r][c] = "J"
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        elif enemies > 1:
            initial_armor_value -= 100
            if initial_armor_value == 0:
                airspace[r][c] = "J"
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
                break
            elif initial_armor_value > 0:
                airspace[r][c] = "-"
        enemies -= 1
    elif airspace[r][c] == "R":
        initial_armor_value = 300
        airspace[r][c] = "-"

    airspace[r][c] = "J"

for row in airspace:
    print(*row, sep='')

