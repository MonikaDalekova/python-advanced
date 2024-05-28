from collections import deque

rows, cols = [int(x) for x in input().split()]
string = list(input())

string_copy = deque(string.copy())

for row in range(rows):
    while len(string_copy) < cols:
        string_copy.extend(string)

    if row % 2 == 0:
        print(*[string_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[string_copy.popleft() for _ in range(cols)][::-1], sep='')

#2
# rows, cols = [int(x) for x in input().split()]
# word = input()
# 
# matrix = [['' for _ in range(cols)] for _ in range(rows)]
# word_index = 0
# word_length = len(word)
# 
# for row_index in range(rows):
#     if row_index % 2 == 0:
#         for col_index in range(cols):
#             matrix[row_index][col_index] = word[word_index]
#             word_index = (word_index + 1) % word_length # когато свършат буквите, да започне отначало
#     else:
#         for col_index in range(cols -1, -1, -1): # отзад напред
#             matrix[row_index][col_index] = word[word_index]
#             word_index = (word_index + 1) % word_length
# 
# [print(*row, sep='') for row in matrix]
