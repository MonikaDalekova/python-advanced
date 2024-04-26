n = int(input())

matrix = [[int(x) for x in input().split()] for el in range(n)]

first_diagonal_el = [matrix[row][row] for row in range(n)] # индексът на ред и колона е един и същ
second_diagonal_el = [matrix[row][n - row - 1] for row in range(n)]
first_sum = sum(first_diagonal_el)
second_sum = sum(second_diagonal_el)
print(abs(first_sum - second_sum))