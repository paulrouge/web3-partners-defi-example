from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction

def balanced_swap():
    # Generates an instance of transaction for the calling method in SCORE.
    transaction = CallTransactionBuilder()\
        .from_(wallet.get_address())\
        .to("cx00...02")\
        .step_limit(1000000)\
        .nid(3)\
        .nonce(100)\
        .method("transfer")\
        .params(params)\
        .build()