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
        self.added_customer = False

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
            print('The customer added successfully')
            self.added_customer = True
        else:
            self.added_customer = False
            raise customerExp.AddCustomerError('Sorry, the customer not added to the bank')

        return self.added_customer

    
    def login_customer(self, customer_id, customer_password):
        while self.logged_customer == False:
            with open(Customer.bank.file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if customer_id == row[0] and customer_password == row[3]:
                        self.logged_customer = True
                        break

                    elif customer_id != row[0] or customer_password != row[3]:
                        self.logged_customer = False

            if self.logged_customer:
                print(f'Logged in successfully!! Welcome, {row[1]} {row[2]}')
                self.logged_customer_id = customer_id
                return self.logged_customer
            else:
                return self.logged_customer