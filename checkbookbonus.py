import os
import datetime

def welcome():
    """
    Prints a welcome message and the options available to the user.
    """
    print(' ')
    print("Welcome to your checkbook!")
    print("What would you like to do?")
    print(' ')
    print("1. View balance")
    print("2. Withdraw cash (Debit)")
    print("3. Deposit cash (Credit)")
    print("4. View transactions")
    print("5. Exit")

def get_balance():
    """
    Reads the transactions from the ledgerbonus.txt file and calculates the current balance.

    Returns:
    float: The current balance.
    """
    balance = 0
    if os.path.exists("ledgerbonus.txt"):
        with open("ledgerbonus.txt", "r") as f:
            for line in f:
                transaction = line.strip().split(", ")
                if transaction[1] == "credit":
                    balance += float(transaction[2].replace("$", "").replace(",", ""))
                elif transaction[1] == "debit":
                    balance -= float(transaction[2].replace("$", "").replace(",", ""))
    return balance

def view_balance():
    """
    Prints the current balance to the console.
    """
    balance = get_balance()
    print(f"Your current balance is: ${balance:.2f}")

def add_debit():
    """
    Prompts the user to enter the amount and description of the debit and writes the transaction to the ledgerbonus.txt file.
    """
    amount = input("Enter the amount to withdraw: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    description = input("Enter a description for the transaction (optional): ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ledgerbonus.txt", "a") as f:
        # f.write(f"debit,{amount},'{description}',{timestamp}\n")
        f.write(f"{timestamp}, debit, ${amount:.2f}, Description: {description}\n")
    print(f"${amount:.2f} removed from your account.")
    print(f"Your new balance is: ${get_balance():.2f}")

def add_credit():
    """
    Prompts the user to enter the amount and description of the credit and writes the transaction to the ledgerbonus.txt file.
    """
    amount = input("Enter the amount to add: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    description = input("Enter a description for the transaction (optional): ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ledgerbonus.txt", "a") as f:
        # f.write(f"credit,{amount},'{description}',{timestamp}\n")
        f.write(f"{timestamp}, credit, ${amount:.2f}, Description: {description}\n")
    print(f"${amount:.2f} added to your account.")
    print(f"Your new balance is: ${get_balance():.2f}")

def view_transactions():
    """
    Prints the last n transactions to the console.
    """
    n = input("Enter the number of transactions to view: ")
    try:
        n = int(n)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    transactions = []
    if os.path.exists("ledgerbonus.txt"):
        with open("ledgerbonus.txt", "r") as f:
            for line in f:
                transactions.append(line.strip())
    if n > len(transactions):
        n = len(transactions)
        print(f"You only have {n} transactions.")
    print(f"Here are your last {n} transactions:")
    for transaction in transactions[-n:]:
        print(transaction)

def main():
    """
    The main function that runs the checkbook program.
    """
    while True:
        welcome()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_balance()
        elif choice == "2":
            add_debit()
        elif choice == "3":
            add_credit()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()