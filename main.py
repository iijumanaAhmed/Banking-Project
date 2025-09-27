# in the .csv file, column 'active_status' is added for later usage when dealing with overdraft protection rules
import bank.account_exceptions as accountExp
import bank.customer_exceptions as customerExp
from bank.bank import Bank
from bank.customer import Customer
from bank.account import Account


def bank_system():
    create_account = Account()
    customer = Customer()
    bank_customers = Bank()
    bank_customers.retrieve_customers() 
    
    while True:            
        customer_action = int(input('\n🏦 | Welcome to the Bank Management System.\n1️⃣  Register\n2️⃣  Login \n3️⃣  Exit\nPlease enter the number of the action you want to preform: '))
        match customer_action:
            case 1:
                while True:
                    try:
                        customer.customer_id = customer.generate_id(customer.customer_id)
                    
                        fname = input('First name: ')
                        if fname.isalpha():
                            customer.fname = fname
                        else:
                            raise customerExp.AddCustomerError('Enter your first name with letters only')
                        
                        lname = input('Last name: ')
                        if lname.isalpha():
                            customer.lname = lname
                        else:
                            raise customerExp.AddCustomerError('Enter your last name with letters only')
                        
                        customer.password = input('Password: ')
                        
                        while True:
                            try:
                                # George's comments: change to be none -> the customer has no account!!, 0 -> the account balance = 0
                                customer_accounts = input('\n[ACCOUNTS CREATION]\n1️⃣  Checking account\n2️⃣  Savings account\n3️⃣  Checking and Savings accounts\nEnter the number of which account type would you want to create: ')
                                match customer_accounts:
                                    case '1':
                                        try:
                                            checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                            if type(int(checking_balance)) == int:
                                                if int(checking_balance) >= 0:
                                                    customer.checking_balance = int(checking_balance)
                                                elif int(checking_balance) < 0:
                                                    raise accountExp.AccountCreationError('Can not initiate your checking account with neigative amount\n')
                                        except ValueError:
                                            raise accountExp.AccountCreationError('Enter 0 or a POSITIVE NUMBER')
                                        
                                    case '2':
                                        savings_balance = input('⌨️  | Enter the intial savings balance: ')
                                        try:
                                            savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                            if type(int(savings_balance)) == int:
                                                if int(savings_balance) >= 0:
                                                    customer.savings_balance = int(savings_balance)
                                                elif int(savings_balance) < 0:
                                                    raise accountExp.AccountCreationError('Can not initiate your savings account with neigative amount\n')
                                        except ValueError:
                                            raise accountExp.AccountCreationError('Enter 0 or a POSITIVE NUMBER')
                                        
                                    case '3':
                                        try:
                                            checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                            if type(int(checking_balance)) == int:
                                                if int(checking_balance) >= 0:
                                                    customer.checking_balance = int(checking_balance)
                                                    bank_customers.update_customers()
                                                elif int(checking_balance) < 0:
                                                    raise accountExp.AccountCreationError('Can not initiate your checking account with neigative amount\n')
                                        except ValueError:
                                            raise accountExp.AccountCreationError('Enter 0 or a POSITIVE NUMBER')
                                        
                                        savings_balance = input('⌨️  | Enter the intial savings balance: ')
                                        try:
                                            savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                            if type(int(savings_balance)) == int:
                                                if int(savings_balance) >= 0:
                                                    customer.savings_balance = int(savings_balance)
                                                elif int(savings_balance) < 0:
                                                    raise accountExp.AccountCreationError('Can not initiate your savings account with neigative amount\n')
                                        except ValueError:
                                            raise accountExp.AccountCreationError('Enter 0 or a POSITIVE NUMBER')
                                        
                                    case _:
                                        raise accountExp.AccountCreationError('Enter VALID OPTION')
                                break
                            except accountExp.AccountCreationError as e:
                                print(f'🚩 | AccountCreationError: {e}')
                                
                        # Add new customer
                        new_customer_list = [customer.customer_id, customer.fname, customer.lname, customer.password, customer.checking_balance, customer.savings_balance, customer.active_status, customer.overdraft_attempt]
                        
                        customer.add_customer(new_customer_list)
                        if customer.add_customer:
                            break
                            
                    except accountExp.AccountCreationError as e:
                        print(f'🚩 | AccountCreationError: {e}\n')
                        
                    except customerExp.AddCustomerError as e:
                        print(f'🚩 | AddCustomerError: {e}\n')
                        
            case 2:
                while True:
                    try:
                        print('\n[LOGIN PAGE]')
                        login_id = input('Customer ID: ')
                        login_password = input('Customer Password: ')
                        if customer.login_customer(login_id, login_password) == True:
                            while True:
                                try:
                                    account_operation = int(input('\n[ACCOUNTS OPERATIONS]\n1) Withdraw\n2) Deposit\n3) Transfer Between Accounts\n4) Transfer To Another Customer Account\n5) Logout\nEnter the number of which operation would you want to do, or 5 to logout: '))
                                    operation = Account()
                                    match account_operation:
                                        case 1:
                                            while True:
                                                try:
                                                    withdraw_operation = input('\n[WITHDRAW OPERATIONS]\n1️⃣  Checking account\n2️⃣  Savings account\n0️⃣  Go Back\nEnter the number of which account would you like to withdraw from, or 0 to go back: ')
                                                    operation.withdraw_operation(customer.logged_customer_id, withdraw_operation)
                                                    if int(withdraw_operation) == 0:
                                                        break
                                                except accountExp.WithdrawOptionError as e:
                                                    print(f'🚩 | WithdrawOptionError: {e}\n')
                                                    
                                        case 2:
                                            while True:
                                                try:
                                                    deposit_operation = input('\n[DEPOSIT OPERATIONS]\n1️⃣  Checking account\n2️⃣  Savings account\n0️⃣  Go Back\nEnter the number of which account would you like to deposit into, or 0 to go back: ')
                                                    operation.deposit_operation(customer.logged_customer_id, deposit_operation)
                                                    if int(deposit_operation) == 0:
                                                        break
                                                except accountExp.DepositOptionError as e:
                                                    print(f'🚩 | DepositOptionError: {e}\n')
                                        case 3:
                                            transfer_to_account_operation = int(input('\n[TRANSFER BETWEEN ACCOUNTS OPERATIONS]\n1) From checking account to savings account\n2) From savings account to checking account\nEnter the number of which transfer would you like to preform: '))
                                            operation.transfer_between_accounts(customer.logged_customer_id, transfer_to_account_operation)
                                        case 4:
                                            transfer_to_customer_account_operation = int(input('\n[TRANSFER TO CUSTOMER ACCOUNT OPERATIONS]\n1) From checking account to other customer account\n2) From savings account to other customer account\nEnter the number of which transfer would you like to preform: '))
                                            operation.transfer_to_customer_account(customer.logged_customer_id, transfer_to_customer_account_operation)
                                        case 5:
                                            print('Back to the main menu')
                                            break
                                except customerExp.AddCustomerError as e:
                                    print(f'🚩 | AddCustomerError: {e}\n')
                        else: 
                            raise customerExp.LoginCustomerError(f'Customer ID or Password is wrong, Try again\n')
                        
                    except customerExp.LoginCustomerError as e:
                        print(f'🚩 | AddCustomerError: {e}\n')
            case 3:
                print('See you later 💵')
                return
        
if __name__ == '__main__':
    bank_system()