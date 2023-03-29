from icon_utils import icon_service, balanced_dex
from iconsdk.builder.call_builder import CallBuilder
import json

def print_latest_block():
    print('\n------------------------------------------------------------------------------------------------------------')
    
    block = icon_service.get_block("latest")
    
    for key, value in block.items():
        # print both, but the key in yellow and the value in blue
        print(f'\033[93m{key}\033[0m: \033[94m{value}\033[0m')
    
    print('------------------------------------------------------------------------------------------------------------\n')

def print_transactions_from_block(block_number, clean_output=False):
    print('\n------------------------------------------------------------------------------------------------------------')
    
    block = icon_service.get_block(block_number)
    
    for transaction in block['confirmed_transaction_list']:
        if clean_output:
            try:
                # transaction to json format
                transaction = json.dumps(transaction, indent=4) 

                # we want the 'data' 
                data = json.loads(transaction)['data']

                # print all keys and values in data, keys in yellow and values in blue
                for key, value in data.items():
                    print(f'\033[93m{key}\033[0m: \033[94m{value}\033[0m')
                
                # a new line to separate the transactions
                print('\n')
            except:
                pass
        else:
            print('\n')
            print(f'\033[93m{transaction}\033[0m')
    
    print('------------------------------------------------------------------------------------------------------------\n')



def print_balanced_price(pool_id):
    print('\n------------ price from balanced --------------')
    
    # Generates a call instance using the CallBuilder
    call = CallBuilder()\
        .from_('hx0000000000000000000000000000000000000000')\
        .to(balanced_dex)\
        .method("getBasePriceInQuote")\
        .params({"_id": hex(pool_id)})\
        .build()

    # Executes a call method to call a read-only API method on the SCORE immediately without creating a transaction on Loopchain
    result = icon_service.call(call)

    # result is now a hex string, that's how it's returned from the blockchain
    print(result)

    # convert hex string to int
    # result = int(result, 16)
    # print(result)

    # result now is multiplied by 10**18, so we need to divide it by 10**18 to get the actual price
    # result = result / 10**18
    
    # print result as int in yellow
    # print(f'\033[93m{result}\033[0m')

    print('-----------------------------------------------\n')