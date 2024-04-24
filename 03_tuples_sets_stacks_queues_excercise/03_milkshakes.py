from collections import deque
milkshakes = 0
chocolates = [int(x) for x in input().split(", ")] # stack, start from last chocolate
cups_of_milk = deque([int(x) for x in input().split(", ")])  # queue, start from first cup

while milkshakes < 5 and len(chocolates) > 0 and len(cups_of_milk) > 0: # вадим стойностите и след това започваме да ги връшаме
    while milkshakes != 5 and chocolates and cups_of_milk:
        chocolate = chocolates.pop()
        cup_of_milk = cups_of_milk.popleft()

        if chocolate <= 0 and cup_of_milk <= 0:
            continue
        elif chocolate <= 0:
            cups_of_milk.appendleft(cup_of_milk)
            continue
        elif cup_of_milk <= 0:
            chocolates.append(chocolate)
            continue

        if cup_of_milk == chocolate:
            milkshakes += 1
        else:
            cups_of_milk.append(cup_of_milk)
            chocolates.append(chocolate - 5)


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print("Chocolate: ", end='')
    print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")
if cups_of_milk:
    print("Milk: ", end='')
    print(*cups_of_milk, sep=', ')
else:
    print("Milk: empty")