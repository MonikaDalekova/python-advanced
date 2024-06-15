game_board = int(input())
gambler = [[x for x in input()] for el in range(game_board)]
tax_entering = 100

r, c = None, None
game_over = False
jackpot = False
for row in range(game_board):
    for col in range(game_board):
        if gambler[row][col] == "G":
            r, c = row, col
            gambler[r][c] = "-"
commands = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    command = input()
    if command == "end":
        break

    r += commands[command][0]
    c += commands[command][1]

    if not 0 <= r < game_board and 0 <= c < game_board:
        game_over = True
        break

    if gambler[r][c] == "W":
        tax_entering += 100
    elif gambler[r][c] == "P":
        tax_entering -= 200
    elif gambler[r][c] == "J":
        tax_entering += 100000
        game_over = True
        print(f"You win the Jackpot!End of the game. Total amount: {tax_entering}$")
        gambler[r][c] = "G"
        for row in gambler:
            print(*row, sep='')
        break

    if tax_entering <= 0:
        game_over = True
        break
    gambler[r][c] = "-"


gambler[r][c] = 'G'
if not game_over:
    print(f"End of the game. Total amount: {tax_entering}$")
    for row in gambler:
        print(*row, sep='')
else:
    print("Game over! You lost everything!")