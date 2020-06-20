water = 400  # ml
milk = 540  # ml
money = 550  # $
beans = 120  # gms
cups = 9  # count
actions = ["buy", "fill", "take", "remaining", "exit"]


def what_machine_has():
    while True:
        print("The coffee machine has:")
        print(water, " of water")
        print(milk, "of milk")
        print(beans, "of coffee beans")
        print(cups, "of disposable cups")
        print(money, "of money")
        break


def not_enough(a, local_water, local_milk, local_beans, local_cups):
    if local_cups < 1:
        print("Sorry, not enough cups!")
    elif a == '1':
        if local_water < 250:
            print("Sorry, not enough water!")
        if beans < 6:
            print("Sorry, not enough beans!")
    if a == '2':
        if local_water < 350:
            print("Sorry, not enough water!")
        if local_milk < 75:
            print("Sorry, not enough milk!")
        if local_beans < 20:
            print("Sorry, not enough beans!")
    if a == '3':
        if local_water < 200:
            print("Sorry, not enough water!")
        if local_milk < 100:
            print("Sorry, not enough milk!")
        if local_beans < 12:
            print("Sorry, not enough beans!")


def perform_action(action):
    while True:
        global water
        global milk
        global money
        global beans
        global cups
        if action == 'remaining':
            what_machine_has()
        elif action == 'take':
            print("I gave you $", + money)
            money -= money
        elif action == 'fill':
            print("Write how many ml of water do you want to add:")
            water += int(input())
            print("Write how many ml of milk do you want to add:")
            milk += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            beans += int(input())
            print("Write how many disposable cups of coffee do you want to add:")
            cups += int(input())
        elif action == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            buy_option = input()
            if buy_option == 'back':
                break
            elif buy_option == '1':
                if water >= 250 and beans >= 6 and cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 250
                    beans -= 16
                    money += 4
                    cups -= 1
                else:
                    not_enough(buy_option, water, milk, beans, cups)
                    break
            elif buy_option == '2':
                if water >= 350 and beans >= 20 and milk >= 75 and cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 350
                    milk -= 75
                    beans -= 20
                    money += 7
                    cups -= 1
                else:
                    not_enough(buy_option, water, milk, beans, cups)
                    break
            elif buy_option == '3':
                if water >= 200 and beans >= 12 and milk >= 100 and cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 200
                    milk -= 100
                    beans -= 12
                    money += 6
                    cups -= 1
                else:
                    not_enough(buy_option, water, milk, beans, cups)
                    break
            else:
                continue


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input != 'exit':
        perform_action(user_input)
    else:
        continue
