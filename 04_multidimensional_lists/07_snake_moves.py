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
