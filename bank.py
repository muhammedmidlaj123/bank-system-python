import datetime
from colorama import Fore, Style, init

# Initialize colorama (autoreset means color goes back to normal after each print)
init(autoreset=True)


class Account:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.history.append(f"[{date}] Deposited: ${amount}")

        # GREEN text for positive things
        print(f"{Fore.GREEN}✅ Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.history.append(f"[{date}] Withdrew: ${amount}")

            # CYAN (Blue-ish) text for withdrawals
            print(f"{Fore.CYAN}📉 Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            # RED text for errors
            print(f"{Fore.RED}⚠️ Insufficient Funds! Transaction blocked.")

    def print_statement(self):
        print(f"\n{Fore.YELLOW}--- 📜 Statement for {self.owner} ---")
        for item in self.history:
            print(item)
        print(f"{Fore.YELLOW}💰 Final Balance: ${self.balance}\n")


# --- (The rest of your BankSystem class stays exactly the same) ---
class BankSystem:
    def __init__(self):
        self.accounts = []

    def find_account(self, name_to_find):
        for account in self.accounts:
            if account.owner == name_to_find:
                return account
        return None

    def create_account(self):
        name = input("Enter your name: ")
        new_account = Account(name)
        self.accounts.append(new_account)
        print(f"{Fore.GREEN}✅ Account created for {name}")

    def deposit_money(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)
        if selected_account is not None:
            amt = int(input("Enter amount: "))
            selected_account.deposit(amt)
        else:
            print(f"{Fore.RED}❌ Account doesn't exist")

    def withdraw_money(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)

        if selected_account is not None:
            amt = int(input("Enter amount to withdraw: "))
            selected_account.withdraw(amt)
        else:
            print(f"{Fore.RED}❌ Account doesn't exist")

    def view_history(self):
        name = input("Enter your name: ")
        selected_account = self.find_account(name)

        if selected_account is not None:
            selected_account.print_statement()
        else:
            print(f"{Fore.RED}❌ Account doesn't exist")

    def main_menu(self):
        name = input("Enter your name to login: ")
        # We assume the file handling is fine, just added a color print
        with open("database.txt", "a") as file:
            file.write(name + "\n")
            print(f"{Fore.GREEN}✅ Login saved to hard drive")

        while True:
            print(f"\n{Fore.MAGENTA}--- 🏦 BANK MENU ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View History")
            print("5. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.view_history()
            elif choice == "5":
                print(f"{Fore.MAGENTA}Goodbye!")
                break


if __name__ == "__main__":
    app = BankSystem()
    app.main_menu()