import unittest
from bank.account import Account
import bank.account_exceptions as accountExp

class TestCreateCheckingAccount(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.logged_customer = Account()
        
    def tearDown(self):
        print('Tearing down')
        
    def test_create_checking_account(self):
        self.assertEqual(self.logged_customer.create_checking_account(500), 500)
        with self.assertRaises(accountExp.AccountCreationError):
            self.logged_customer.create_checking_account(-10)
        with self.assertRaises(accountExp.AccountCreationError):
            self.logged_customer.create_checking_account('hello')
