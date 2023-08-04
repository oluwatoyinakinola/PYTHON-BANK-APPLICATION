import random

CUSTOMER_FILE = 'customers.txt'
AGENT_FILE = 'agents.txt'

def generate_account_number():
    return random.randint(10000000, 99999999)

def write_to_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + '\n')

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def create_account(fname, lname, password, balance=0):
    account_number = generate_account_number()
    customer_info = f"Account Number: {account_number}, First Name: {fname}, Last Name: {lname}, Password: {password}, Balance: {balance}"
    write_to_file(CUSTOMER_FILE, customer_info)
    print("Account created successfully.")
    print(f"Account Number: {account_number}")

def parse_customer_data(data):
    customer = {}
    data = data.strip().split(', ')
    for item in data:
        key_value = item.split(': ')
        if len(key_value) == 2:
            key, value = key_value
            if key == 'Account Number':
                value = int(value)  
            customer[key] = value
    return customer

def get_customer_info(account_number):
    customers = read_from_file(CUSTOMER_FILE)
    for customer in customers:
        customer_data = parse_customer_data(customer)
        if 'Account Number' in customer_data and customer_data['Account Number'] == account_number:
            return customer_data
    return None

def update_balance(account_number, new_balance):
    customers = read_from_file(CUSTOMER_FILE)
    updated_customers = []
    for customer in customers:
        customer_data = parse_customer_data(customer)
        if 'Account Number' in customer_data and customer_data['Account Number'] == account_number:
            customer_data['Balance'] = new_balance
        updated_customer = ', '.join([f"{key}: {value}" for key, value in customer_data.items()])
        updated_customers.append(updated_customer)
    with open(CUSTOMER_FILE, 'w') as file:
        file.write('\n'.join(updated_customers))

def reset_password(account_number, new_password):
    customers = read_from_file(CUSTOMER_FILE)
    updated_customers = []
    for customer in customers:
        customer_data = parse_customer_data(customer)
        if 'Account Number' in customer_data and customer_data['Account Number'] == account_number:
            customer_data['Password'] = new_password
        updated_customer = ', '.join([f"{key}: {value}" for key, value in customer_data.items()])
        updated_customers.append(updated_customer)
    with open(CUSTOMER_FILE, 'w') as file:
        file.write('\n'.join(updated_customers))
    print("Password reset successful.")


