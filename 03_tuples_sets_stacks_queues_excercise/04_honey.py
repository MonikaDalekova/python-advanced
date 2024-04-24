from collections import deque
bees = deque(int(x) for x in input().split()) # first bee -> queue
nectar = [int(x) for x in input().split()] # last nectar -> stack
making_process = deque(input().split())

total_honey = 0

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}
while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    else:
        total_honey += abs(functions[making_process.popleft()](current_bee, current_nectar))


print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: ", end='')
    print(*bees, sep=', ')
if nectar:
    print(f"Nectar left: ", end='')
    print(*nectar, sep=', ')