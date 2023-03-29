from icon_utils import icon_service
from iconsdk.wallet.wallet import KeyWallet

# if you need you can create a new wallet
def create_new_wallet():
    password = input("\nEnter a password for your wallet: ")
    name = input("\nEnter a name for your wallet: ")
    
    _wallet = KeyWallet.create()
    _wallet.store(f'wallets/{name}', password)

    # print in red the file location and name
    print(f"\033[91mWallet file created at: wallets/{name}\033[0m")

# loads a wallet from the wallets/ folder
def load_wallet(name, password):
    _wallet = KeyWallet.load(f'wallets/{name}', password)
    return _wallet