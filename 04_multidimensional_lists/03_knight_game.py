n = int(input())
matrix = [list(input()) for _ in range(n)]

positions = (  # създаваме тюпъл с всички посоки на коня
    (-2, -1),  # горе 2 и ляво 1
    (-2, 1),  # горе 2 и дясно 1
    (-1, -2),  # горе 1 и ляво 2
    (-1, 2),  # горе 1 и дясно 2
    (2, 1),  # долу 2 и дясно 1
    (2, -1),  # долу 2 и ляво 1
    (1, 2),  # долу  1 и дясно 2
    (1, -2)  # долу 1 и ляво 2
)
removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = pos[0] + row
                    pos_col = pos[1] + col
                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [row, col]
    if knight_with_most_attacks:
        r, c = knight_with_most_attacks
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break
print(removed_knights)
