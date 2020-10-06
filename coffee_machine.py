class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.run()

    def run(self):
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.remaining()
        elif action == 'exit':
            exit()

    def buy(self):
        action = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "
        )
        if action in ['1', '2', '3']:
            if self.water >= 400 and self.milk >= 75 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                if action == '1':
                    self.espresso()
                elif action == '2':
                    self.latte()
                elif action == '3':
                    self.cappuccino()
            else:
                print('Sorry, not enough water!')
                self.run()
        else:
            self.run()

    def remaining(self):
        print(f"""
            The coffee machine has:
            {self.water} of water
            {self.milk} of milk
            {self.beans} of coffee beans
            {self.cups} of disposable cups
            ${self.money} of money
            """)
        self.run()

    def espresso(self):
        self.water -= 250
        self.beans -= 16
        self.cups -= 1
        self.money += 4
        self.run()

    def latte(self):
        self.water -= 350
        self.milk -= 75
        self.beans -= 20
        self.cups -= 1
        self.money += 7
        self.run()

    def cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.beans -= 12
        self.cups -= 1
        self.money += 6
        self.run()

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        self.run()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money
        self.run()


client = CoffeeMachine()
