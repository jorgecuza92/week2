

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)


checking_account = BankAccount('FDS8223', 100)
checking_account.deposit(50)
print(checking_account.balance)
checking_account.withdraw(20)
print(checking_account.balance)

savings_account = BankAccount('FDS2342', 500)
checking_account.transer(50, savings_account)

print(f"Savings Account Number {savings_account.account_number}\nBalance: {savings_account.balance}")

