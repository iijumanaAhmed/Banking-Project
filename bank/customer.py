# Customer class defs:
# # init
# # customer registeration
# # customer login

import csv

class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
    
    def customer_register(self, customer):
        with open('bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(customer)
    