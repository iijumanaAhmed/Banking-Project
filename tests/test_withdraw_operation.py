import unittest
from unittest import mock
from bank.customer import Customer
from bank.account import Account

# TEST CASES FOR customer with positive checking balance
class TestCorrectWithdrawCheckingOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account1 = Account()
        self.customer1 = Customer()
        
        # customer with positive checking balance
        self.customer1.customer_id = '10002'
        self.customer1.password = 'idh36%@#FGd'
        
    def tearDown(self):
        print('Tearing down')
        
    #  input mock resource: https://www.youtube.com/watch?v=aoW5mpDg5Os
    @mock.patch('builtins.input', side_effect=['0', 'no', '0', 'no', '0'])
    def test_withdraw1_checking_operation(self, input):
        self.account1.withdraw_operation(self.customer1.customer_id, '1')
    
    @mock.patch('builtins.input', side_effect=['hello', 'yes', '0', 'no', '0'])
    def test_withdraw2_checking_operation(self, input):
        self.account1.withdraw_operation(self.customer1.customer_id, '1')        

    @mock.patch('builtins.input', side_effect=['-5','yes', '100', 'yes', '100'])
    def test_withdraw3_checking_operation(self, input):
        self.account1.withdraw_operation(self.customer1.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['10', 'no', '0', 'yes', '0'])
    def test_withdraw4_checking_operation(self, input):
        self.account1.withdraw_operation(self.customer1.customer_id, '1')     
    
    
# TEST CASES FOR customer with negative checking balance
class TestErrorWithdrawCheckingOperation(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account2 = Account()
        self.customer2 = Customer()

        # customer with negative checking balance
        self.customer2.customer_id = '10003'
        self.customer2.password = 'uYWE732g4ga1'

    def tearDown(self):
        print('Tearing down')
        
    @mock.patch('builtins.input', side_effect=['hello', 'no', '0', 'no', '0'])
    def test_withdraw1_savings_operation(self, input):
        self.account2.withdraw_operation(self.customer2.customer_id, '2')
    
    @mock.patch('builtins.input', side_effect=['0', 'yes', '0', 'no', '0'])
    def test_withdraw2_savings_operation(self, input):
        self.account2.withdraw_operation(self.customer2.customer_id, '2')        

    @mock.patch('builtins.input', side_effect=['10','yes', '100', 'yes', '100'])
    def test_withdraw3_savings_operation(self, input):
        self.account2.withdraw_operation(self.customer2.customer_id, '2')
            
    @mock.patch('builtins.input', side_effect=['-5', 'no', '0', 'yes', '0'])
    def test_withdraw4_savings_operation(self, input):
        self.account2.withdraw_operation(self.customer2.customer_id, '2')    