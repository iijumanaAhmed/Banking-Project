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
        self.bank = Bank()
        
        self.correct_customer.customer_id = '10002'
        self.correct_customer.password = 'idh36%@#FGd'

        self.wrong1_customer.customer_id = '1000'
        self.wrong1_customer.password = 'idh36%@#FGd'
        
        self.correct_customer.customer_id = '10002'
        self.correct_customer.password = '1234'

    def tearDown(self):
        print('Tearing down')
        
    def test_add_customer(self):
        
        with self.assertRaises(accountExp.AccountCreationError):
            self.correct_customer.login_customer()
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