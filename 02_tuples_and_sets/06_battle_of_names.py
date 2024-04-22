n = int(input())
set_even = set()
set_odd = set()
for row in range(1, n+1):
    name = input()
    result = sum([int(ord(letter))for letter in name]) // row
    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)
sum_set_even = sum(set_even)
sum_set_odd = sum(set_odd)
if sum_set_odd == sum_set_even:
    final_result = [str(x) for x in list(set_even.union(set_odd))]
elif sum_set_odd > sum_set_even:
    final_result = [str(x) for x in list(set_odd.difference(set_even))]
else:
    final_result = [str(x) for x in list(set_even.symmetric_difference(set_odd))]
print(*final_result, sep=", ")
