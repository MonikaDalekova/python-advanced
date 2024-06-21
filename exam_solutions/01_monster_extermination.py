from collections import deque

monsters_armor = deque(int(x) for x in input().split(","))
strike_strength = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters_armor and strike_strength:

    current_monster = monsters_armor.popleft()
    current_strike = strike_strength.pop()

    if current_strike >= current_monster:
        current_strike -= current_monster
        killed_monsters += 1
        if len(strike_strength) > 0:
            strike_strength[-1] += current_strike
        else:
            strike_strength.append(current_strike) if current_strike > 0 else None
    else:
        current_monster -= current_strike
        monsters_armor.append(current_monster)

if not monsters_armor:
    print("All monsters have been killed!")
if not strike_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")

