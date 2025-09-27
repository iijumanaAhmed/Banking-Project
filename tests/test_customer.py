import unittest
from bank.customer import Customer
from bank.account import Account
from bank.bank import Bank
import bank.customer_exceptions as customerExp

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
        self.correct_customer.checking_balance = 100
        self.correct_customer.savings_balance = 500
        self.correct_customer.active_status = 'active'
        self.correct_customer.overdraft_attempt = 0
        
        self.correct_customer_list = [self.correct_customer.customer_id, self.correct_customer.fname, self.correct_customer.lname, self.correct_customer.password, self.correct_customer.checking_balance, self.correct_customer.savings_balance, self.correct_customer.active_status, self.correct_customer.overdraft_attempt]
        self.wrong_customer_list = [self.correct_customer.customer_id, self.correct_customer.fname, self.correct_customer.lname, self.correct_customer.checking_balance, self.correct_customer.savings_balance, self.correct_customer.active_status, self.correct_customer.overdraft_attempt]
        
    def tearDown(self):
        print('Tearing down')
        
    def test_add_customer(self):
        self.assertEqual(self.correct_customer.fname, 'Jumana')        
        self.assertEqual(self.correct_customer.lname, 'Khawaji')
        self.assertEqual(self.correct_customer.checking_balance, 100)
        self.assertEqual(self.correct_customer.savings_balance, 500)
        self.assertEqual(self.correct_customer.active_status, 'active')
        self.assertEqual(self.correct_customer.overdraft_attempt, 0)
        
        with self.assertRaises(customerExp.AddCustomerError):
            self.wrong1_customer.add_customer(self.wrong_customer_list)

        self.length_before = len(self.bank_length_before.retrieve_customers())
        self.assertEqual(self.correct_customer.add_customer(self.correct_customer_list), True)
        self.length_after = len(self.bank_length_after.retrieve_customers())
        self.assertEqual(self.length_after, self.length_before + 1)
        
class TestLoginCustomer(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.correct_customer = Customer()
        self.wrong1_customer = Customer()
        self.wrong2_customer = Customer()
        
        self.correct_customer.customer_id = '10002'
        self.correct_customer.password = 'idh36%@#FGd'

        self.wrong1_customer.customer_id = 1000
        self.wrong1_customer.password = 'idh36%@#FGd'

        self.wrong2_customer.customer_id = '10002'
        self.wrong2_customer.password = '1234'
        
    def tearDown(self):
        print('Tearing down')
        
    def test_login_customer(self):
        self.assertEqual(self.correct_customer.login_customer(self.correct_customer.customer_id, self.correct_customer.password), True)        
        self.assertEqual(self.wrong1_customer.login_customer(self.wrong1_customer.customer_id, self.wrong1_customer.password), False)        
        self.assertEqual(self.wrong2_customer.login_customer(self.wrong2_customer.customer_id, self.wrong2_customer.password), False)        
