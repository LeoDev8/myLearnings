# Object-oriented Programming
class Account():
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance

"""
Account Types
"""
class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

class SavingAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
"""
Clever Bank Marketing Exexutive wants:
- Low interest rate of 1%
- A $1 fee for withdrawals
- A $2 fee for deposits
- A free dollar when you open your account
"""
class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

# Object-Oriented Design
class Bank:
    """ A bank *has* accounts
    
    >>> bank = Bank()
    >>> john = bank.open_account("John", 10)
    >>> jack = bank.open_account("jack", 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        new_account = kind(holder)
        new_account.deposit(amount)
        self.accounts.append(new_account)
        return new_account
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    def too_big_to_fail(self):
        return len(self.accounts) > 1


if __name__ == "__main__":
    print("<<<< Test Codes Start >>>>")
    
    # a = Account("John")
    # b = Account("Mark")
    # print(a, a.holder, a.balance)
    # print(b, b.holder, b.balance)
    
    # a.deposit(100)
    # print(a.balance, b.balance)
    # print(b.withdraw(100))
    
    print("<<<<  Test Codes End  >>>>")
