class BankAccount:
    def __init__(self, name, phone, balance=0.00):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        if amount >=0:
            self.balance += amount
            print(f"Successful deposit {amount:.2f} to {self.name} account")
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"withdraw ${amount:.2f} from {self.name}'s account.")
        else:
            print("Invalid withdraw Amount or Insufficient Balance")

    def get_amount(self):
        return f"{self.name}'s current balance: ${self.balance:.2f}"

Ram = BankAccount("Ram Thapa", "98888888")
Ram.deposit(5000)
Ram.withdraw(1000)

print(Ram.get_amount())
