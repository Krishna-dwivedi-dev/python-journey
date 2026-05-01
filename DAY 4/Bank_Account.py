# Day 4: Instance Methods and Object State
# Q1 & Q2 - BankAccount with transaction tracking

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1
        print(f"Deposited! New Balance = ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            self.transaction_count += 1
            print(f"Withdrawn! Remaining Balance = ₹{self.balance}")

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Balance: ₹{self.balance}")
        print(f"Transactions: {self.transaction_count}")

# Test
BankAccount1 = BankAccount("Krishna Dwivedi", 1080000)
BankAccount1.display()
BankAccount1.deposit(90500)
BankAccount1.withdraw(650000)
BankAccount1.display()

BankAccount2 = BankAccount("Diksha Makani", 590000)
BankAccount2.display()
BankAccount2.deposit(550000)
BankAccount2.withdraw(385000)
BankAccount2.display()