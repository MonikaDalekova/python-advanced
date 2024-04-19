from collections import deque

customers = deque()
while True:
    name = input() # import name
    if name == "Paid":
        while customers: # докато има хора в опашката
            print(customers.popleft()) # нека да се махат по реда на влизане, принтираме махнатите
        continue
    elif name == "End":
        break
    customers.append(name) # added name to our queue
print(f"{len(customers)} people remaining.")