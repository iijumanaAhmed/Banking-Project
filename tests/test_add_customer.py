import unittest
from bank.customer import Customer
from bank.account import Account
from bank.bank import Bank
import bank.customer_exceptions as customerExp
import bank.account_exceptions as accountExp

class TestAddCustomer(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.correct_customer = Customer()
        self.wrong1_customer = Customer()
        self.wrong2_customer = Customer()
        self.account = Account()
        self.bank_length_before = Bank()
        self.bank_length_after = Bank()
        self.correct_customer.customer_id = self.correct_customer.generate_id(self.correct_customer.customer_id)
        self.correct_customer.fname = 'Jumana'
        self.correct_customer.lname = 'Khawaji'
        self.correct_customer.password = '1234JA@'
        self.correct_customer.checking_balance = self.account.create_account(100)
        self.correct_customer.savings_balance = self.account.create_account(500)
        self.correct_customer.active_status = 'active'
        self.correct_customer.overdraft_attempt = 0
        
        self.wrong1_customer.fname = 'Juma12'
        self.wrong1_customer.lname = '66waji'
        
        self.correct_customer_list = [self.correct_customer.customer_id, self.correct_customer.fname, self.correct_customer.lname, self.correct_customer.password, self.correct_customer.checking_balance, self.correct_customer.savings_balance, self.correct_customer.active_status, self.correct_customer.overdraft_attempt]
        self.wrong_customer_list = [self.correct_customer.customer_id, self.correct_customer.fname, self.correct_customer.lname, self.correct_customer.checking_balance, self.correct_customer.savings_balance, self.correct_customer.active_status, self.correct_customer.overdraft_attempt]
        
    def tearDown(self):
        print('Tearing down')
        
    def test_add_customer(self):
        self.assertEqual(self.correct_customer.customer_id, self.correct_customer.customer_id)
        self.assertEqual(self.correct_customer.fname, 'Jumana')
        
        self.assertEqual(self.correct_customer.lname, 'Khawaji')
        self.assertEqual(self.correct_customer.checking_balance, 100)
        self.assertEqual(self.correct_customer.savings_balance, 500)
        self.assertEqual(self.correct_customer.active_status, 'active')
        self.assertEqual(self.correct_customer.overdraft_attempt, 0)

        
        with self.assertRaises(accountExp.AccountCreationError):
            self.wrong1_customer.checking_balance = self.account.create_account(-50)
        with self.assertRaises(accountExp.AccountCreationError):
            self.wrong1_customer.savings_balance = self.account.create_account(-40)  
        with self.assertRaises(customerExp.AddCustomerError):
            self.wrong1_customer.add_customer(self.wrong_customer_list)
        with self.assertRaises(accountExp.AccountCreationError):
            self.wrong2_customer.checking_balance = self.account.create_account('hi')
        with self.assertRaises(accountExp.AccountCreationError):
            self.wrong2_customer.savings_balance = self.account.create_account('welcome')

        self.length_before = len(self.bank_length_before.retrieve_customers())
        self.assertEqual(self.correct_customer.add_customer(self.correct_customer_list), 'The customer added successfully')
        self.length_after = len(self.bank_length_after.retrieve_customers() + 1)
        self.assertEqual(self.length_after, self.length_before)