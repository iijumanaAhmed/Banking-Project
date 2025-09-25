import csv
import bank.account_exceptions as accountExp
from bank.bank import Bank

class Account():
    def __init__(self):
        self.logged_customer = False
        
    def create_account(self, initial_amount):
        while True:
            try:
                if type(int(initial_amount)) == int:
                    if int(initial_amount) < 0:
                        raise ValueError
                    elif int(initial_amount) >= 0:
                        return initial_amount
                else:
                    raise ValueError
                
            except ValueError:
                raise accountExp.AccountCreationError('Enter 0 or a POSITIVE NUMBER')
            
            except accountExp.AccountCreationError as e:
                print(f'🚩 | AccountCreationError: {e}\n')
                return

    def withdraw_operation(self, customer_id):
        while True:
            try:
                account_option = int(input('\n[WITHDRAW OPERATIONS]\n1️⃣  Checking account\n2️⃣  Savings account\n0️⃣  Go Back\nEnter the number of which account would you like to withdraw from, or 0 to go back: '))
                if account_option == 1:
                    checking_completed = False
                    while True:
                        bank_customers = Bank()
                        bank_customers.retrieve_customers()
                        with open(bank_customers.fileName, 'r', newline='') as file:
                            reader = csv.reader(file)
                            next(reader)
                            row_index = 1
                            print('\n[WITHDRAW CHECKING]')
                            for row in reader:
                                if customer_id == row[0]:
                                    if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                        if bank_customers.customers[row_index][4] != '':
                                            if int(bank_customers.customers[row_index][4]) > 0:
                                                print(f'💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                checking_amount = int(input('💳 | Checking Amount: '))
                                                old_checking_balance = int(bank_customers.customers[row_index][4])
                                                bank_customers.customers[row_index][4] = str(old_checking_balance - checking_amount)
                                                bank_customers.update_customers()
                                                print(f'🔴 | The old checking balance = {old_checking_balance}\n📉 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                checking_completed = True
                                                break
                                            else:
                                                while True:
                                                    print(f'💲 | Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                    checking_amount = int(input('💳 | Checking Amount: '))
                                                    if checking_amount > 100:
                                                        raise accountExp.WithdrawError(f'As your cehcking balance is {bank_customers.customers[row_index][4]}, you are not allowed to withdraw {checking_amount} as it above 100')
                                                    elif checking_amount <= 100 and checking_amount > 0:
                                                        bank_customers.overdraft_protection_fee(customer_id, checking_amount)                                                            
                                                        return
                                                    else:
                                                        raise accountExp.WithdrawError('Can not withdraw zero or neigative amount')
                                        else:
                                            print(f'‼️  | The customer with id {customer_id} don\'t have a checking account')
                                            account_creation = input('❓ | Do you want to create a checking account (yes/no): ').lower()
                                            match account_creation:
                                                case 'yes':
                                                    while True:
                                                        checking_account = self.create_checking_account()
                                                        if checking_account >= 0:
                                                            bank_customers.customers[row_index][4] = int(checking_account)
                                                            bank_customers.update_customers()
                                                            print(f'✔️  | Your checking account has been created and the balance now is {bank_customers.customers[row_index][4]}\n')
                                                            return
                                                        elif int(checking_account) < 0:
                                                            raise accountExp.WithdrawError('Can not initiate your checking account with neigative amount\n')
                                                        else:
                                                            raise ValueError
                                                case 'no':
                                                    print('💰 | Your checking account still not created\n')
                                                    return
                                                case _:
                                                    if account_creation.isalpha():
                                                        raise accountExp.WithdrawError('Enter a YES or NO only')
                                                    else:
                                                        raise ValueError
                                    else:
                                        print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                        reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                        match reactivate:
                                            case 'yes':
                                                while True:
                                                    print(f'💲| Your Checking Balance : {bank_customers.customers[row_index][4]}')
                                                    charge_amount = int(input('💳 | Charge Amount: '))
                                                    aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                    if aprroved_balance < 0:
                                                        raise accountExp.WithdrawError(f'This {charge_amount} can not reactivate your account')
                                                    else:
                                                        bank_customers.activate_customer(customer_id, charge_amount)
                                                        break
                                            case 'no':
                                                print('💰 | Your account remain DEACTIVE')
                                                return
                                            case _:
                                                raise ValueError
                                row_index += 1
                        if checking_completed:
                            break
                elif account_option == 2:    
                    savings_completed = False
                    while True:
                        print('\n[WITHDRAW SAVINGS]')
                        bank_customers = Bank()
                        bank_customers.retrieve_customers()
                        with open('bank.csv', 'r', newline='') as file:
                            reader = csv.reader(file)
                            next(reader)
                            row_index = 1
                            for row in reader:
                                if customer_id == row[0]:
                                    if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                                        if bank_customers.customers[row_index][5] != '':
                                            if int(bank_customers.customers[row_index][5]) >= 0:
                                                print(f'💲 | Your Savings Balance : {bank_customers.customers[row_index][4]}')
                                                savings_amount = int(input('💳 | Savings Amount: '))
                                                old_savings_balance = int(bank_customers.customers[row_index][4])
                                                bank_customers.customers[row_index][5] = str(old_savings_balance - savings_amount)
                                                bank_customers.update_customers()
                                                print(f'🔴 | The old savings balance = {old_savings_balance}\n📉 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                savings_completed = True
                                                break
                                            elif int(bank_customers.customers[row_index][5]) == 0:
                                                raise accountExp.WithdrawError(f'Can not withdraw any amount as the savings balance is {bank_customers.customers[row_index][5]}')
                                            else:
                                                raise ValueError
                                        else:
                                            print(f'‼️  | The customer with id {customer_id} don\'t have a savings account')
                                            account_creation = input('❓ | Do you want to create a savings account (yes/no): ').lower()
                                            match account_creation:
                                                case 'yes':
                                                    while True:
                                                        savings_account = self.create_savings_account()
                                                        if int(savings_account) >= 0:
                                                            bank_customers.customers[row_index][5] = int(savings_account)
                                                            bank_customers.update_customers()
                                                            print(f'✔️  | Your savings account has been created and the balance now is {bank_customers.customers[row_index][5]}\n')
                                                            return
                                                        elif int(savings_account) < 0:
                                                            raise accountExp.WithdrawError('Can not initiate your checking account with neigative amount\n')
                                                        else:
                                                            raise ValueError
                                                case 'no':
                                                    print('💰 | Your savings account still not created\n')
                                                    return
                                                case _:
                                                    raise ValueError
                                    else:
                                        print(f'🔽 | The accounts assoiated with customer ID {customer_id} are DEACTIVE for now')
                                        reactivate = input('❓ | Do you want to REACTIVATE your accounts (yes/no): ').lower()
                                        match reactivate:
                                            case 'yes':
                                                while True:
                                                    print(f'💲| Your savings Balance : {bank_customers.customers[row_index][4]}')
                                                    charge_amount = int(input('💳 | Charge Amount: '))
                                                    aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                                    if aprroved_balance < 0:
                                                        raise accountExp.WithdrawError(f'This {charge_amount} can not reactivate your account')
                                                    else:
                                                        bank_customers.activate_customer(customer_id, charge_amount)
                                                        break
                                            case 'no':
                                                print('💰 | Your account remain DEACTIVE')
                                                return
                                            case _:
                                                raise ValueError
                                row_index += 1
                        if savings_completed:
                            break
                else:
                    raise accountExp.WithdrawError('Enter a VALID operation option')
                break
            except ValueError:
                if not account_creation.isalpha():
                    raise accountExp.WithdrawError('Enter a YES or NO')
                elif not checking_account.isdigit():
                    raise accountExp.WithdrawError('Enter a NUMBER operation option')
                elif not savings_amount.isdigit():
                    raise accountExp.WithdrawError('Enter a NUMBER operation option')
            except FileNotFoundError:
                raise accountExp.WithdrawError(f'The file {bank_customers.fileName} Not found')
            except accountExp.WithdrawError as e:
                print(f'🚩 | WithdrawError: {e}\n')

# deposit requierments:
# # 1. the user can deposit any > 0 amount into the checking/saving accounts 
# # 2. the user can not deposit a -ve amount into the checking/saving accounts 
# # 3. the user need to be logged in so he/she can deposit an amount

    def deposit_checking(self, customer_id):
        checking_deposit_completed = False
        checking_deposit = 0
        while True:
            print('[DEPOSIT CHECKING]\n')
            bank_customers = Bank()
            bank_customers.retrieve_customers()
            
            with open('bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                row_index = 1
                for row in reader:
                    if customer_id == row[0]:
                        if bank_customers.customers[row_index][6] != 'deactive' and int(bank_customers.customers[row_index][7]) < 2:
                            if bank_customers.customers[row_index][4] != '' and int(bank_customers.customers[row_index][4]) >= 0:
                                checking_deposit = int(input('Deposit Amount Into Checking: '))
                                if checking_deposit > 0:
                                    old_checking_balance = int(bank_customers.customers[row_index][4])
                                    bank_customers.customers[row_index][4] = str(old_checking_balance + checking_deposit)
                                    bank_customers.update_customers()
                                    print(f'🔵 | The old checking balance = {old_checking_balance}\n📈 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                    checking_deposit_completed = True
                                    break
                                
                                else:
                                    # raise error
                                    print(f'Can\'t deposit {checking_deposit} into the checking account')
                            
                            elif int(bank_customers.customers[row_index][4]) < 0:
                                bank_customers.overdraft_protection_fee(customer_id, checking_deposit)                                                            
                                break
                            else:
                                print(f'the customer with id: {customer_id} don\'t have a checking account')
                        else:
                            print(f'the customer accounts with id: {customer_id} are deactive for now.....')
                            reactivate = input('Do you want to activate the accounts (yes/no): ').lower()
                            match reactivate:
                                case 'yes':
                                    while True:
                                        charge_amount = int(input('Charge amount: '))
                                        aprroved_balance = int(bank_customers.customers[row_index][4]) + charge_amount
                                        print(aprroved_balance)
                                        if aprroved_balance < 0:
                                            print(f'This {charge_amount} can\'t make your balance >= 0')
                                        else:
                                            bank_customers.activate_customer(customer_id, charge_amount)
                                            break
                                case 'no':
                                    print('Your account remain DEACTIVE')
                                    return

                    row_index += 1
                    
            if checking_deposit_completed:
                break

    def deposit_savings(self, customer_id):
        savings_deposit_completed = False
        while True:
            print('[DEPOSIT SAVINGS]\n')
            bank_customers = Bank()
            bank_customers.retrieve_customers()
            
            with open('bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                row_index = 1
                for row in reader:
                    if customer_id == row[0]:
                        if bank_customers.customers[row_index][5] != '':
                            savings_deposit = int(input('Deposit Amount Into Savings: '))
                            if savings_deposit > 0:
                                old_savings_balance = int(bank_customers.customers[row_index][5])
                                bank_customers.customers[row_index][5] = str(old_savings_balance + savings_deposit)
                                bank_customers.update_customers()
                                print(f'🔵 | The old savings balance = {old_savings_balance}\n📈 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                savings_deposit_completed = True
                                break
                            
                            else:
                                # raise error
                                print(f'Can\'t deposit {savings_deposit} into the savings account')
                        else:
                            print(f'the customer with id: {customer_id} don\'t have a savings account')
                    row_index += 1

            if savings_deposit_completed:
                break

# transfer requierments:
# # A. between customer's accounts 
# # # A.1. from checking to savings
# # # # i. the user can transfer amount less than or equal to the checking_balance
# # # # ii. the user can not transfer -ve amount
# # # # iii. overdraft fee $35 applied when try to transfer and the checking_balance is negative

# # # A.2. from savings to checking
# # # # i. the user can transfer amount less than or equal to the savings_balance
# # # # ii. the user can not transfer -ve amount
# # # # iii. no transfer allowed when the savings_balance = 0 **the savings_balance can not be -ve**
    def transfer_between_accounts(self, customer_id, customer_choice):

        match customer_choice:
            case 1:
                transfer_between_accounts_completed = False
                while True:
                    print('[TRANSFER FROM CHECKING TO SAVINGS]\n')
                    bank_customers = Bank()
                    bank_customers.retrieve_customers()
                    
                    with open('bank.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader)
                        row_index = 1
                        for row in reader:
                            if customer_id == row[0]:
                                if bank_customers.customers[row_index][4] != '' and bank_customers.customers[row_index][5] != '':
                                    
                                    transfer_amount = int(input('Transfer Amount From Checking To Savings: '))
                                    if int(bank_customers.customers[row_index][4]) > 0:
                                        
                                        if transfer_amount > 0 and transfer_amount <= int(bank_customers.customers[row_index][4]):
                                            old_checking_balance = int(bank_customers.customers[row_index][4])
                                            bank_customers.customers[row_index][4] = str(old_checking_balance - transfer_amount)
                                            old_savings_balance = int(bank_customers.customers[row_index][5])
                                            bank_customers.customers[row_index][5] = str(old_savings_balance + transfer_amount)
                                            
                                            bank_customers.update_customers()
                                            print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                            print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                            transfer_between_accounts_completed = True
                                            break
                                        
                                        else:
                                            # raise error
                                            print(f'Can\'t transfer {transfer_amount} from checking to savings account as it exceed the checking account balance')
                                            break
                                    
                                    else:
                                        print(f'Can\'t transfer {transfer_amount} from checking to savings account as the account balance is {bank_customers.customers[row_index][4]}')
                                        # apply the overdraft fee here (call the method after creation)
                                        break
                                
                                elif bank_customers.customers[row_index][4] == '':
                                    print(f'the customer with id: {customer_id} don\'t have a checking account')
                                    return
                                    
                                elif bank_customers.customers[row_index][5] == '':
                                    print(f'the customer with id: {customer_id} don\'t have a savings account')
                                    return
                                    
                                else:
                                    print(f'the customer with id: {customer_id} don\'t have both checking and savings accounts')
                                    return
                            
                            row_index += 1

                    if transfer_between_accounts_completed:
                        break
            case 2:
                transfer_between_accounts_completed = False
                while True:
                    print('[TRANSFER FROM SAVINGS TO CHECKING]\n')
                    bank_customers = Bank()
                    bank_customers.retrieve_customers()
                    
                    with open('bank.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader)
                        row_index = 1
                        for row in reader:
                            if customer_id == row[0]:
                                if bank_customers.customers[row_index][4] != '' and bank_customers.customers[row_index][5] != '':
                                    
                                    transfer_amount = int(input('Transfer Amount From Savings To Checking: '))
                                    if int(bank_customers.customers[row_index][5]) > 0:
                                        
                                        if transfer_amount > 0 and transfer_amount <= int(bank_customers.customers[row_index][5]):
                                            old_checking_balance = int(bank_customers.customers[row_index][4])
                                            bank_customers.customers[row_index][4] = str(old_checking_balance + transfer_amount)
                                            old_savings_balance = int(bank_customers.customers[row_index][5])
                                            bank_customers.customers[row_index][5] = str(old_savings_balance - transfer_amount)
                                            
                                            bank_customers.update_customers()
                                            print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                            print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                            transfer_between_accounts_completed = True
                                            break
                                        
                                        else:
                                            # raise error
                                            print(f'Can\'t transfer {transfer_amount} from savings to checking account as it exceed the savings account balance')
                                            break
                                    
                                    else:
                                        print(f'Can\'t transfer {transfer_amount} from savings to checking account as the account balance is {bank_customers.customers[row_index][5]}')
                                        break
                                
                                elif bank_customers.customers[row_index][4] == '':
                                    print(f'the customer with id: {customer_id} don\'t have a checking account')
                                    return
                                    
                                elif bank_customers.customers[row_index][5] == '':
                                    print(f'the customer with id: {customer_id} don\'t have a savings account')
                                    return
                                    
                                else:
                                    print(f'the customer with id: {customer_id} don\'t have both checking and savings accounts')
                                    return
                            
                            row_index += 1

                    if transfer_between_accounts_completed:
                        break       

# # B. the user can not deposit a -ve amount into the checking/saving accounts 
# # # B.1. from checking to another account
# # # # i. the user can transfer amount less than or equal to the checking_balance
# # # # ii. the user can not transfer -ve amount
# # # # iii. overdraft fee $35 applied when try to transfer and the checking_balance is negative

# # # B.2. from savings to another acccount
# # # # i. the user can transfer amount less than or equal to the savings_balance
# # # # ii. the user can not transfer -ve amount
# # # # iii. no transfer allowed when the savings_balance = 0 **the savings_balance can not be -ve**
    def transfer_to_customer_account(self, customer_id, customer_choice):

        match customer_choice:
            case 1:
                transfer_to_customer_completed = False
                while True:
                    print('[TRANSFER FROM CHECKING TO CUSTOMER\'S ACCOUNT]\n')
                    bank_customers = Bank()
                    bank_customers.retrieve_customers()

                    other_customer_id = input('Enter the customer\'s account id you want to transfer to: ')
                    other_customer_row_index = 0

                    other_customer_found = False
                    if other_customer_id == customer_id:
                        print(f'The customer with id: {other_customer_id} is the current customer')

                    else:
                        with open('bank.csv', 'r', newline='') as file:
                            reader = csv.reader(file)
                            next(reader)
                            row_index = 1
                            for row in reader:
                                if other_customer_id == row[0]:
                                    other_customer_found = True
                                    other_customer_row_index = row_index
                                    break
                                row_index += 1

                            if other_customer_found:
                                with open('bank.csv', 'r', newline='') as file:
                                    reader = csv.reader(file)
                                    next(reader)                            
                                    row_index = 1
                                    for row in reader:
                                        if customer_id == row[0]:
                                            if bank_customers.customers[row_index][4] != '' and bank_customers.customers[other_customer_row_index][4] != '':

                                                if int(bank_customers.customers[row_index][4]) >= 0:
                                                    transfer_amount = int(input('Transfer Amount From Checking To Customer\'s Account: '))

                                                    if transfer_amount > 0 and transfer_amount <= int(bank_customers.customers[row_index][4]):
                                                        old_checking_balance = int(bank_customers.customers[row_index][4])
                                                        bank_customers.customers[row_index][4] = str(old_checking_balance - transfer_amount)
                                                        other_customer_balance = int(bank_customers.customers[other_customer_row_index][4])
                                                        bank_customers.customers[other_customer_row_index][4] = str(other_customer_balance + transfer_amount)

                                                        bank_customers.update_customers()
                                                        print(f'🔶 | The old checking balance = {old_checking_balance}\n🔷 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                                        print(f'🔶 | The old other customer balance = {other_customer_balance}\n🔷 | The new  other customer balance = {bank_customers.customers[other_customer_row_index][4]}\n')
                                                        transfer_to_customer_completed = True
                                                        break

                                                    else:
                                                        # raise error
                                                        print(f'Can\'t transfer {transfer_amount} from checking to other customer account as it exceed the checking account balance')
                                                        break
                                                
                                                else:
                                                    while True:
                                                        transfer_amount = int(input('Transfer Amount From Checking To Customer\'s Account: '))
                                                        if transfer_amount > 100:
                                                            print(f'You are not allowed to transfer {transfer_amount} as it above 100')
                                                        elif transfer_amount <= 100 and transfer_amount > 0:
                                                            print(f'Can\'t transfer {transfer_amount} from checking to savings account as the account balance is {bank_customers.customers[row_index][4]}')
                                                            # apply the overdraft fee here (call the method after creation)
                                                            bank_customers.overdraft_protection_fee(customer_id, transfer_amount)                                                            
                                                            break
                                                        else:
                                                            print('can not enter a -ve amount')

                                                    break
                                            
                                            elif bank_customers.customers[row_index][4] == '':
                                                print(f'the customer with id: {customer_id} don\'t have a checking account')
                                                return

                                            elif bank_customers.customers[other_customer_row_index][4] == '':
                                                print(f'the customer with id: {customer_id} don\'t have a checking account')
                                                return

                                            else:
                                                print(f'the both of you and other customer with id: {customer_id} don\'t have both checking accounts')
                                                return

                                        row_index += 1

                                if transfer_to_customer_completed:
                                    break

                            else:
                                print(f'The customer with id: {other_customer_id} that you want to transfer to does not exsit in the system')

            case 2:
                transfer_between_accounts_completed = False
                while True:
                    print('[TRANSFER FROM SAVINGS TO CUSTOMER\'S ACCOUNT]\n')
                    bank_customers = Bank()
                    bank_customers.retrieve_customers()

                    other_customer_id = input('Enter the customer\'s account id you want to transfer to: ')
                    other_customer_row_index = 0

                    other_customer_found = False
                    if other_customer_id == customer_id:
                        print(f'The customer with id: {other_customer_id} is the current customer')

                    else:
                        with open('bank.csv', 'r', newline='') as file:
                            reader = csv.reader(file)
                            next(reader)
                            row_index = 1
                            for row in reader:
                                if other_customer_id == row[0]:
                                    other_customer_found = True
                                    other_customer_row_index = row_index
                                    break
                                row_index += 1

                            if other_customer_found:
                                with open('bank.csv', 'r', newline='') as file:
                                    reader = csv.reader(file)
                                    next(reader)                            
                                    row_index = 1
                                    for row in reader:
                                        if customer_id == row[0]:
                                            if bank_customers.customers[row_index][5] != '' and bank_customers.customers[other_customer_row_index][4] != '':

                                                transfer_amount = int(input('Transfer Amount From Savings To Customer\'s Account: '))
                                                if int(bank_customers.customers[row_index][5]) > 0:

                                                    if transfer_amount > 0 and transfer_amount <= int(bank_customers.customers[row_index][5]):
                                                        old_savings_balance = int(bank_customers.customers[row_index][5])
                                                        bank_customers.customers[row_index][5] = str(old_savings_balance - transfer_amount)
                                                        other_customer_balance = int(bank_customers.customers[other_customer_row_index][4])
                                                        bank_customers.customers[other_customer_row_index][4] = str(other_customer_balance + transfer_amount)

                                                        bank_customers.update_customers()
                                                        print(f'🔶 | The old savings balance = {old_savings_balance}\n🔷 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                                        print(f'🔶 | The old other customer balance = {other_customer_balance}\n🔷 | The new  other customer balance = {bank_customers.customers[other_customer_row_index][4]}\n')
                                                        transfer_to_customer_completed = True
                                                        break

                                                    else:
                                                        # raise error
                                                        print(f'Can\'t transfer {transfer_amount} from savings to other customer account as it exceed the savings account balance')
                                                        break
                                                
                                                else:
                                                    print(f'Can\'t transfer {transfer_amount} from savings to savings account as the account balance is {bank_customers.customers[row_index][4]}')
                                                    # apply the overdraft fee here (call the method after creation)
                                                    break
                                            
                                            elif bank_customers.customers[row_index][5] == '':
                                                print(f'the customer with id: {customer_id} don\'t have a savings account')
                                                return

                                            elif bank_customers.customers[other_customer_row_index][4] == '':
                                                print(f'the customer with id: {customer_id} don\'t have a savings account')
                                                return

                                            else:
                                                print(f'the both of you and other customer with id: {customer_id} don\'t have both savings accounts')
                                                return

                                        row_index += 1

                                if transfer_to_customer_completed:
                                    break

                            else:
                                print(f'The customer with id: {other_customer_id} that you want to transfer to does not exsit in the system')
