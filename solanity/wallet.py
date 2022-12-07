import json

from typing import Union

from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer


class Wallet:
    def __init__(self, private_key=None,
                       public_key=None,
                       address=None,
                       network='devnet') -> None:

        self.solana_client = Client(f"https://api.{network}.solana.com")
        self.private_key = private_key
        self.public_key = public_key
        self.address = address

    def open(self) -> None:
        if self.private_key:
            kp = Keypair.from_secret_key(self.private_key)

            self.address = str(kp.public_key)
            self.public_key = kp.public_key
            self.private_key = kp.secret_key

    def create(self) -> None:
        kp = Keypair.generate()

        self.address = str(kp.public_key)
        self.public_key = kp.public_key
        self.private_key = kp.secret_key

    def balance(self) -> str:
        response = self.solana_client.get_balance(self.address)
        balance = response['result']['value'] / 1000000000

        return str(balance)

    def request(self, amount) -> Union[str, None]:
        amount = int(1000000000 * amount)
        response = self.solana_client.request_airdrop(
            self.address, amount)
        transaction_id = response['result']
        return transaction_id

    def send(self, receiver, amount) -> Union[str, None]:
        sender = Keypair.from_secret_key(self.private_key)
        amount = int(1000000000 * amount)

        txn = Transaction().add(transfer(TransferParams(
            from_pubkey=sender.public_key, to_pubkey=PublicKey(receiver), lamports=amount)))
        response = solana_client.send_transaction(txn, sender)

        transaction_id = response['result']
        return transaction_id
