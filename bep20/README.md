# BEP20_web3
The wallet_balances_bsc.py script allows you to get the balance of the BEP20 token in the selected wallet.

Interaction:

Input: python3 wallet_balances_bsc.py --wallet={wallet} --token={token}

Output: decimal value in eth or "Balance not found"

Examples:

Input: python3 wallet_balances_bsc.py --wallet=0xc36E54d8313d76168c823BF44cB72e46020DbF73 --token=0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d

Output: 136.6

Input: python3 wallet_balances_bsc.py --wallet=0xc36E54d8313d76168c823BF44cB72e46020DbF73 --token=0x68E374F856bF25468D365E539b700b648Bf94B67

Output: 20674.6
