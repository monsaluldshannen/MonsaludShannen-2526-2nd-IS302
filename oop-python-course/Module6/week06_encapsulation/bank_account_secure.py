class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account_shnn = BankAccount(5000)
account_shnn.deposit(1000)
account_shnn.withdraw(2000)
print("Balance:", account_shnn.get_balance())
