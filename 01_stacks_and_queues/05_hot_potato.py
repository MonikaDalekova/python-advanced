from collections import deque

name = deque(input().split())
rotation = int(input()) - 1

while len(name) > 1:
    name.rotate(-rotation) # ротация наобратно
    exited_name = name.popleft()
    print(f"Removed {exited_name}")

print(f"Last is {name.popleft()}")
