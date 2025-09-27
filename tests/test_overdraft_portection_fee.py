import unittest
from bank.customer import Customer
from bank.bank import Bank

class TestOverDaraftFee(unittest.TestCase):
    def setUp(self):
        print('Setting Up')
        self.bank1 = Bank()
        self.customer1 = Customer()
        
        self.customer1.customer_id = '10002'
        self.customer1.password = 'idh36%@#FGd'
        
    def tearDown(self):
        print('Tearing down')
        
    def test_first_overdraft(self):
        self.assertEqual(self.bank1.overdraft_protection_fee(self.customer1.customer_id, '50'), True)

    def test_second_overdraft(self):
        self.assertEqual(self.bank1.overdraft_protection_fee(self.customer1.customer_id, '10'), True)
        
    def test_third_overdraft(self):
        self.assertEqual(self.bank1.overdraft_protection_fee(self.customer1.customer_id, '20'), False)

    def test_account_reactivate(self):
        self.assertEqual(self.bank1.activate_customer(self.customer1.customer_id, '140'), True)