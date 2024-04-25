rows = int(input())
flattened = []
for i in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    flattened.extend(inner_list)
print(flattened)