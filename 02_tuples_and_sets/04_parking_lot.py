number_of_commands = int(input())
parking = set()
for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking.add(car_number)
    elif direction == "OUT":
        parking.remove(car_number)
if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")