from collections import deque

amount_of_money = [int(x) for x in input().split()] #stack
prices_of_food = deque(int(x) for x in input().split())
food_count = 0

while amount_of_money and prices_of_food:
    current_money = amount_of_money.pop()
    current_price = prices_of_food.popleft()

    if current_money == current_price:
        food_count += 1
        continue
    elif current_money < current_price:
        continue
    elif current_money > current_price:
        food_count += 1
        change = current_money - current_price
        if len(amount_of_money) > 1:
            current_money = amount_of_money.pop()
            current_money += change
            amount_of_money.append(current_money)
        else:
            amount_of_money.append(change)

if food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")