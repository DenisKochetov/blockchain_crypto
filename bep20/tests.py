import unittest
from wallet_balances_bsc import BSCContract

class TestBalance(unittest.TestCase):

    def test_bad_token(self):
        wallet = "0xc36E54d8313d76168c823BF44cB72e46020DbF73"
        token = "0x"
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), 'Balance not found')

    def test_bad_wallet(self):
        wallet = "0xbF73"
        token = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"        
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), 'Balance not found')

    def test_original(self):
        wallet = "0xc36E54d8313d76168c823BF44cB72e46020DbF73"
        token = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), '136.6')

    def test_mist(self):
        wallet = "0xc36E54d8313d76168c823BF44cB72e46020DbF73"
        token = "0x68E374F856bF25468D365E539b700b648Bf94B67"
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), '20674.6')
    
    def test_argon(self):
        wallet = "0xc36E54d8313d76168c823BF44cB72e46020DbF73"
        token = "0x851F7a700c5d67DB59612b871338a85526752c25"
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), '1.6')
        

    def test_angel_swap(self):
        wallet = "0xc36E54d8313d76168c823BF44cB72e46020DbF73"
        token = "0x347Af9141A19f2d4B0c03187c15733De107Be085"
        self.assertEqual(BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token))), '5570987.2')
    

if __name__ == '__main__':
    unittest.main()