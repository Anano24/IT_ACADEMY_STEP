import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Setting up two bank accounts for testing
        self.account1 = BankAccount("11111", "John", 0)
        self.account2 = BankAccount("22222", "Jackson", 100)

    
    def test_deposit(self):
        # Testing deposit functionality
        # Ensure depositing positive amounts updates balance correctly
        self.assertEqual(self.account1.deposit(500), "Deposited $500. New balance: $500")
        self.assertEqual(self.account2.deposit(1000), "Deposited $1000. New balance: $1100")
        # Ensure depositing negative amounts returns appropriate error message
        self.assertEqual(self.account1.deposit(-100), "Invalid amount for deposit.")
        # Ensure depositing zero returns appropriate error message
        self.assertEqual(self.account2.deposit(0), "Invalid amount for deposit.")


    def test_withdraw(self):
        self.assertEqual(self.account1.withdraw(100), "Insufficient funds or invalid amount for withdrawal.")
        # Deposit to account1 to enable withdrawals
        self.account1.deposit(1000)
        # Ensure withdrawing within balance updates balance correctly
        self.assertEqual(self.account1.withdraw(450), "Withdrew $450. New balance: $550")
        self.assertEqual(self.account1.withdraw(600), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account1.withdraw(400), "Withdrew $400. New balance: $150")
        self.assertEqual(self.account1.withdraw(-100), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account1.withdraw(0), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account2.withdraw(100), "Withdrew $100. New balance: $0")


    def test_display_balance(self):
        # Testing display balance functionality
        # Ensure initial balances are displayed correctly
        self.assertEqual(self.account1.display_balance(), "Current Balance: $0")
        self.assertEqual(self.account2.display_balance(), "Current Balance: $100")
        # Deposit to account1 and withdraw from account2 to check updated balances
        self.account1.deposit(500)
        self.account1.deposit(110)
        self.account2.withdraw(50)
        # Ensure balances are displayed correctly after transactions
        self.assertEqual(self.account1.display_balance(), "Current Balance: $610")
        self.assertEqual(self.account2.display_balance(), "Current Balance: $50")
        



if __name__ == "__main__":
    unittest.main()


        
