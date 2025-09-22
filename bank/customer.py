# Customer class defs:
# # init
# # customer registeration
# # customer login

import csv
from bank.bank import Bank

class Customer:
    def __init__(self):
        self.logged_customer = False
        self.logged_customer_id = ''

    def add_customer(self, new_customer):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        bank_customers.customers.append(new_customer)

        with open('bank.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for data in bank_customers.customers:
                writer.writerow(data)
                
    def login_customer(self):
        while self.logged_customer == False:
            with open('bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                print('[LOGIN PAGE]\n')
                login_id = input('Customer ID: ')
                login_password = input('Customer Password: ')
                for row in reader:
                    if login_id == row[0] and login_password == row[3]:
                        self.logged_customer = True
                        break

                    elif login_id != row[0] or login_password != row[3]:
                        self.logged_customer = False

            if self.logged_customer:
                print(f'Logged in successfully!! Welcome, {row[1]} {row[2]}')
                self.logged_customer_id = login_id
                return self.logged_customer
            else:
                print(f'The customer with {login_id} does not exsit in the system!, Try again\n')