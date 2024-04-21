first_set_len, second_set_len = [int(x) for x in input().split()]
first_set = {int(input()) for _ in range(first_set_len)}
second_set = {int(input()) for _ in range(second_set_len)}
result = first_set.intersection(second_set)
for el in result:
    print(el)