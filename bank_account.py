class BankAccount:
    total_accounts = 0
    all_accounts = []
    
    def _init_(self, account_holder, initial_balance=0, account_type="Current"):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        self.account_type = account_type
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)
        print(f"New {self.account_type} Account created for {self.account_holder}.")

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")
            print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        fee = 10  
        min_balance = 1000 if self.account_type == "Savings" else 0  

        if amount + fee > self.balance - min_balance:
            print("Insufficient funds or minimum balance requirement not met.")
            return

        self.balance -= (amount + fee)
        self.transactions.append(f"Withdrew ₹{amount}, Fee: ₹{fee}. New Balance: ₹{self.balance}")
        print(f"₹{amount} withdrawn. New Balance: ₹{self.balance}")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred ₹{amount} to {recipient.account_holder}. New Balance: ₹{self.balance}")
            recipient.transactions.append(f"Received ₹{amount} from {self.account_holder}. New Balance: ₹{recipient.balance}")
            print(f"Transfer successful. ₹{amount} sent to {recipient.account_holder}.")
        else:
            print("Insufficient funds for transfer.")

    def check_balance(self):
        print(f"{self.account_holder}'s Balance: ₹{self.balance}")

    def get_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

    @classmethod
    def total_bank_accounts(cls):
        print(f"Total Bank Accounts: {cls.total_accounts}")

    @staticmethod
    def validate_amount(amount):
        if 0 < amount <= 50000:
            return True
        print("Invalid amount! Transactions over ₹50,000 are not allowed.")
        return False


class SavingsAccount(BankAccount):
    def _init_(self, account_holder, initial_balance=0):
        super()._init_(account_holder, initial_balance, "Savings")

    def apply_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest applied: ₹{interest}. New Balance: ₹{self.balance}")
        print(f"Interest of ₹{interest} added. New Balance: ₹{self.balance}")


class CurrentAccount(BankAccount):
    def _init_(self, account_holder, initial_balance=0):
        super()._init_(account_holder, initial_balance, "Current")


def find_account(name):
    for account in BankAccount.all_accounts:
        if account.account_holder == name:
            return account
    return None


def main():
    print("\nWelcome to the Bank Management System!")
    while True:
        print("\nChoose an option:")
        print("1. Open an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. View Transaction History")
        print("7. Show Total Accounts")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter Account Holder Name: ")
            acc_type = input("Enter Account Type (Savings/Current): ").strip().capitalize()
            balance = float(input("Enter Initial Deposit Amount: "))
            if acc_type == "Savings":
                account = SavingsAccount(name, balance)
            else:
                account = CurrentAccount(name, balance)

        elif choice == "2":
            name = input("Enter Account Holder Name: ")
            account = find_account(name)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter Account Holder Name: ")
            account = find_account(name)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            sender_name = input("Enter Your Account Name: ")
            recipient_name = input("Enter Recipient Account Name: ")
            sender = find_account(sender_name)
            recipient = find_account(recipient_name)
            if sender and recipient:
                amount = float(input("Enter transfer amount: "))
                sender.transfer(recipient, amount)
            else:
                print("One or both accounts not found.")

        elif choice == "5":
            name = input("Enter Account Holder Name: ")
            account = find_account(name)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == "6":
            name = input("Enter Account Holder Name: ")
            account = find_account(name)
            if account:
                account.get_transaction_history()
            else:
                print("Account not found.")

        elif choice == "7":
            BankAccount.total_bank_accounts()

        elif choice == "8":
            print("Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__=="__main__":
    main()
