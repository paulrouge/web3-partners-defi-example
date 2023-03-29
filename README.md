# code example Web3 Partners meet up 30-03-2022

Some snippets of code that interact with the Icon blockchain.

## What's happening
- in icon_utils/__init__.py there are some things declared that are used in the other files.
- in icon_utils/iconcalls.py there are some functions that call the blockchain / a smart contract on the blockchain. 

## How to use
- pip install iconsdk
- if you want to sign txs place your keystore file in the wallets directory, or
- create a new keystore file by importing 'create_new_wallet':

```python
from icon_utils.wallets import create_new_wallet
create_new_wallet()
```

You will be asked a password and a name for the keystore file. The keystore file will be saved in the wallets directory.


more info on the icon-sdk: (https://docs.icon.community/icon-stack/client-apis/python-sdk)[https://docs.icon.community/icon-stack/client-apis/python-sdk]