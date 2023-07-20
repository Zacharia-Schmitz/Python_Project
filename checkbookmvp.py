import os

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
    print("4. Exit")

def get_balance():
    """
    Reads the transactions from the ledger.txt file and calculates the current balance.

    Returns:
    float: The current balance.
    """
    balance = 0
    # Check if the ledger.txt file exists
    if os.path.exists("ledger.txt"):
        # Open the ledger.txt file for reading
        with open("ledger.txt", "r") as f:
            # Loop through each line in the file
            for line in f:
                # Split the line into a list of strings using the comma as a delimiter
                transaction = line.strip().split(",")
                # If the transaction is a credit, add the amount to the balance
                if transaction[0] == "credit":
                    balance += float(transaction[1])
                # If the transaction is a debit, subtract the amount from the balance
                elif transaction[0] == "debit":
                    balance -= float(transaction[1])
    # Return the current balance
    return balance

def view_balance():
    """
    Prints the current balance to the console.
    """
    # Get the current balance
    balance = get_balance()
    # Print the balance to the console with two decimal places
    print(f"Your current balance is: ${balance:.2f}")

def add_debit():
    """
    Prompts the user to enter the amount of the debit and writes the transaction to the ledger.txt file.
    """
    # Prompt the user to enter the amount of the debit
    amount = input("Enter the amount of the debit: ")
    try:
        # Convert the amount to a float
        amount = float(amount)
    except ValueError:
        # If the input is not a number, print an error message and return
        print("Invalid input. Please enter a number.")
        return
    # Open the ledger.txt file for appending
    with open("ledger.txt", "a") as f:
        # Write the debit transaction to the file in the format "debit,amount"
        f.write("debit,{}\n".format(amount))
    # Print a success message and the new balance to the console
    print(f"${amount:.2f} removed from your account.")
    print(f"Your new balance is: ${get_balance():.2f}")

def add_credit():
    """
    Prompts the user to enter the amount of the credit and writes the transaction to the ledger.txt file.
    """
    # Prompt the user to enter the amount of the credit
    amount = input("Enter the amount of the credit: ")
    try:
        # Convert the amount to a float
        amount = float(amount)
    except ValueError:
        # If the input is not a number, print an error message and return
        print("Invalid input. Please enter a number.")
        return
    # Open the ledger.txt file for appending
    with open("ledger.txt", "a") as f:
        # Write the credit transaction to the file in the format "credit,amount"
        f.write(f"credit,{amount}\n")
    # Print a success message and the new balance to the console
    print(f"${amount:.2f} added to your account.")
    print(f"Your new balance is: ${get_balance():.2f}")
    
def main():
    """
    The main function that runs the checkbook program.
    """
    while True:
        # Print the welcome message and options to the console
        welcome()
        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-4): ")
        # If the user chooses option 1, view the balance
        if choice == "1":
            view_balance()
        # If the user chooses option 2, add a debit
        elif choice == "2":
            add_debit()
        # If the user chooses option 3, add a credit
        elif choice == "3":
            add_credit()
        # If the user chooses option 4, exit the program
        elif choice == "4":
            print("Goodbye!")
            break
        # If the user enters an invalid choice, print an error message
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()