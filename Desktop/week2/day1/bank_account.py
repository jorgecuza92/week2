
# Activity 2 - Bank Account

# In this activity, you are going to model a bank account.
#
# - Create a class called **BankAccount**.
# - Add properties for **balance** and **account_number**
# - Allow the user to deposit funds to the account. This can be accomplished by adding a **deposit** function to the BankAccount class.
# - Allow the user to withdraw funds from the account. This can be accomplished by adding a **withdraw** function to the BankAccount class.
# - Allow the user to transfer funds between two accounts. This can be accomplished by adding a **transfer_funds** function to the BankAccount class.
# - After creating the BankAccount class, along with all the functions make sure to create instance of BankAccount and perform actions.
#
# **Example:**
#
# ```
# checking_account = BankAccount("FD332", 100)
# checking_account.deposit(50)
# print(checking_account.balance) # $150
# ```
# ___________


class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
        self.withdraw = ''
        self.deposit = int
        self.transfer_funds =

    def deposit(self, deposit):
        self.deposit = 100
    def withdraw(self, withdraw):
        self.withdraw = ''

    def transfer_funds(self):
        self.transfer_funds =

checkings_account = BankAccount(120, '123456790')
checkings_account.trasnfer_funds =


