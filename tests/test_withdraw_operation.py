import unittest
from unittest import mock
from bank.customer import Customer
from bank.account import Account
from bank.bank import Bank
import bank.customer_exceptions as customerExp
import bank.account_exceptions as accountExp

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
    @mock.patch('builtins.input', side_effect=['100'])
    def test_correct1_withdraw_operation(self, input):
        self.account1.withdraw_operation(self.customer1.customer_id, '1')
    
    @mock.patch('builtins.input', side_effect=['-10'])
    def test_negative1_withdraw_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account1.withdraw_operation(self.customer1.customer_id, '1')        

    @mock.patch('builtins.input', side_effect=['hello'])
    def test_wrong1_withdraw_operation(self, input):
        with self.assertRaises(StopIteration):
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
        
    @mock.patch('builtins.input', side_effect=['50'])
    def test_correct2_withdraw_operation(self, input):
        self.account2.withdraw_operation(self.customer2.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['200'])
    def test_over100_withdraw_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account2.withdraw_operation(self.customer2.customer_id, '1')
    
    @mock.patch('builtins.input', side_effect=['-10'])
    def test_negative2_withdraw_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account2.withdraw_operation(self.customer2.customer_id, '1')        

    @mock.patch('builtins.input', side_effect=['hello'])
    def test_wrong2_withdraw_operation(self, input):
        with self.assertRaises(StopIteration):
            self.account2.withdraw_operation(self.customer2.customer_id, '1')      


# TEST CASES FOR customer with deactive accounts
class TestWithdrawOperationDeactive(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.account3 = Account()
        self.customer3 = Customer()
        self.account4 = Account()
        self.customer4 = Customer()

        # customer with customer with deactive accounts
        self.customer3.customer_id = '10004'
        self.customer3.password = 'DEU8_qw3y72$'
        self.customer4.customer_id = '10005'
        self.customer4.password = 'd^dg23g)@'
        
    def tearDown(self):
        print('Tearing down')
    
    @mock.patch('builtins.input', side_effect=['yes','0'])
    def test_activate_with_zero_withdraw(self, input):
        with self.assertRaises(StopIteration):
            self.account3.withdraw_operation(self.customer3.customer_id, '1')
    
    @mock.patch('builtins.input', side_effect=['yes','50'])
    def test_activate_with_lower_withdraw(self, input):
        self.account3.withdraw_operation(self.customer3.customer_id, '1')
            
    @mock.patch('builtins.input', side_effect=['yes','120'])
    def test_activate_with_accepted_withdraw(self, input):
        with self.assertRaises(StopIteration):
            self.account3.withdraw_operation(self.customer3.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['no'])
    def test_no_activate_withdraw(self, input):
        self.account4.withdraw_operation(self.customer4.customer_id, '1')

    @mock.patch('builtins.input', side_effect=['Hi'])
    def test_wrong_activate_withdraw(self, input):
        with self.assertRaises(StopIteration):
            self.account4.withdraw_operation(self.customer4.customer_id, '1')