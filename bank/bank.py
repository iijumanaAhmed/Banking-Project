import csv, random

# Bank class defs:
# # init
# # display of all customer accounts
# # Transfer Money Between Accounts
# # Overdraft Protection?

# Customer class defs:
# # init
# # add new customer info

# Account class defs:
# # init
# # Withdraw Money from Account
# # Deposit Money into Account

# .csv file 
# # add column 'active_status'
# # 

class Bank:
    def __init__(self):
        self.customers = []
        
    def add_customer(self, customer):
        with open('bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(customer)

            
# Build Overdraft Protection

    # def deactivate_customer(self, customer):
    #     # deactivate the account after 2 overdrafts
            
    # def activate_customer(self, customer):
    #     # reactivate the account if the customer brings the account current, paying both the overdraft amount and the resulting overdraft fees

class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        
    def check_id(self, customer_id):
        id_unique = False
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if customer_id == row[0]:
                    id_unique = False
                    break
                else:
                    id_unique = True
                    
            # print(id_unique)
            if id_unique:
                print(f'{customer_id}, This id is unique')
            else:
                print(f'{customer_id}, This id is NOT unique')
    
if __name__ == '__main__':    
    customers = [
        ['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings'],
        ['10001', 'suresh', 'sigera', 'juagw362', '1000', '10000'],
        ['10002', 'james', 'taylor', 'idh36%@#FGd', '10000', '10000'],
        ['10003', 'melvin', 'gordon', 'uYWE732g4ga1', '2000', '20000'],
        ['10004', 'stacey', 'abrams', 'DEU8_qw3y72$', '2000', '20000'],
        ['10005', 'jake', 'paul', 'd^dg23g)@', '100000', '100000']
    ]

    with open('bank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customers)

    with open('bank.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            
    bank = Bank()
    bank.add_customer(['00000', 'jumana', 'paul', 'd^dg23g)@', '100000', '100000'])
    bank.add_customer(['001100', 'lama', 'paul', 'd^dg23g)@', '100000', '100000'])
    
    id = random.randint(10000, 15000)
    # print(id)
    password = 'hello1'
    cust = Customer(id)
    # at this stage checking the unique id
    cust.check_id(str(id))
    
    with open('bank.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
        
