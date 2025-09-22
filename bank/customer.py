# Customer class defs:
# # init
# # customer registeration
# # customer login

import csv
from bank.bank import Bank

class Customer:
    def __init__(self):
        self.logged_customer = False

    def login_customer(self):
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            while self.logged_customer == False:
                print('[LOGIN PAGE]\n')
                login_id = input('Customer ID: ')
                login_password = input('Customer Password: ')
                for row in reader:
                    if login_id == row[0]:
                        if login_password == row[3]:
                            self.logged_customer = True
                            break

                    else:
                        print(f'The customer with {login_id} does not exsit in the system!, Try again\n')
                        break

                if self.logged_customer:
                    print(f'Logged in successfully !! Welcome, {row[1]} {row[2]}')
                    return self.logged_customer
                else:
                    continue