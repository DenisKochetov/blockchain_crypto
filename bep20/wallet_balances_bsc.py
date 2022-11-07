# class AbstractContract is a template for any 
# EVM based contract and initializing with contract address and ABI.
# Address and ABI can be found on blockchain explorer such as https://etherscan.io

from abc import ABC
import sys
from web3 import Web3
import decimal
import argparse


# Binance Smart Chain http node provider
BSC = 'https://bsc-dataseed1.binance.org:443'


class AbstractContract(ABC):
    
    provider = None
    
    def __init__(self, address: str, ABI: str):
        
        if self.provider is not None:
            self.w3 = Web3(Web3.HTTPProvider(self.provider))
        else:
            raise ProviderInitException
        
        try:
            self.contract = self.w3.eth.contract(address, abi=ABI)
        except Exception as e:
            print(f'{e} in contract {address}')
    
    @property
    def address(self):
        return self.contract.address
    
    @property
    def abi(self):
        return self.contract.abi
        
    def get_functions_list(self) -> list:
        return self.contract.all_functions()

    
class BSCContract(AbstractContract):
    provider = BSC 
    # abi is a large text stored in a txt file
    with open('BEP20_abi.txt', 'r') as file:
      BEP20_ABI = file.read().replace('\n', '')

    def __init__(self, address: str, ABI: str=BEP20_ABI):
            
      if self.provider is not None:
          self.w3 = Web3(Web3.HTTPProvider(self.provider))
      else:
          raise ProviderInitException
      try:
            self.contract = self.w3.eth.contract(address, abi=ABI)
      except Exception as e:
            print(f'{e} in contract {address}')        
    
    def get_balance(wallet: str, self) -> decimal.Decimal:
      try:
        balance = self.contract.functions.balanceOf(wallet).call()
        balance = self.w3.fromWei(balance, 'ether')
      except Exception as e:
        print(f'{e} in contract {self}')    
        balance = None
      return balance

    def get_balance_formatted(balance: decimal.Decimal) -> str:
      try:
        return str(round(balance, 1))
      except:
          return "Balance not found"


# Parse arguments from console
def parse_data() -> str:
  parser = argparse.ArgumentParser()
  parser.add_argument("--wallet", "-w", help="input wallet")
  parser.add_argument("--token", "-t", help="token")

  args = parser.parse_args()

  return args.wallet, args.token



if __name__ == "__main__":

  wallet, token = parse_data()

  balance = BSCContract.get_balance_formatted(BSCContract.get_balance(wallet, BSCContract(token)))
  print(balance)
  

