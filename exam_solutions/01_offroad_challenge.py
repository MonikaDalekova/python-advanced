from collections import deque

initial_fuel = [int(x) for x in input().split()] #stack
consumption_index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())
fail = False
counter_altitude = 0
altitude = len(initial_fuel)

while initial_fuel and consumption_index:
    current_fuel = initial_fuel.pop()
    current_consumption = consumption_index.popleft()
    current_fuel_needed = fuel_needed.popleft()

    current_diff = current_fuel - current_consumption
    if current_diff >= current_fuel_needed:
        counter_altitude += 1
        print(f"John has reached: Altitude {counter_altitude}")
    else:
        print(f"John did not reach: Altitude {counter_altitude+1}")
        fail = True
        break

if fail:
    print("John failed to reach the top.")
    if counter_altitude > 0:
        print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, counter_altitude+1)])}")
    else:
        print("John didn't reach any altitude.")
elif counter_altitude == altitude:
    print("John has reached all the altitudes and managed to reach the top!")