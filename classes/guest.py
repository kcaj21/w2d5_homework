class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sufficient_funds(self, price):
            if self.money >= price.fee:
                 return True
