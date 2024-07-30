class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def check_balance(self):
        print(f"Current balance for account {self.name}: {self.balance}")

class Bank:
    def __init__(self,bankname):
        self.bankname=bankname
        self.accounts = {}
 
    def create_account(self, name, initial_balance):
        if name not in self.accounts:
            self.accounts[name] = Account(name, initial_balance)
            print(f"Account created successfully for {name}. Initial balance: {initial_balance}")
        else:
            print("Account already exists.")
            
    def access_account(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account does not exist.")
            return None
def main():
    bankname=input("Enter Bank Name: ")
    bank = Bank(bankname)
    
    while True:
        print(f"\nWelcome to the {bank.bankname}")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)
        elif choice == '2':
            name = input("Enter account holder's name: ")
            account = bank.access_account(name)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Go back")
                    option = input("Enter your option: ")
                    if option == '1':
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                    elif option == '2':
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    elif option == '3':
                        account.check_balance()
                    elif option == '4':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print(f"Exiting {bank.bankname}.Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
