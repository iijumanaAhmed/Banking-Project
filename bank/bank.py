import csv

# Bank class defs:
# # init
# # display of all customer accounts
# # Transfer Money Between Accounts
# # Overdraft Protection?

class Bank:
    def __init__(self):
        self.customers = []
        self.file_name = 'bank.csv'

    def retrieve_customers(self):
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.customers.append(row)

        return self.customers

    def update_customers(self):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for data in self.customers:
                writer.writerow(data)

# Build Overdraft Protection

    def overdraft_protection_fee(self, customer_id, amount):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        overdraft_fee = 35
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row_index = 1
            for row in reader:
                if customer_id == row[0]:
                    if int(bank_customers.customers[row_index][7]) == 0:
                        print(f'⚠️  | You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                        bank_customers.customers[row_index][4] = int(bank_customers.customers[row_index][4]) - int(amount) - overdraft_fee
                        bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                        print(f'\n⚠️  | Based on the Overdraft Protection Rules, you are charged ${overdraft_fee} for this overdraft\nℹ️  | Number of attemtps before deactivate the account = {bank_customers.customers[row_index][7]}\n💲 | The checking account balance now is {bank_customers.customers[row_index][4]}')
                        bank_customers.update_customers()
                        break

                    elif int(bank_customers.customers[row_index][7]) == 1:
                        print(f'⚠️  | You tried to overdraft an amount {amount} while your checking account balance is {bank_customers.customers[row_index][4]}')
                        bank_customers.customers[row_index][4] = int(bank_customers.customers[row_index][4]) - int(amount) - overdraft_fee
                        bank_customers.customers[row_index][6] = 'deactive'
                        bank_customers.customers[row_index][7] = str(int(bank_customers.customers[row_index][7]) + 1)
                        print(f'\n⚠️  | Based on the Overdraft Protection Rules, you are charged ${overdraft_fee} for this overdraft\nℹ️  | You have reached the maximum overdraft attempts = {bank_customers.customers[row_index][7]}, and your account now is DEACTIVE\n💲 | The checking account balance now is {bank_customers.customers[row_index][4]}')
                        bank_customers.update_customers()
                        break
                row_index += 1

    def activate_customer(self, customer_id, amount):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row_index = 1
            for row in reader:
                if customer_id == row[0]:
                    if int(bank_customers.customers[row_index][7]) == 2 and int(bank_customers.customers[row_index][4]) < 0:
                        print(f'✔️  | Your account has been reactivated as the checking account balance now is {int(bank_customers.customers[row_index][4]) + int(amount)}')
                        bank_customers.customers[row_index][4] = str(int(bank_customers.customers[row_index][4]) + int(amount))
                        bank_customers.customers[row_index][6] = 'active'
                        bank_customers.customers[row_index][7] = 0
                        bank_customers.update_customers()
                        return
                row_index += 1