n = int(input())

matrix = [[int(x) for x in input().split(', ')] for el in range(n)]

first_diagonal_el = [matrix[row][row] for row in range(n)] # индексът на ред и колона е един и същ
second_diagonal_el = [matrix[row][n - row - 1] for row in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in first_diagonal_el)}. Sum: {sum(first_diagonal_el)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonal_el)}. Sum: {sum(second_diagonal_el)}")