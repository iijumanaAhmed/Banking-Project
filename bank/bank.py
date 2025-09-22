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

    # def deactivate_customer(self, customer):
    #     # deactivate the account after 2 overdrafts

    # def activate_customer(self, customer):
    #     # reactivate the account if the customer brings the account current, paying both the overdraft amount and the resulting overdraft fees
