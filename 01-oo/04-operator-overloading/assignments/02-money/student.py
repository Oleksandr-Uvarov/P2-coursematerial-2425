class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    
    def __add__(self, money):
        if self.currency == money.currency:
            return Money(self.amount + money.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")
        
    
    def __sub__(self, money):
        if self.currency == money.currency:
            return Money(self.amount - money.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")


    def __mul__(self, value):
        return Money(self.amount * value, self.currency)