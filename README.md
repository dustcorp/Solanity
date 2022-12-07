# Solanity

Solanity is a Python3 library for managing Solana wallet.

```python3
from solanity.wallet import Wallet

wallet = Wallet(network='testnet')
wallet.create()

print(wallet.balance())
```
