from collections import deque
duration_green_light = int(input()) # enter and exit under green light
duration_yellow_light = int(input()) # only exit under green light
waiting_cars = deque()
fully_passed_cars = 0
command = input()
while command != "END":
    if command != "green":
        waiting_cars.append(command)
    else:
        current_green = duration_green_light
        while current_green > 0 and waiting_cars:
            car = waiting_cars.popleft()
            time = current_green + duration_yellow_light
            if len(car) > time:
                print(f"A crash happened! \n{car} was hit at {car[time]}.")
                raise SystemExit
            current_green -= len(car)
            fully_passed_cars += 1
    command = input()
print(f"Everyone is safe.\n{fully_passed_cars} total cars passed the crossroads.")
