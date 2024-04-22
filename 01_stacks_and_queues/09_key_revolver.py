from collections import deque

price_of_bullet = int(input()) # цена на куршум
size_gun_barrel = int(input()) # куршуми в цевта
bullets = [int(x) for x in input().split()] # back-to-front (stack)
locks = deque([int(x) for x in input().split()]) # shoot the locks front-to-back (queue)
value_of_intelligence = int(input())
count_bullets = 0
# money_earned = value_of_intelligence - price_of_bullet*count_bullets
current_bullets = size_gun_barrel
while bullets and locks:
    if bullets[-1] <= locks[0]:
        print("Bang!")
        bullets.pop()
        locks.popleft()
        count_bullets += 1
        current_bullets -= 1
        if current_bullets == 0 and bullets:
            print("Reloading!")
            current_bullets = size_gun_barrel

    else:
        print("Ping!")
        bullets.pop()
        count_bullets += 1
        current_bullets -= 1
        if current_bullets == 0 and bullets:
            print("Reloading!")
            current_bullets = size_gun_barrel
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - count_bullets * price_of_bullet}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")