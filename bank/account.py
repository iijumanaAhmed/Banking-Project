# Account class defs:
# # init
# # Withdraw Money from Checking Account - done
# # Withdraw Money from Savings Account - done
# # Deposit Money into Checking Account
# # Deposit Money into Savings Account

import csv
from bank.bank import Bank

class Account():
    def __init__(self):
        self.logged_customer = False

    def withdraw_checking(self, customer_id):
        checking_completed = False
        while True:
            print('[WITHDRAW CHECKING]\n')
            bank_customers = Bank()
            bank_customers.retrieve_customers()

            with open('bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                row_index = 1
                for row in reader:
                    if customer_id == row[0]:
                        if bank_customers.customers[row_index][4] != '':
                            checking_amount = int(input('Checking Amount: '))
                            if checking_amount > 0 and checking_amount <= 100:
                                old_checking_balance = int(bank_customers.customers[row_index][4])
                                bank_customers.customers[row_index][4] = str(old_checking_balance - checking_amount)
                                bank_customers.update_customers()
                                print(f'🔴 | The old checking balance = {old_checking_balance}\n📉 | The new checking balance = {bank_customers.customers[row_index][4]}\n')
                                checking_completed = True
                                break
                            else:
                                print(f'Can\'t withdraw {checking_amount} from the checking account')
                                break
                        else:
                            print(f'the customer with id: {customer_id} don\'t have a checking account')
                    row_index += 1
            if checking_completed:
                break
            
            # write overdraft protection marning and appliance

    def withdraw_savings(self, customer_id):
        savings_completed = False
        while True:
            print('[WITHDRAW SAVINGS]\n')
            bank_customers = Bank()
            bank_customers.retrieve_customers()
            
            with open('bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                row_index = 1
                for row in reader:
                    if customer_id == row[0]:
                        if bank_customers.customers[row_index][5] != '':
                            savings_amount = int(input('Savings Amount: '))
                            if savings_amount > 0 and savings_amount <= 100:
                                old_savings_balance = int(bank_customers.customers[row_index][5])
                                bank_customers.customers[row_index][5] = str(old_savings_balance - savings_amount)
                                bank_customers.update_customers()
                                print(f'🔴 | The old savings balance = {old_savings_balance}\n📉 | The new savings balance = {bank_customers.customers[row_index][5]}\n')
                                savings_completed = True
                                break
                            else:
                                print(f'Can\'t withdraw {savings_amount} from the savings account')
                        else:
                            print(f'the customer with id: {customer_id} don\'t have a savings account')
                    row_index += 1
            if savings_completed:
                break
            
            # write overdraft protection marning and appliance