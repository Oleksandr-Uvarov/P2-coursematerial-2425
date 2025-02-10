class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
        self.__transactions = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__log_transaction("deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__log_transaction("withdraw", amount)

    def __log_transaction(self, transaction_type, amount):
        self.__transactions.append((transaction_type, amount))
        print(f"Logged {transaction_type} of amount: {amount}")

    @property
    def transaction_history(self):
        return self.__transactions.copy()
    


bank_account = BankAccount("a")
print(bank_account.__log_transaction)