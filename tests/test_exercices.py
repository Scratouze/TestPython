import string
import unittest
import random

from myBank import CheckingAccount, Account

if __name__ == '__main__':
    unittest.main()


class TestAccountCreation(unittest.TestCase):
    print("Avant tests")

    def setUp(self) -> None:
        str1 = string.ascii_lowercase
        str2 = string.ascii_lowercase
        self.CheckingAccount1 = CheckingAccount(random.choice(str1), random.choice(str2),
                                                random.randint(0, 10000))

    # def tearDown(self) -> None:
    #     self.CheckingAccount1.balance = -5

    def test_is_instance_of_account(self):
        self.assertIsInstance(self.CheckingAccount1, Account)

    def test_new_account_balance_is_positif(self):
        self.assertGreater(self.CheckingAccount1.balance, 100)

    def test_account_is_uniq(self):
        pass



