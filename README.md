# code example Web3 Partners meet up 30-03-2022

Some snippets of code that interact with the Icon blockchain.

## What's happening
- in icon_utils/__init__.py there are some things declared that are used in the other files.
- in icon_utils/iconcalls.py there are some functions that call the blockchain / a smart contract on the blockchain. 
- in icon_utils/icontxs.py there are some functions that create and sign transactions.

_note: the code in icon_utils is custom made, it is not part of the icon-sdk_

## How to use
- pip install iconsdk

In call.py you can find some examples of how to call the blockchain, at icon_utils/iconcalls.py you can take a look at how the functions work.

some examples:
    
```python
    from icon_utils.iconcalls import print_latest_block
    from icon_utils.iconcalls import print_transactions_from_block
    from icon_utils.iconcalls import print_balanced_price

    print_latest_block()
    print_transactions_from_block(63762860, clean_output=False) # set to True to have cleaner output

    # pick pool id from the contract (see tracker link below), in this case we use pool id 3
    print_balanced_price(3)


    # Often text is converted to so called 'hex' format. Use function below to convert back to text.

    # hexstring = '0x7b226d6574686f64223a225f7374616b65227d' # replace with your hexstring
    # print(bytes.fromhex(hexstring[2:]).decode('utf-8'))
```

- if you want to sign txs place your keystore file in the wallets directory, or
- create a new keystore file by importing the 'create_new_wallet' function.

You will be asked a password and a name for the keystore file. The keystore file will be saved in the wallets directory.

If you already have a keystore file, you can load it by importing the 'load_wallet' function.

```python
    from icon_utils.wallets import create_new_wallet

    # create new wallet
    create_new_wallet()

    # or load from /wallets folder
    wallet = load_wallet('wallet_name', 'password')
```







more info on the icon-sdk: https://docs.icon.community/icon-stack/client-apis/python-sdk