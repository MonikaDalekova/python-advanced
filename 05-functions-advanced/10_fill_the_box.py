from collections import deque


def fill_the_box(height, length, width, *args):
    space_box = height * length * width
    number_cubes = deque(args)
    while number_cubes[0] != "Finish":
        space_box -= number_cubes.popleft()
    if space_box < 0:
        left_cubes = sum(c for c in number_cubes if c != "Finish")
        return f"No more free space! You have {left_cubes + abs(space_box)} more cubes."
    else:
        return f"There is free space in the box. You could put {space_box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))