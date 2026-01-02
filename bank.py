import datetime
import google.generativeai as genai
from colorama import Fore, init

# 1. Initialize Colorama (Colors)
init(autoreset=True)

# 2. Configure the AI Brain (Gemini)
# ⚠️ SECURITY NOTE: In a real job, never hide keys in code. Use Environment Variables.
genai.configure(api_key="AIzaSyAnvuxuaMDF6NAVLdiA3JxK9HWaZljXk5g")
model = genai.GenerativeModel('gemini-2.5-flash')


def ask_ai_advisor():
    print(f"\n{Fore.CYAN}🤖 AI FINANCIAL ADVISOR ONLINE...")
    print(f"{Fore.CYAN}Example: 'How can I save for a car?' or 'Explain inflation.'")

    while True:
        question = input(f"\n{Fore.WHITE}Ask a question (or type 'exit'): ")

        if question.lower() == "exit":
            print("🤖 disconnecting AI...")
            break

        print(f"{Fore.YELLOW}Thinking...")

        try:
            # We add a hidden instruction so it acts like a Banker
            prompt = f"Act as a professional financial advisor. Keep answers short and helpful. User asks: {question}"
            response = model.generate_content(prompt)

            print(f"\n{Fore.GREEN}💡 AI ADVICE:")
            print(f"{Fore.WHITE}{response.text}")
            print("-" * 50)

        except Exception as e:
            print(f"{Fore.RED}❌ Connection Error: {e}")


# --- CLASS 1: THE ROBOT (Account) ---
class Account:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.history.append(f"[{date}] Deposited: ${amount}")
        print(f"{Fore.GREEN}✅ Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.history.append(f"[{date}] Withdrew: ${amount}")
            print(f"{Fore.CYAN}📉 Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print(f"{Fore.RED}⚠️ Insufficient Funds!")

    def print_statement(self):
        print(f"\n{Fore.YELLOW}--- 📜 Statement for {self.owner} ---")
        for item in self.history:
            print(item)
        print(f"{Fore.YELLOW}💰 Final Balance: ${self.balance}\n")


# --- CLASS 2: THE MANAGER (BankSystem) ---
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
        print(f"{Fore.GREEN}✅ Welcome, {name}")

        while True:
            print(f"\n{Fore.MAGENTA}--- 🏦 SMART BANK MENU ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View History")
            print(f"{Fore.CYAN}5. 🤖 Ask AI Advisor")  # <--- NEW OPTION
            print("6. Exit")

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
                ask_ai_advisor()  # <--- Triggers the AI
            elif choice == "6":
                print(f"{Fore.MAGENTA}Goodbye!")
                break


if __name__ == "__main__":
    app = BankSystem()
    app.main_menu()