# Customer class defs:
# # init
# # customer registeration
# # customer login

import csv, random
from bank.bank import Bank
import bank.customer_exceptions as customerExp

class Customer:
    def __init__(self):
        self.customer_id = 0
        self.fname = ''
        self.lname = ''
        self.password = ''
        self.checking_balance = None
        self.savings_balance = None
        self.active_status = 'active'
        self.overdraft_attempt = 0
        self.logged_customer = False
        self.logged_customer_id = ''

    bank = Bank()
    def generate_id(self, customer_id):
        id_unique = False
        while id_unique == False:
            random_id = str(random.randint(10000, 11000))
            with open(Customer.bank.file_name, 'r', newline='') as file:
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
                return customer_id

    def add_customer(self, new_customer_list):
        bank_customers = Bank()
        bank_customers.retrieve_customers()
        if len(new_customer_list) == 8:
            bank_customers.customers.append(new_customer_list)

            with open(Customer.bank.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                for data in bank_customers.customers:
                    writer.writerow(data)
            return 'The customer added successfully'
        else:
            raise customerExp.AddCustomerError('Sorry, the customer not added to the bank')

    
    def login_customer(self):
        while self.logged_customer == False:
            with open(Customer.bank.file_name, 'r', newline='') as file:
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