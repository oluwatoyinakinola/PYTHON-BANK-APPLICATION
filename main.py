import database

#agent actions
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


# customer actions
def create_account():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    password = input("Enter a password: ")
    balance = float(input("Enter the initial balance: "))

    database.create_account(fname, lname, password, balance)

def view_account_info():
    account_number = int(input("Enter your account number: "))

    customer_info = database.get_customer_info(account_number)
    if customer_info:
        print(f"Name: {customer_info['First Name']} {customer_info['Last Name']}")
        print(f"Balance: {customer_info['Balance']}")
    else:
        print("Invalid account number or account not found.")



def make_transfer():
    sender_account_number = int(input("Enter your account number: "))
    receiver_account_number = int(input("Enter receiver's account number: "))
    amount = float(input("Enter the amount to transfer: "))

    sender_info = database.get_customer_info(sender_account_number)
    receiver_info = database.get_customer_info(receiver_account_number)

    if sender_info and receiver_info:
        sender_balance = float(sender_info['Balance'])
        receiver_balance = float(receiver_info['Balance'])

        if sender_balance >= amount:
            sender_balance -= amount
            receiver_balance += amount

            database.update_balance(sender_account_number, sender_balance)
            database.update_balance(receiver_account_number, receiver_balance)

            print("Transfer successful.")
        else:
            print("Insufficient funds. Transfer failed.")
    else:
        print("Invalid account number(s) or account not found.")


def reset_password():
    account_number = int(input("Enter your account number: "))

    customer_info = database.get_customer_info(account_number)
    if customer_info:
        old_password = input("Enter old password: ")

        if old_password == customer_info['Password']:
            new_password = input("Enter new password: ")
            database.reset_password(account_number, new_password)
            print("Password reset successful.")
        else:
            reset_option = input("Forgot password? (yes/no): ")

            if reset_option.lower() == 'yes':
                last_name = input("Enter your last name: ")

                if last_name == customer_info['Last Name']:
                    new_password = input("Enter new password: ")
                    database.reset_password(account_number, new_password)
                    print("Password reset successful.")
                else:
                    print("Invalid last name. Password reset failed.")
            else:
                print("Invalid old password. Password reset failed.")
    else:
        print("Invalid account number.")

def customer_actions():
    while True:
        print("\nCustomer Actions:")
        print("1. Create account")
        print("2. View account information")
        print("3. Make a transfer")
        print("4. Reset password")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account_info()
        elif choice == "3":
            make_transfer()
        elif choice == "4":
            reset_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


# main function
def main():
    while True:
        print("\nWelcome to the Bank System!")
        print("1. Agent Actions")
        print("2. Customer Actions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            agent_actions()
        elif choice == "2":
            customer_actions()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
