from collections import deque
# for every pump in range n, we put oil and distance as list in a queue
pumps_date = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_date_copy = pumps_date.copy()
gas_in_tank = 0
index = 0
while pumps_date_copy:
    petrol, distance = pumps_date_copy.popleft()
    gas_in_tank += petrol
    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_date.rotate(-1)
        pumps_date_copy = pumps_date.copy()
        index += 1
        gas_in_tank = 0
print(index)

