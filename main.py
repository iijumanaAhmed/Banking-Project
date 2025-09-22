# in the .csv file, column 'active_status' is added for later usage when dealing with overdraft protection rules
import csv, random
from bank.bank import Bank
from bank.customer import Customer

def bank_system():
    bank_customers = Bank()
    bank_customers.retrive_customers() 

    customer_action = int(input('🏦 | Welcome to the Bank Management System.\n\n1) Register\n2) Login \n3) Exit\nPlease enter the number of the action you want to preform: '))
    match customer_action:
        case 1:
            id_unique = False
            while id_unique == False:
                random_id = str(random.randint(10000, 11000))
                with open('bank.csv', 'r', newline='') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        if random_id == row[0]:
                            id_unique = False
                            break
                        else:
                            id_unique = True
                if id_unique:
                    customer_id = random_id
                    print(f'New customer ID: {customer_id}')
                    break

            customer_fname = input('First name: ')
            customer_lname = input('Last name: ')
            customer_password = input('Password: ')

            # George's comments: change to be none -> the customer has no account!!, 0 -> the account balance = 0
            checking_account = None
            savings_account = None
            customer_accounts = int(input('\n[ACCOUNTS CREATION]\n1) Checking account\n2) Savings account\n3) Checking and Savings accounts\nEnter the number of which account type would you want to create: '))
            match customer_accounts:
                case 1:
                    checking_account = int(input('Enter the intial checking balance: '))
                case 2:
                    savings_account = int(input('Enter the intial savings balance: '))
                case 3:
                    checking_account = int(input('Enter the intial checking balance: '))
                    savings_account = int(input('Enter the intial savings balance: '))

            account_status = 'active'

            # Add new customer
            new_customer_list = [customer_id, customer_fname, customer_lname, customer_password, checking_account, savings_account, account_status] 
            bank_customers.updated_customers(new_customer_list)

if __name__ == '__main__':
    bank_system()