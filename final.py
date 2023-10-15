import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_count = 0
        self.loan_amount = 0

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited ${amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount < 0:
            print("Invalid withdrawal amount")
        else:
            print("Withdrawal amount exceeded or invalid")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_count += 1
            self.loan_amount += amount
            self.balance += amount
            self.transaction_history.append(f"Took a loan of {amount}")
            print(f"Loan of {amount} granted. New balance: {self.balance}")
        else:
            print("Maximum number of loans reached.")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
            print(f"Transferred {amount} to {recipient.name}. New balance: {self.balance}")
        else:
            print("Insufficient funds for transfer")

    def show_info(self):
        print(f"Account Type: {self.account_type}")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

    def change_info(self, new_name):
        self.name = new_name
        print("Name changed successfully.")

    def apply_interest(self):
        print("Interest applied.")

class Admin:
    user_accounts = []
    loan_feature_enabled = True

    def create_account(self, user):
        self.user_accounts.append(user)
        print(f"Account created for {user.name}.")

    def delete_account(self, user):
        if user in self.user_accounts:
            self.user_accounts.remove(user)
            print(f"Account for {user.name} deleted.")
        else:
            print("User not found.")

    def see_all_accounts(self):
        print("All User Accounts:")
        for user in self.user_accounts:
            print(user.name)

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.user_accounts)
        print(f"Total Available Balance: ${total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_amount for user in self.user_accounts if hasattr(user, 'loan_amount'))
        print(f"Total Loan Amount: ${total_loan_amount}")

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        status = "ON" if self.loan_feature_enabled else "OFF"
        print(f"Loan feature is now {status}.")

# Example usage:
user1 = User("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = User("Alice Smith", "alice@example.com", "456 Oak St", "Current")

admin = Admin()

admin.create_account(user1)
admin.create_account(user2)

user1.deposit(1000)
user1.withdraw(500)
user1.check_balance()

user2.deposit(2000)
user2.transfer(1000, user1)
user2.check_transaction_history()

admin.see_all_accounts()
admin.check_total_balance()
admin.toggle_loan_feature()

current_user = user1

while True:
    if current_user:
        print(f"\nWelcome {current_user.name}!\n")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Show Info")
        print("4. Change Info")
        print("5. Apply Interest")
        print("6. Logout\n")

        option = input("Choose Option: ")

        if option == "1":
            amount = int(input("Enter withdrawal amount: "))
            current_user.withdraw(amount)

        elif option == "2":
            amount = int(input("Enter deposit amount: "))
            current_user.deposit(amount)

        elif option == "3":
            current_user.show_info()

        elif option == "4":
            new_name = input("Enter new name: ")
            current_user.change_info(new_name)

        elif option == "5":
            if hasattr(current_user, 'apply_interest'):
                current_user.apply_interest()
            else:
                print("Interest not applicable for this account type.")

        elif option == "6":
            current_user = None
            print("Logged out.")

    else:  # Admin options
        print("\nAdmin Menu:")
        print("1. See All User Accounts")
        print("2. Check Total Balance")
        print("3. Check Total Loan Amount")
        print("4. Toggle Loan Feature")
        print("5. Logout\n")

        admin_option = input("Choose Option: ")

        if admin_option == "1":
            admin.see_all_accounts()

        elif admin_option == "2":
            admin.check_total_balance()

        elif admin_option == "3":
            admin.check_total_loan_amount()

        elif admin_option == "4":
            admin.toggle_loan_feature()

        elif admin_option == "5":
            break