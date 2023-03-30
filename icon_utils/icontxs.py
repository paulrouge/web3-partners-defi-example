from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from icon_utils import icon_service, balanced_dex

# make sure to send a wallet object as parameter, this is used to sign the transaction
def balanced_swap(wallet):
    
    # for clearity, the method and params are defined in separate variables
    method = "method_to_call"
    params = {}

    # Generates an instance of transaction for the calling method in SCORE.
    transaction = CallTransactionBuilder()\
        .from_(wallet.get_address())\
        .to(balanced_dex)\
        .step_limit(1000000)\
        .nid(1)\
        .nonce(100)\
        .method(method)\
        .params(params)\
        .build()

    # Returns the signed transaction object having a signature
    signed_transaction = SignedTransaction(transaction, wallet)

    # Sends the transaction
    tx_hash = icon_service.send_transaction(signed_transaction)

    print(f"tx_hash: {tx_hash}")
