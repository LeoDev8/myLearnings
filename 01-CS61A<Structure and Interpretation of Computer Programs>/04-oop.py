# Object-oriented Programming
class Account():
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

if __name__ == "__main__":
    print("<<<< Test Codes Start >>>>")
    
    a = Account("John")
    b = Account("Mark")
    print(a, a.holder, a.balance)
    print(b, b.holder, b.balance)
    
    a.deposit(100)
    print(a.balance, b.balance)
    print(b.withdraw(100))
    
    print("<<<<  Test Codes End  >>>>")
