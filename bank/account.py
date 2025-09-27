import csv
import bank.account_exceptions as accountExp
from bank.bank import Bank

class Account():
    def __init__(self):
        self.logged_customer = False

    # method holds the withdraw operations on both checking and savings accounts
    def withdraw_operation(self, customer_id, account_option):
        operation_completed = False
        while operation_completed != True:
            try:
                if account_option.isdigit() and (int(account_option) <= 2 and int(account_option) >= 0):
                    if int(account_option) == 1:
                        withdraw_completed = False
                        operation_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[WITHDRAW CHECKING]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][4] != '':
                                                while True:
                                                    try:
                                                        print(f'💲 | Your Checking Balance: {bank_customers.customers[row_index][4]}')
                                                        checking_amount = input('💳 | Checking Amount: ')
                                                        if int(bank_customers.customers[row_index][4]) >= 0 and (int(bank_customers.customers[row_index][4]) - int(checking_amount) >= 0):
                                                            if type(int(checking_amount)) == int:
                                                                if int(checking_amount) > 0:
                                                                    old_checking_balance = int(bank_customers.customers[row_index][4])
                                                                    bank_customers.customers[row_index][4] = old_checking_balance - int(checking_amount)
                                                                    bank_customers.update_customers()
                                                                    print(f'🔴 | The old checking balance = {old_checking_balance}\n📉 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                                    withdraw_completed = True
                                                                    operation_completed = True
                                                                    break
                                                                elif int(checking_amount) <= 0:
                                                                    operation_completed = True
                                                                    raise accountExp.WithdrawOperationError('Can not withdraw zero or neigative amount')
                                                            else:
                                                                operation_completed = True
                                                                raise ValueError
                                                        else:
                                                            if type(int(checking_amount)) == int:
                                                                if int(checking_amount) <= 100 and int(checking_amount) > 0:
                                                                    bank_customers.overdraft_protection_fee(customer_id, checking_amount)
                                                                    withdraw_completed = True
                                                                    operation_completed = True                                                            
                                                                    break
                                                                elif int(checking_amount) > 100:
                                                                    operation_completed = True
                                                                    raise accountExp.WithdrawOperationError(f'You tried to withdraw {checking_amount}. As your checking balance is {bank_customers.customers[row_index][4]}, you are not allowed to withdraw more than 100')
                                                                elif int(checking_amount) <= 0:
                                                                    operation_completed = True
                                                                    raise accountExp.WithdrawOperationError('Can not withdraw zero or neigative amount')
                                                            else:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.WithdrawOperationError('Please enter a positive withdrawal amount')
                                            else:
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                                                    if type(int(checking_balance)) == int:
                                                                        if int(checking_balance) >= 0:
                                                                            bank_customers.customers[row_index][4] = int(checking_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                                            withdraw_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(checking_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.WithdrawOperationError('Can not initiate your checking account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.WithdrawOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your checking account still not created\n')
                                                                withdraw_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.WithdrawOperationError('Enter a YES or NO only')
                                        else:
                                            try:
                                                print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                                reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                                match reactivate:
                                                    case 'yes':
                                                        print(f'\n💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                        charge_amount = int(input('💳 | Charge Amount: '))
                                                        aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                        if aprroved_balance < 0:
                                                            operation_completed = True
                                                            raise accountExp.WithdrawOperationError(f'This {charge_amount} can not reactivate your account')
                                                        else:
                                                            bank_customers.activate_customer(customer_id, charge_amount)
                                                            withdraw_completed = True
                                                            operation_completed = True
                                                    case 'no':
                                                        withdraw_completed = True
                                                        operation_completed = True
                                                        raise accountExp.WithdrawAlert('Your account remain DEACTIVE')
                                                    case _:
                                                        operation_completed = True
                                                        raise ValueError
                                            except ValueError:
                                                raise accountExp.WithdrawOperationError('Enter a YES or NO only')
                                            except accountExp.WithdrawAlert as e:
                                                print(f'💰 | WithdrawAlert: {e}\n')
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if withdraw_completed:
                                    break
                        if operation_completed == True:
                            break
                    elif int(account_option) == 2:
                        withdraw_completed = False
                        operation_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[WITHDRAW SAVINGS]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][5] != '':
                                                while True:
                                                    try:
                                                        print(f'💲 | Your Savings Balance: {bank_customers.customers[row_index][5]}')
                                                        savings_amount = input('💳 | Savings Amount: ')
                                                        if int(bank_customers.customers[row_index][5]) >= 0  and (int(bank_customers.customers[row_index][5]) - int(savings_amount) >= 0):
                                                            if type(int(savings_amount)) == int:
                                                                if int(savings_amount) > 0:
                                                                    old_savings_balance = int(bank_customers.customers[row_index][5])
                                                                    bank_customers.customers[row_index][5] = old_savings_balance - int(savings_amount)
                                                                    bank_customers.update_customers()
                                                                    print(f'🔴 | The old savings balance = {old_savings_balance}\n📉 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                                    withdraw_completed = True
                                                                    operation_completed = True
                                                                    break
                                                                elif int(savings_amount) <= 0:
                                                                    operation_completed = True
                                                                    raise accountExp.WithdrawOperationError('Can not withdraw zero or neigative amount')
                                                            else:
                                                                operation_completed = True
                                                                raise ValueError
                                                        elif (int(bank_customers.customers[row_index][5]) - int(savings_amount) < 0):
                                                            operation_completed = True
                                                            raise accountExp.WithdrawOperationError(f'Can not withdraw amount more than the savings balance {bank_customers.customers[row_index][5]}')
                                                        elif int(bank_customers.customers[row_index][5]) == 0:
                                                            operation_completed = True
                                                            raise accountExp.WithdrawOperationError(f'Can not withdraw any amount as the savings balance is {bank_customers.customers[row_index][5]}')
                                                        else:
                                                            operation_completed = True
                                                            raise ValueError
                                                    except ValueError:
                                                        raise accountExp.WithdrawOperationError('Please enter a positive withdrawal amount')
                                            else:
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                                                    if type(int(savings_balance)) == int:
                                                                        if int(savings_balance) >= 0:
                                                                            bank_customers.customers[row_index][5] = int(savings_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                                            withdraw_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(savings_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.WithdrawOperationError('Can not initiate your savings account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.WithdrawOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your savings account still not created\n')
                                                                withdraw_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.WithdrawOperationError('Enter a YES or NO only')
                                        else:
                                            try:
                                                print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                                reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                                match reactivate:
                                                    case 'yes':
                                                        print(f'\n💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                        charge_amount = int(input('💳 | Charge Amount: '))
                                                        aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                        if aprroved_balance < 0:
                                                            operation_completed = True
                                                            raise accountExp.WithdrawOperationError(f'This {charge_amount} can not reactivate your account')
                                                        else:
                                                            bank_customers.activate_customer(customer_id, charge_amount)
                                                            withdraw_completed = True
                                                            operation_completed = True
                                                    case 'no':
                                                        withdraw_completed = True
                                                        operation_completed = True
                                                        raise accountExp.WithdrawAlert('Your account remain DEACTIVE')
                                                    case _:
                                                        operation_completed = True
                                                        raise ValueError
                                            except ValueError:
                                                raise accountExp.WithdrawOperationError('Enter a YES or NO only')
                                            except accountExp.WithdrawAlert as e:
                                                print(f'💰 | WithdrawAlert: {e}\n')
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if withdraw_completed:
                                    break
                        if operation_completed == True:
                            break
                    elif int(account_option) == 0:
                        break
                    
                elif not account_option.isdigit():
                    raise accountExp.WithdrawOptionError('Enter a VALID operation option')
                elif account_option.isdigit() and (int(account_option) > 2 or int(account_option) < 0):
                    raise accountExp.WithdrawOptionError('Enter a VALID operation option')
                break                
            
            except accountExp.WithdrawOperationError as e:
                print(f'🚩 | WithdrawOperationError: {e}\n')
            except FileNotFoundError:
                raise accountExp.WithdrawOperationError(f'The file {bank_customers.file_name} Not found')

    # method holds the deposit operations on both checking and savings accounts
    def deposit_operation(self, customer_id, account_option):
        operation_completed = False
        while operation_completed != True:
            try:
                if account_option.isdigit() and (int(account_option) <= 2 and int(account_option) >= 0):
                    if int(account_option) == 1:
                        deposit_completed = False
                        operation_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[DEPOSIT CHECKING]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][4] != '':
                                                while True:
                                                    try:
                                                        checking_deposit = input('💳 | Deposit Amount Into Checking: ')
                                                        if type(int(checking_deposit)) == int:
                                                            if int(checking_deposit) > 0:
                                                                old_checking_balance = int(bank_customers.customers[row_index][4])
                                                                bank_customers.customers[row_index][4] = old_checking_balance + int(checking_deposit)
                                                                bank_customers.update_customers()
                                                                print(f'🔵 | The old checking balance = {old_checking_balance}\n📈 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                                deposit_completed = True
                                                                operation_completed = True
                                                                break
                                                            
                                                            elif int(checking_deposit) <= 0:
                                                                operation_completed = True
                                                                raise accountExp.DepositOperationError('Can not deposit zero or neigative amount')
                                                        else:
                                                            operation_completed = True
                                                            raise ValueError
                                                    except ValueError:
                                                        raise accountExp.DepositOperationError('Please enter a positive deposit amount')

                                            else:
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                                                    if type(int(checking_balance)) == int:
                                                                        if int(checking_balance) >= 0:
                                                                            bank_customers.customers[row_index][4] = int(checking_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                                            deposit_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(checking_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.DepositOperationError('Can not initiate your checking account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.DepositOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your checking account still not created\n')
                                                                deposit_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.DepositOperationError('Enter a YES or NO only')
    
                                        else:
                                            try:
                                                print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                                reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                                match reactivate:
                                                    case 'yes':
                                                        print(f'\n💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                        charge_amount = int(input('💳 | Charge Amount: '))
                                                        aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                        if aprroved_balance < 0:
                                                            operation_completed = True
                                                            raise accountExp.DepositOperationError(f'This {charge_amount} can not reactivate your account')
                                                        else:
                                                            bank_customers.activate_customer(customer_id, charge_amount)
                                                            deposit_completed = True
                                                            operation_completed = True
                                                    case 'no':
                                                        deposit_completed = True
                                                        operation_completed = True
                                                        raise accountExp.DepositAlert('Your account remain DEACTIVE')
                                                    case _:
                                                        operation_completed = True
                                                        raise ValueError
                                            except ValueError:
                                                raise accountExp.DepositOperationError('Enter a YES or NO only')
                                            except accountExp.DepositAlert as e:
                                                print(f'💰 | DepositAlert: {e}\n')
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if deposit_completed:
                                    break
                        if operation_completed == True:
                            break

                    if int(account_option) == 2:
                        deposit_completed = False
                        operation_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[DEPOSIT SAVINGS]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][5] != '':
                                                while True:
                                                    try:
                                                        savings_deposit = input('💳 | Deposit Amount Into Savings: ')
                                                        if type(int(savings_deposit)) == int:
                                                            if int(savings_deposit) > 0:
                                                                old_savings_balance = int(bank_customers.customers[row_index][5])
                                                                bank_customers.customers[row_index][5] = old_savings_balance + int(savings_deposit)
                                                                bank_customers.update_customers()
                                                                print(f'🔵 | The old savings balance = {old_savings_balance}\n📈 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                                deposit_completed = True
                                                                operation_completed = True
                                                                break
                                                            
                                                            elif int(savings_deposit) <= 0:
                                                                operation_completed = True
                                                                raise accountExp.DepositOperationError('Can not deposit zero or neigative amount')
                                                        else:
                                                            operation_completed = True
                                                            raise ValueError
                                                    except ValueError:
                                                        raise accountExp.DepositOperationError('Please enter a positive deposit amount')

                                            else:
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                                        account_creation = input('❓ | Do you want to create a savings account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                                                    if type(int(savings_balance)) == int:
                                                                        if int(savings_balance) >= 0:
                                                                            bank_customers.customers[row_index][5] = int(savings_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                                            deposit_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(savings_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.DepositOperationError('Can not initiate your savings account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.DepositOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your savings account still not created\n')
                                                                deposit_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.DepositOperationError('Enter a YES or NO only')

                                        else:
                                            try:
                                                print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                                reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                                match reactivate:
                                                    case 'yes':
                                                        print(f'\n💲 | Your savings Balance : {bank_customers.customers[row_index][4]}')
                                                        charge_amount = int(input('💳 | Charge Amount: '))
                                                        aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                        if aprroved_balance < 0:
                                                            operation_completed = True
                                                            raise accountExp.DepositOperationError(f'This {charge_amount} can not reactivate your account')
                                                        else:
                                                            bank_customers.activate_customer(customer_id, charge_amount)
                                                            deposit_completed = True
                                                            operation_completed = True
                                                    case 'no':
                                                        deposit_completed = True
                                                        operation_completed = True
                                                        raise accountExp.DepositAlert('Your account remain DEACTIVE')
                                                    case _:
                                                        operation_completed = True
                                                        raise ValueError
                                            except ValueError:
                                                raise accountExp.DepositOperationError('Enter a YES or NO only')
                                            except accountExp.DepositAlert as e:
                                                print(f'💰 | DepositAlert: {e}\n')
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if deposit_completed:
                                    break
                        if operation_completed == True:
                            break

                    elif int(account_option) == 0:
                        break

                elif not account_option.isdigit():
                    raise accountExp.DepositOptionError('Enter a VALID operation option')
                elif account_option.isdigit() and (int(account_option) > 2 or int(account_option) < 0):
                    raise accountExp.DepositOptionError('Enter a VALID operation option')
                break                
            
            except accountExp.DepositOperationError as e:
                print(f'🚩 | DepositOperationError: {e}\n')
            except FileNotFoundError:
                raise accountExp.DepositOperationError(f'The file {bank_customers.file_name} Not found')

    # method holds the transfer operations between checking and savings accounts of the same customer
    def transfer_between_accounts_operation(self, customer_id, account_option):
        operation_completed = False
        while operation_completed != True:
            try:
                if account_option.isdigit() and (int(account_option) <= 2 and int(account_option) >= 0):
                    if int(account_option) == 1:
                        transfer_between_accounts_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[TRANSFER FROM CHECKING TO SAVINGS]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][4] != '' and bank_customers.customers[row_index][5] != '':
                                                while True:
                                                    try:
                                                        if int(bank_customers.customers[row_index][4]) == 0:
                                                            transfer_between_accounts_completed = True
                                                            operation_completed = True
                                                            print(f'‼️  | Can\'t transfer from checking to savings account as the checking account balance is {bank_customers.customers[row_index][4]}')
                                                            break
                                                        else:
                                                            transfer_amount = input('🔁 | Transfer Amount From Checking To Savings: ')
                                                            if int(bank_customers.customers[row_index][4]) > 0:
                                                                if type(int(transfer_amount)) == int:
                                                                    if int(transfer_amount) > 0 and int(transfer_amount) <= int(bank_customers.customers[row_index][4]):
                                                                        old_checking_balance = int(bank_customers.customers[row_index][4])
                                                                        bank_customers.customers[row_index][4] = old_checking_balance - int(transfer_amount)
                                                                        old_savings_balance = int(bank_customers.customers[row_index][5])
                                                                        bank_customers.customers[row_index][5] = old_savings_balance + int(transfer_amount)
                                                                        
                                                                        bank_customers.update_customers()
                                                                        print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                                        print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                                        transfer_between_accounts_completed = True
                                                                        operation_completed = True
                                                                        break
                                                                    elif int(transfer_amount) > 0 and int(transfer_amount) > int(bank_customers.customers[row_index][4]):
                                                                        operation_completed = True
                                                                        raise accountExp.TransferBetweenAccountsOperationError(f'Can\'t transfer {transfer_amount} from checking to savings account as it exceed the checking account balance')
                                                                    elif int(transfer_amount) <= 0:
                                                                        operation_completed = True
                                                                        raise accountExp.TransferBetweenAccountsOperationError('Can not transfer zero or neigative amount')
                                                                else:
                                                                    operation_completed = True
                                                                    raise ValueError
                                                            else:
                                                                operation_completed = True
                                                                raise accountExp.TransferBetweenAccountsOperationError(f'Can\'t preform the transfer operation from checking to savings account as the checking account balance is {bank_customers.customers[row_index][4]}')
                                                            
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Please enter a positive transfer amount')                                                    

                                            elif bank_customers.customers[row_index][4] == '':
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                                                    if type(int(checking_balance)) == int:
                                                                        if int(checking_balance) >= 0:
                                                                            bank_customers.customers[row_index][4] = int(checking_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                                            transfer_between_accounts_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(checking_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.TransferBetweenAccountsOperationError('Can not initiate your checking account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.TransferBetweenAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your checking account still not created\n')
                                                                transfer_between_accounts_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Enter a YES or NO only')

                                            elif bank_customers.customers[row_index][5] == '':
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                                        account_creation = input('❓ | Do you want to create a savings account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                                                    if type(int(savings_balance)) == int:
                                                                        if int(savings_balance) >= 0:
                                                                            bank_customers.customers[row_index][5] = int(savings_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                                            transfer_between_accounts_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(savings_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.TransferBetweenAccountsOperationError('Can not initiate your savings account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.TransferBetweenAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your savings account still not created\n')
                                                                transfer_between_accounts_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Enter a YES or NO only')

                                            else:
                                                operation_completed = True
                                                raise accountExp.TransferBetweenAccountsOperationError(f'‼️  | The customer with id {customer_id} don\'t have both checking and savings accounts')

                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if transfer_between_accounts_completed:
                                    break
                        if operation_completed == True:
                            break
                        
                    if int(account_option) == 2:
                        transfer_between_accounts_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)
                                row_index = 1
                                print('\n[TRANSFER FROM SAVINGS TO CHECKING]')
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            if bank_customers.customers[row_index][4] != '' and bank_customers.customers[row_index][5] != '':
                                                while True:
                                                    try:
                                                        if int(bank_customers.customers[row_index][5]) == 0:
                                                            transfer_between_accounts_completed = True
                                                            operation_completed = True
                                                            print(f'‼️  | Can\'t transfer from savings to checking account as the savings account balance is {bank_customers.customers[row_index][5]}')
                                                            break
                                                        else:
                                                            transfer_amount = input('🔁 | Transfer Amount From Savings To Checking: ')
                                                            if int(bank_customers.customers[row_index][5]) > 0:
                                                                if type(int(transfer_amount)) == int:
                                                                    if int(transfer_amount) > 0 and int(transfer_amount) <= int(bank_customers.customers[row_index][5]):
                                                                        old_checking_balance = int(bank_customers.customers[row_index][4])
                                                                        bank_customers.customers[row_index][4] = old_checking_balance + int(transfer_amount)
                                                                        old_savings_balance = int(bank_customers.customers[row_index][5])
                                                                        bank_customers.customers[row_index][5] = old_savings_balance - int(transfer_amount)
                                                                        
                                                                        bank_customers.update_customers()
                                                                        print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                                        print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                                        transfer_between_accounts_completed = True
                                                                        operation_completed = True
                                                                        break
                                                                    elif int(transfer_amount) > 0 and int(transfer_amount) > int(bank_customers.customers[row_index][5]):
                                                                        operation_completed = True
                                                                        raise accountExp.TransferBetweenAccountsOperationError(f'Can\'t transfer {transfer_amount} from savings to checking account as it exceed the savings account balance')
                                                                    elif int(transfer_amount) <= 0:
                                                                        operation_completed = True
                                                                        raise accountExp.TransferBetweenAccountsOperationError('Can not transfer zero or neigative amount')
                                                                else:
                                                                    operation_completed = True
                                                                    raise ValueError
                                                            else:
                                                                operation_completed = True
                                                                raise accountExp.TransferBetweenAccountsOperationError(f'Can\'t preform the transfer operation from savings to checking account as the savings account balance is {bank_customers.customers[row_index][5]}')
                                                            
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Please enter a positive transfer amount')                                                    

                                            elif bank_customers.customers[row_index][4] == '':
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                                                    if type(int(checking_balance)) == int:
                                                                        if int(checking_balance) >= 0:
                                                                            bank_customers.customers[row_index][4] = int(checking_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                                            transfer_between_accounts_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(checking_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.TransferBetweenAccountsOperationError('Can not initiate your checking account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.TransferBetweenAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your checking account still not created\n')
                                                                transfer_between_accounts_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Enter a YES or NO only')

                                            elif bank_customers.customers[row_index][5] == '':
                                                while True:
                                                    try:
                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                                        account_creation = input('❓ | Do you want to create a savings account (yes/no): ').lower()
                                                        match account_creation:
                                                            case 'yes':
                                                                try:
                                                                    savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                                                    if type(int(savings_balance)) == int:
                                                                        if int(savings_balance) >= 0:
                                                                            bank_customers.customers[row_index][5] = int(savings_balance)
                                                                            bank_customers.update_customers()
                                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                                            transfer_between_accounts_completed = True
                                                                            operation_completed = True
                                                                            break
                                                                        elif int(savings_balance) < 0:
                                                                            operation_completed = True
                                                                            raise accountExp.TransferBetweenAccountsOperationError('Can not initiate your savings account with neigative amount\n')
                                                                except ValueError:
                                                                    raise accountExp.TransferBetweenAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                            case 'no':
                                                                print('💰 | Your savings account still not created\n')
                                                                transfer_between_accounts_completed = True
                                                                operation_completed = True
                                                                break
                                                            case _:
                                                                operation_completed = True
                                                                raise ValueError
                                                    except ValueError:
                                                        raise accountExp.TransferBetweenAccountsOperationError('Enter a YES or NO only')

                                            else:
                                                operation_completed = True
                                                raise accountExp.TransferBetweenAccountsOperationError(f'‼️  | The customer with id {customer_id} don\'t have both checking and savings accounts')

                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if transfer_between_accounts_completed:
                                    break
                        if operation_completed == True:
                            break
                    elif int(account_option) == 0:
                        break

                elif not account_option.isdigit():
                    raise accountExp.TransferBetweenAccountsOptionError('Enter a VALID operation option')
                elif account_option.isdigit() and (int(account_option) > 2 or int(account_option) < 0):
                    raise accountExp.TransferBetweenAccountsOptionError('Enter a VALID operation option')
                break                
            
            except accountExp.TransferBetweenAccountsOperationError as e:
                print(f'🚩 | TransferBetweenAccountsOperationError: {e}\n')
            except FileNotFoundError:
                raise accountExp.TransferBetweenAccountsOperationError(f'The file {bank_customers.file_name} Not found')

    # method holds the transfer operations between customers accounts
    def transfer_to_customer_account_operation(self, customer_id, account_option):
        operation_completed = False
        while operation_completed != True:
            try:
                if account_option.isdigit() and (int(account_option) <= 2 and int(account_option) >= 0):
                    if int(account_option) == 1:
                        transfer_to_customer_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            print('[TRANSFER FROM CHECKING TO CUSTOMER\'S ACCOUNT]\n')
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)                            
                                row_index = 1
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            while True:
                                                try:
                                                    other_customer_id = input('⌨️  | Enter the customer\'s account id you want to transfer to: ')
                                                    other_customer_row_index = 0
                                                    other_customer_found = False
                                                    if other_customer_id == customer_id:
                                                        operation_completed = True
                                                        raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id: {other_customer_id} is the current customer')

                                                    else:
                                                        with open(bank_customers.file_name, 'r', newline='') as file:
                                                            reader = csv.reader(file)
                                                            next(reader)
                                                            index = 1
                                                            for row in reader:
                                                                if other_customer_id == row[0]:
                                                                    other_customer_found = True
                                                                    other_customer_row_index = index
                                                                    break
                                                                index += 1
                                                            
                                                        if other_customer_found:
                                                            if bank_customers.customers[row_index][4] != '' and bank_customers.customers[other_customer_row_index][4] != '':
                                                                if int(bank_customers.customers[row_index][4]) == 0:
                                                                    transfer_to_customer_completed = True
                                                                    operation_completed = True
                                                                    raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t transfer from checking to the customer account with id {other_customer_id} as the checking account balance is {bank_customers.customers[row_index][4]}')

                                                                else:
                                                                    transfer_amount = input('🔁 | Transfer Amount From Checking To Customer\'s Account: ')
                                                                    if int(bank_customers.customers[row_index][4]) > 0:
                                                                        if type(int(transfer_amount)) == int:
                                                                            if int(transfer_amount) > 0 and int(transfer_amount) <= int(bank_customers.customers[row_index][4]):
                                                                                old_checking_balance = int(bank_customers.customers[row_index][4])
                                                                                bank_customers.customers[row_index][4] = old_checking_balance - int(transfer_amount)
                                                                                other_customer_balance = int(bank_customers.customers[other_customer_row_index][4])
                                                                                bank_customers.customers[other_customer_row_index][4] = other_customer_balance + int(transfer_amount)                                                                                        

                                                                                bank_customers.update_customers()
                                                                                print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                                                print(f'🔶 | The old other customer balance = {other_customer_balance}\n🔷 | The new  other customer balance = {bank_customers.customers[other_customer_row_index][4]}\n')
                                                                                operation_completed = True
                                                                                transfer_to_customer_completed = True
                                                                                break                                                                                        
                                                                            elif int(transfer_amount) > 0 and int(transfer_amount) > int(bank_customers.customers[row_index][4]):
                                                                                operation_completed = True
                                                                                raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t transfer {transfer_amount} from checking to the customer account with id {other_customer_id} as it exceed the checking account balance')
                                                                            elif int(transfer_amount) <= 0:
                                                                                operation_completed = True
                                                                                raise accountExp.TransferToCustomerAccountsOperationError('Can not transfer zero or neigative amount')
                                                                        else:
                                                                            operation_completed = True
                                                                            raise ValueError
                                                                    else:
                                                                        operation_completed = True
                                                                        raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t preform the transfer operation from checking to the customer account with id {other_customer_id} as the checking account balance is {bank_customers.customers[row_index][4]}')
                                                            
                                                            elif bank_customers.customers[row_index][4] == '':
                                                                while True:
                                                                    try:
                                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                                                        account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                                                        match account_creation:
                                                                            case 'yes':
                                                                                try:
                                                                                    checking_balance = input('\n⌨️  | Enter the intial checking balance: ')
                                                                                    if type(int(checking_balance)) == int:
                                                                                        if int(checking_balance) >= 0:
                                                                                            bank_customers.customers[row_index][4] = int(checking_balance)
                                                                                            bank_customers.update_customers()
                                                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                                                            transfer_to_customer_completed = True
                                                                                            operation_completed = True
                                                                                            break
                                                                                        elif int(checking_balance) < 0:
                                                                                            operation_completed = True
                                                                                            raise accountExp.TransferToCustomerAccountsOperationError('Can not initiate your checking account with neigative amount\n')
                                                                                except ValueError:
                                                                                    raise accountExp.TransferToCustomerAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                                            case 'no':
                                                                                print('💰 | Your checking account still not created\n')
                                                                                transfer_to_customer_completed = True
                                                                                operation_completed = True
                                                                                break
                                                                            case _:
                                                                                operation_completed = True
                                                                                raise ValueError
                                                                    except ValueError:
                                                                        raise accountExp.TransferToCustomerAccountsOperationError('Enter a YES or NO only')

                                                            elif bank_customers.customers[other_customer_row_index][4] == '':
                                                                operation_completed = True
                                                                raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id {other_customer_id} don\'t have checking account')

                                                        else:
                                                            operation_completed = True
                                                            raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id {other_customer_id} doesn\'t exist')
                                                        
                                                except ValueError:
                                                    raise accountExp.TransferToCustomerAccountsOperationError('Please enter a positive transfer amount')                                                    
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if transfer_to_customer_completed:
                                    break
                        if operation_completed == True:
                            break

                    elif int(account_option) == 2:
                        transfer_to_customer_completed = False
                        while True:
                            bank_customers = Bank()
                            bank_customers.retrieve_customers()
                            print('[TRANSFER FROM SAVINGS TO CUSTOMER\'S ACCOUNT]\n')
                            with open(bank_customers.file_name, 'r', newline='') as file:
                                reader = csv.reader(file)
                                next(reader)                            
                                row_index = 1
                                for row in reader:
                                    if customer_id == row[0]:
                                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                            while True:
                                                try:
                                                    other_customer_id = input('⌨️  | Enter the customer\'s account id you want to transfer to: ')
                                                    other_customer_row_index = 0
                                                    other_customer_found = False
                                                    if other_customer_id == customer_id:
                                                        operation_completed = True
                                                        raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id: {other_customer_id} is the current customer')

                                                    else:
                                                        with open(bank_customers.file_name, 'r', newline='') as file:
                                                            reader = csv.reader(file)
                                                            next(reader)
                                                            index = 1
                                                            for row in reader:
                                                                if other_customer_id == row[0]:
                                                                    other_customer_found = True
                                                                    other_customer_row_index = index
                                                                    break
                                                                index += 1
                                                            
                                                        if other_customer_found:
                                                            if bank_customers.customers[row_index][5] != '' and bank_customers.customers[other_customer_row_index][4] != '':
                                                                if int(bank_customers.customers[row_index][5]) == 0:
                                                                    transfer_to_customer_completed = True
                                                                    operation_completed = True
                                                                    raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t transfer from checking to the customer account with id {other_customer_id} as the checking account balance is {bank_customers.customers[row_index][5]}')

                                                                else:
                                                                    transfer_amount = input('🔁 | Transfer Amount From Savings To Customer\'s Account: ')
                                                                    if int(bank_customers.customers[row_index][5]) > 0:
                                                                        if type(int(transfer_amount)) == int:
                                                                            if int(transfer_amount) > 0 and int(transfer_amount) <= int(bank_customers.customers[row_index][5]):
                                                                                old_savings_balance = int(bank_customers.customers[row_index][5])
                                                                                bank_customers.customers[row_index][5] = old_savings_balance - int(transfer_amount)
                                                                                other_customer_balance = int(bank_customers.customers[other_customer_row_index][4])
                                                                                bank_customers.customers[other_customer_row_index][4] = other_customer_balance + int(transfer_amount)                                                                                        

                                                                                bank_customers.update_customers()
                                                                                print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                                                print(f'🔶 | The old other customer balance = {other_customer_balance}\n🔷 | The new  other customer balance = {bank_customers.customers[other_customer_row_index][4]}\n')
                                                                                operation_completed = True
                                                                                transfer_to_customer_completed = True
                                                                                break                                                                                        
                                                                            elif int(transfer_amount) > 0 and int(transfer_amount) > int(bank_customers.customers[row_index][5]):
                                                                                operation_completed = True
                                                                                raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t transfer {transfer_amount} from savings to the customer account with id {bank_customers.customers[other_customer_row_index][0]} as it exceed the savings account balance')
                                                                            elif int(transfer_amount) <= 0:
                                                                                operation_completed = True
                                                                                raise accountExp.TransferToCustomerAccountsOperationError('Can not transfer zero or neigative amount')
                                                                        else:
                                                                            operation_completed = True
                                                                            raise ValueError
                                                                    else:
                                                                        operation_completed = True
                                                                        raise accountExp.TransferToCustomerAccountsOperationError(f'Can\'t preform the transfer operation from checking to the customer account with id {other_customer_id} as the checking account balance is {bank_customers.customers[row_index][5]}')
                                                                        
                                                            elif bank_customers.customers[row_index][5] == '':
                                                                while True:
                                                                    try:
                                                                        print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                                                        account_creation = input('❓ | Do you want to create a savings account (yes/no): ').lower()
                                                                        match account_creation:
                                                                            case 'yes':
                                                                                try:
                                                                                    savings_balance = input('\n⌨️  | Enter the intial savings balance: ')
                                                                                    if type(int(savings_balance)) == int:
                                                                                        if int(savings_balance) >= 0:
                                                                                            bank_customers.customers[row_index][5] = int(savings_balance)
                                                                                            bank_customers.update_customers()
                                                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                                                            transfer_to_customer_completed = True
                                                                                            operation_completed = True
                                                                                            break
                                                                                        elif int(savings_balance) < 0:
                                                                                            operation_completed = True
                                                                                            raise accountExp.TransferToCustomerAccountsOperationError('Can not initiate your savings account with neigative amount\n')
                                                                                except ValueError:
                                                                                    raise accountExp.TransferToCustomerAccountsOperationError('Enter 0 or a POSITIVE NUMBER')
                                                                            case 'no':
                                                                                print('💰 | Your savings account still not created\n')
                                                                                transfer_to_customer_completed = True
                                                                                operation_completed = True
                                                                                break
                                                                            case _:
                                                                                operation_completed = True
                                                                                raise ValueError
                                                                    except ValueError:
                                                                        raise accountExp.TransferToCustomerAccountsOperationError('Enter a YES or NO only')

                                                            elif bank_customers.customers[other_customer_row_index][4] == '':
                                                                operation_completed = True
                                                                raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id {other_customer_id} don\'t have checking account')

                                                        else:
                                                            operation_completed = True
                                                            raise accountExp.TransferToCustomerAccountsOperationError(f'The customer with id {other_customer_id} doesn\'t exist')
                                                except ValueError:
                                                    raise accountExp.TransferToCustomerAccountsOperationError('Please enter a positive transfer amount')
                                    
                                    row_index += 1
                                    if row_index == len(bank_customers.customers):
                                        break
                                if transfer_to_customer_completed:
                                    break
                        if operation_completed == True:
                            break

                    elif int(account_option) == 0:
                        break

                elif not account_option.isdigit():
                    raise accountExp.TransferToCustomerAccountsOptionError('Enter a VALID operation option')
                elif account_option.isdigit() and (int(account_option) > 2 or int(account_option) < 0):
                    raise accountExp.TransferToCustomerAccountsOptionError('Enter a VALID operation option')
                break                
            
            except accountExp.TransferToCustomerAccountsOperationError as e:
                print(f'🚩 | TransferToCustomerAccountsOperationError: {e}\n')
            except FileNotFoundError:
                raise accountExp.TransferToCustomerAccountsOperationError(f'The file {bank_customers.file_name} Not found')