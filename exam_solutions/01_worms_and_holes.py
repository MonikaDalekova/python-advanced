from collections import deque

worms = [int(x) for x in input().split()] #stack
worms_copy = worms.copy()
holes = deque(int(x) for x in input().split())
matches = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole == current_worm:
        matches += 1
        continue
    else:
        worms.append(current_worm-3)
        if worms[-1] <= 0:
            worms.pop()

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if not worms and len(worms_copy) == matches:
    print("Every worm found a suitable hole!")
elif not worms and len(worms_copy) > matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")