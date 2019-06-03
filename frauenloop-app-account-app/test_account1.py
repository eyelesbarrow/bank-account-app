import unittest
from account1 import Account


class TestAccount1(unittest.TestCase):


    def test_display_balance_user1(self):
        user = '1234'
        self.assertEqual(user, '1234')

    def test_display_balance_user2(self):
        user2= '4212'
        self.assertEqual(user2, user2)

    def test_display_balance(self):
        pin_number = 'abc'
        user_name = 'user1'
        Account(pin_number,user_name)

if __name__ == '__main__':
    unittest.main()


