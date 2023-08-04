import database

def deposit_money():
    account_number = int(input("Enter customer's account number: "))
    amount = float(input("Enter the amount to deposit: "))

    customer_info = database.get_customer_info(account_number)
    if customer_info:
        current_balance = float(customer_info['Balance'])  
        new_balance = current_balance + amount
        database.update_balance(account_number, new_balance)
        print("Deposit successful.")
    else:
        print("Invalid account number or account not found.")


def reset_customer_password():
    customer_account_number = int(input("Enter the customer's account number: "))
    new_password = input("Enter the new password: ")

    database.reset_password(customer_account_number, new_password)

# this function executes the agents action
def agent_actions():
    while True:
        print("\nAgent Actions:")
        print("1. Deposit money into customer's account")
        print("2. Reset customer's password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            deposit_money()
        elif choice == "2":
            reset_customer_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
