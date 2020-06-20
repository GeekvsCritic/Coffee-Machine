# Write your code here
# Stage 6


class CoffeeMachine:

    def __init__(self):
        self.water = 400  # ml
        self.milk = 540  # ml
        self.money = 550  # $
        self.beans = 120  # gms
        self.cups = 9  # count

    def what_machine_has(self):
        print ( f"The coffee machine has:" +
                f"\n{self.water}  of water" +
                f"\n{self.milk} of milk" +
                f"\n{self.beans} of coffee beans" +
                f"\n{self.cups} of disposable cups" +
                f"\n${self.money} of money")

    def not_enough(self, buy_option):
        if self.cups < 1:
            print("Sorry, not enough cups!")
        elif buy_option == '1':
            if self.water < 250:
                print("Sorry, not enough water!")
            if self.beans < 6:
                print("Sorry, not enough beans!")
        if buy_option == '2':
            if self.water < 350:
                print("Sorry, not enough water!")
            if self.milk < 75:
                print("Sorry, not enough milk!")
            if self.beans < 20:
                print("Sorry, not enough beans!")
        if buy_option == '3':
            if self.water < 200:
                print("Sorry, not enough water!")
            if self.water < 100:
                print("Sorry, not enough milk!")
            if self.beans < 12:
                print("Sorry, not enough beans!")
        return

    def perform_action(self, action):
        while True:
            if action == 'remaining':
                machine.what_machine_has()
            elif action == 'take':
                print("I gave you $", + self.money)
                self.money -= self.money
            elif action == 'fill':
                print("Write how many ml of water do you want to add:")
                self.water += int(input())
                print("Write how many ml of milk do you want to add:")
                self.milk += int(input())
                print("Write how many grams of coffee beans do you want to add:")
                self.beans += int(input())
                print("Write how many disposable cups of coffee do you want to add:")
                self.cups += int(input())
            elif action == 'buy':
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                buy_option = input()
                if buy_option == 'back':
                    break
                elif buy_option == '1':
                    if self.water >= 250 and self.beans >= 6 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.beans -= 16
                        self.money += 4
                        self.cups -= 1
                    else:
                        machine.not_enough(buy_option)
                        break
                elif buy_option == '2':
                    if self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350
                        self.milk -= 75
                        self.beans -= 20
                        self.money += 7
                        self.cups -= 1
                    else:
                        machine.not_enough(buy_option)
                        break
                elif buy_option == '3':
                    if self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200
                        self.milk -= 100
                        self.beans -= 12
                        self.money += 6
                        self.cups -= 1
                    else:
                        machine.not_enough(buy_option)
                        break
                else:
                    continue
            break
        return

machine = CoffeeMachine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input != 'exit':
        machine.perform_action(user_input)
    else:
        continue

