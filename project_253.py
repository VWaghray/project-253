# --------------253 Proj----------------
from web3 import Web3
import time


ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x92Bb7244b9A007d19580bD1d2595C00ea3F0AFa7'
James_account = '0x1085cd9899928eFEe7117B927D4C99402086D326'
Ryan_account  = '0x6b3Ae215e5c7A07701F8ae4f4d657EA109977037'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(10, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x2585c75c068dca361556e5b23342b2eabdaf5f5fd6bb7d630456dd1a76a921a2'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
print('Wait for few seconds Transaction is in progress...')
time.sleep(5)
# -----------------




nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei(5, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0xfa15f5356d8d89a5cd5e2ae420cdbc4bf332dbee9cefbb7847f8f8a49c82c3ed'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))



