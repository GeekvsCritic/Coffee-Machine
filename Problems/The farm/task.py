Chicken = 23
Goat = 678
Pig = 1296
Cow = 3848
Sheep = 6769
money = int(input())
# print(max(Chicken, Goat, Pig, Cow, Sheep))

if money >= Sheep:
    buy_sheep = money // Sheep
    print(buy_sheep, "sheep")
elif money >= Cow:
    buy_cow = money // Cow
    if buy_cow == 1:
        print(buy_cow, "cow")
    else:
        print(buy_cow, "cows")
elif money >= Pig:
    buy_pig = money // Pig
    if buy_pig == 1:
        print(buy_pig, "pig")
    else:
        print(buy_pig, "pigs")
elif money >= Goat:
    buy_goat = money // Goat
    if buy_goat == 1:
        print(buy_goat, "goat")
    else:
        print(buy_goat, "goats")
elif money >= Chicken:
    buy_chicken = money // Chicken
    if buy_chicken == 1:
        print(buy_chicken, "chicken")
    else:
        print(buy_chicken, "chickens")
else:
    print("None")
