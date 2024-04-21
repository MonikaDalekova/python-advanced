number_of_guests = int(input())
reserved = set()
come = set()
missing = set()

for guests in range(number_of_guests):
    reserved.add(input())

while True:
    comming = input()
    if comming == "END":
        break
    come.add(comming)
missing = reserved.difference(come)
print(len(missing))
for guest in sorted(missing):
    print(guest)