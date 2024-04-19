from collections import deque

quantity_of_water = int(input())
people = deque()

name = input()
while name != "Start":
    people.append(name)

    name = input()

command = input()
while command != "End":
    data = command.split()
    if "refill" in data:
        litres = int(data[1])
        quantity_of_water += litres
    else:
        litres = int(data[0])
        if quantity_of_water >= litres:
            quantity_of_water -= litres
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")

    command = input()

print(f"{quantity_of_water} liters left")