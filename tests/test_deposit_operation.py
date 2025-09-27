import unittest
from unittest import mock
from bank.customer import Customer
from bank.account import Account
from bank.bank import Bank
import bank.customer_exceptions as customerExp
import bank.account_exceptions as accountExp

class TestDepositCheckingOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account1 = Account()
        self.customer1 = Customer()
        
        self.customer1.customer_id = '10002'
        self.customer1.password = 'idh36%@#FGd'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['100'])
    def test_correct_deposit_checking_operation(self, input):
        self.account1.deposit_operation(self.customer1.customer_id, '1')
    
    @mock.patch('builtins.input', side_effect=['-10'])
    def test_negative_deposit_checking_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account1.deposit_operation(self.customer1.customer_id, '1')        

    @mock.patch('builtins.input', side_effect=['hello'])
    def test_wrong_deposit_checking_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account1.deposit_operation(self.customer1.customer_id, '1')

class TestDepositSavingsOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account2 = Account()
        self.customer2 = Customer()
        
        self.customer2.customer_id = '10004'
        self.customer2.password = 'DEU8_qw3y72$'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['500'])
    def test_correct_deposit_savings_operation(self, input):
        self.account2.deposit_operation(self.customer2.customer_id, '2')
    
    @mock.patch('builtins.input', side_effect=['-100'])
    def test_negative_deposit_savings_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account2.deposit_operation(self.customer2.customer_id, '2')        

    @mock.patch('builtins.input', side_effect=['welcome'])
    def test_wrong_deposit_savings_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account2.deposit_operation(self.customer2.customer_id, '2')
            
class TestCreateSavingsAccount(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account3 = Account()
        self.customer3 = Customer()
        
        self.customer3.customer_id = '10001'
        self.customer3.password = 'juagw362'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['yes', '1000'])
    def test_correct_create_savings_operation(self, input):
        self.account3.deposit_operation(self.customer3.customer_id, '2')
    
    @mock.patch('builtins.input', side_effect=['yes', '-50'])
    def test_negative_create_savings_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account3.deposit_operation(self.customer3.customer_id, '2')        

    @mock.patch('builtins.input', side_effect=['yes', 'welcome'])
    def test_wrong_create_savings_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account3.deposit_operation(self.customer3.customer_id, '2')