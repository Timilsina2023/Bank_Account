# BankAccount Management System

## Overview
This is a simple Bank Account Management System implemented in Python. The system allows users to create a bank account, deposit funds, withdraw funds, and check the current balance. This is a beginner-friendly project that demonstrates the basic concepts of object-oriented programming (OOP) in Python.

## Features
- Create a bank account with name, phone number, and initial balance.
- Deposit funds into the account.
- Withdraw funds from the account.
- Check the current balance of the account.
- Validation for deposit and withdrawal amounts.

## Technologies Used
The project is implemented using the following technologies and libraries:

- **Python 3.x**: The programming language used to develop the project.
- **Built-in Libraries**:
  - `print()` - Used to display output messages.
  - `f-string` - Used for formatted string literals to format output.

## Installation
To get a local copy up and running, follow these simple steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/bank-account-system.git
   ```
2. **Navigate to Project Directory:**
   ```bash
   cd bank-account-system
   ```
3. **Run the Python Script:**
   ```bash
   python bank_account.py
   ```

## Usage
The following snippet demonstrates the usage of the `BankAccount` class:

```python
class BankAccount:
    def __init__(self, name, phone, balance=0.00):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Successful deposit {amount:.2f} to {self.name} account")
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
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
```

## Output Example
```
Successful deposit 5000.00 to Ram Thapa account
withdraw $1000.00 from Ram Thapa's account.
Ram Thapa's current balance: $4000.00
```

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

