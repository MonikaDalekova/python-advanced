box_of_clothes = [int(x) for x in input().split()]
capacity_per_rack = int(input())
count_racks = 0

while box_of_clothes:
    count_racks += 1
    current_capacity = capacity_per_rack
    while box_of_clothes and box_of_clothes[-1] <= current_capacity:
        current_capacity -= box_of_clothes.pop()

print(count_racks)