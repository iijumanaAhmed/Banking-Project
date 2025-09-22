# in the .csv file, column 'active_status' is added for later usage when dealing with overdraft protection rules
import csv, random
from bank.bank import Bank
from bank.customer import Customer
from bank.account import Account

def bank_system():
    bank_customers = Bank()
    bank_customers.retrieve_customers() 

    while True:
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
                new_customer = Customer()
                new_customer_list = [customer_id, customer_fname, customer_lname, customer_password, checking_account, savings_account, account_status] 
                new_customer.add_customer(new_customer_list)

            case 2:
                customer_login = Customer()
                if customer_login.login_customer() == True:
                    # customer_login.account_transaction()
                    account_operation = int(input('\n[ACCOUNTS OPERATIONS]\n1) Withdraw\n2) Deposit\n3) Transfer\n4) Logout\nEnter the number of which operation would you want to do, or 4 to logout: '))
                    operation = Account()
                    match account_operation:
                        case 1:
                            withdraw_operation = int(input('[WITHDRAW OPERATIONS]\n1) Checking account\n2) Savings account\nEnter the number of which account would you like to withdraw from: '))
                            match withdraw_operation:
                                case 1:
                                    operation.withdraw_checking(customer_login.logged_customer_id)

                                case 2:
                                    operation.withdraw_savings(customer_login.logged_customer_id)

                        # case 2:
                        #     deposit_operation = int(input('[DEPOSIT OPERATIONS]\n1) Checking account\n2) Savings account\nEnter the number of which account would you like to deposit into: '))
                        #     match deposit_operation:
                        #         case 1:
                        #             operation.deposit_checking(customer_login.logged_customer_id)

                        #         case 2:
                        #             operation.deposit_savings(customer_login.logged_customer_id)
                        # case 3:

                        case 4:
                            print('Back to the main menu')
                            
            case 3:
                print('See you later 💵')
                return

if __name__ == '__main__':
    bank_system()