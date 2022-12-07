import json

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer


class Wallet:
    def __init__(private_key=None, network='devnet'):
        self.solana_client = Client(f"https://api.{network}.solana.com")
        self.private_key = private_key
