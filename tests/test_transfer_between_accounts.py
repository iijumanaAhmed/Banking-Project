import unittest
from unittest import mock
from bank.customer import Customer
from bank.account import Account

class TestTransferFromCheckingOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account1 = Account()
        self.customer1 = Customer()
        
        self.customer1.customer_id = '10002'
        self.customer1.password = 'idh36%@#FGd'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['hello', 'no', '0', 'no', '0'])
    def test_1_transfer_from_checking_operation(self, input):
            self.account1.transfer_between_accounts(self.customer1.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['0', 'yes', '0', 'no', '0'])
    def test_2_transfer_from_checking_operation(self, input):
        self.account1.transfer_between_accounts(self.customer1.customer_id, '1')
        
    @mock.patch('builtins.input', side_effect=['yes', '100', 'yes', '100'])
    def test_3_transfer_from_checking_operation(self, input):
        self.account1.transfer_between_accounts(self.customer1.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['-5', 'no', '0', 'yes', '0'])
    def test_4_transfer_from_checking_operation(self, input):
            self.account1.transfer_between_accounts(self.customer1.customer_id, '1')

class TestTransferFromSavingsOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account2 = Account()
        self.customer2 = Customer()
        
        self.customer2.customer_id = '10004'
        self.customer2.password = 'DEU8_qw3y72$'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['hello', 'no', '0', 'no', '0'])
    def test_1_transfer_from_savings_operation(self, input):
            self.account2.transfer_between_accounts(self.customer2.customer_id, '2') 
                
    @mock.patch('builtins.input', side_effect=['0', 'yes', '0', 'no', '0'])
    def test_2_transfer_from_savings_operation(self, input):
        self.account2.transfer_between_accounts(self.customer2.customer_id, '2')     
            
    @mock.patch('builtins.input', side_effect=['yes', '100', 'yes', '100'])
    def test_3_transfer_from_savings_operation(self, input):
        self.account2.transfer_between_accounts(self.customer2.customer_id, '2')        

    @mock.patch('builtins.input', side_effect=['-5', 'no', '0', 'yes', '0'])
    def test_4_transfer_from_savings_operation(self, input):
        self.account2.transfer_between_accounts(self.customer2.customer_id, '2')