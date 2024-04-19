#1
from collections import deque

daily_food_quantity = int(input())
each_order_quantity = deque(int(x) for x in input().split())
biggest = max(each_order_quantity)
print(biggest)
while each_order_quantity and each_order_quantity[0] <= daily_food_quantity:
    daily_food_quantity -= each_order_quantity[0]
    each_order_quantity.popleft()

if each_order_quantity:
    print(f"Orders left: ", end='')
    while each_order_quantity:
        print(each_order_quantity.popleft(), end=' ')
else:
    print("Orders complete")



