import sys
import argparse

from pymaker.keys import register_key
from web3 import Web3, HTTPProvider
from pymaker import Address

class TxMonitor:
    def __init__(self, args: list):

        parser = argparse.ArgumentParser(prog='tx_monitor')

        parser.add_argument("--web3-address", type=str)
        parser.add_argument("--eth-from", type=str)
        parser.add_argument("--eth-key", type=str)

        self.arguments = parser.parse_args(args)

        self.web3 = Web3(HTTPProvider(endpoint_uri=f"http://{self.arguments.web3_address}"))
        self.web3.eth.defaultAccount = self.arguments.eth_from
        self.our_address = Address(self.arguments.eth_from)
        register_key(self.web3, self.arguments.eth_key)

    def main(self):
        print(f'sync - {self.web3.eth.blockNumber}')
        print(self.web3.txpool.__dict__)



if __name__ == '__main__':
    TxMonitor(sys.argv[1:]).main()
