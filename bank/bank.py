import csv

# Bank class defs:
# # init
# # display of all customer accounts
# # Transfer Money Between Accounts
# # Overdraft Protection?

class Bank:
    def __init__(self):
        self.customers = []

    def retrieve_customers(self):
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.customers.append(row)

        return self.customers

    def update_customers(self):
        with open('bank.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for data in self.customers:
                writer.writerow(data)

# Build Overdraft Protection

    def overdraft_protection_fee(self, customer_id, amount):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        overdraft_fee = 35
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row_index = 1
            for row in reader:
                if customer_id == row[0]:
                    if int(bank_customers.customers[row_index][7]) == 0:
                        print(f'You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                        bank_customers.customers[row_index][4] = str(int(bank_customers.customers[row_index][4]) - amount - overdraft_fee)
                        bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                        print(f'number of attemtps before deactivate the account = {bank_customers.customers[row_index][7]}\nYou are charged 35 fee for this overdraft\n\nThe checking account balance now is {bank_customers.customers[row_index][4]}')
                        bank_customers.update_customers()
                        break

                    elif int(bank_customers.customers[row_index][7]) == 1:
                        print(f'You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                        bank_customers.customers[row_index][4] = str(int(bank_customers.customers[row_index][4]) - amount - overdraft_fee)
                        bank_customers.customers[row_index][6] = 'deactive'
                        bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                        print(f'you have reached th amximum attempts before deactivate the account = {bank_customers.customers[row_index][7]}\nYou are charged 35 fee for this overdraft\n\nThe checking account balance now is {bank_customers.customers[row_index][4]}\n****Deposit the charged amount or above it to reactivate your account')
                        bank_customers.update_customers()
                        break
                row_index += 1

    def activate_customer(self, customer_id, amount):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row_index = 1
            for row in reader:
                if customer_id == row[0]:
                    if int(bank_customers.customers[row_index][7]) == 2 and int(bank_customers.customers[row_index][4]) < 0:
                        if int(bank_customers.customers[row_index][4]) + int(amount) >= 0:
                            print(f'Your account has been reactivated as the checking account balance is {int(bank_customers.customers[row_index][4]) + int(amount)}')
                            bank_customers.customers[row_index][4] = str(int(bank_customers.customers[row_index][4]) + int(amount))
                            bank_customers.customers[row_index][6] = 'active'
                            bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) - 2)
                            bank_customers.update_customers()
                            return
                row_index += 1