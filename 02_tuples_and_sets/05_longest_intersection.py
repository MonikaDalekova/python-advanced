n = int(input())
longest_length = []

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = (int(y) for y in first_range.split(","))
    second_start, second_end = (int(x) for x in second_range.split(","))
    first_set = {num for num in range(first_start, first_end+1)}
    second_set = {num for num in range(second_start, second_end+1)}
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) >= len(longest_length):
        longest_length = list(current_intersection)

print(f'Longest intersection is {longest_length} with length {len(longest_length)}')
