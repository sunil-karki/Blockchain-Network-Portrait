###########################################################################
# File: To acquire blockchain data
###########################################################################
import json

from web3 import Web3

# Infura API key
API_KEY = "76d2fa7e008240c786855ac5d4b5e85e"
# change endpoint to mainnet or ropsten or any other of your account
url = f"https://mainnet.infura.io/v3/{API_KEY}"

w3 = Web3(Web3.HTTPProvider(url))
isWeb3Connected = w3.is_connected()
print("isConnected: " + str(isWeb3Connected))

# Get the latest block
# latest = w3.eth.get_block('latest')
# print("Latest block:")
# print(latest)
# print(latest['number'])
# print(latest['parentHash'].hex())

# Get a random block
randNumber = 17140930
blockNumber = randNumber
randBlock = w3.eth.get_block(randNumber)
print(randBlock)
print("Block Hash Number: " + randBlock.get('hash').hex())
print("Block Number: " + str(randBlock.get('number')))
print("-----------------------------------------------------------\n")

# Get information about a particular transaction:
transaction1 = w3.eth.get_transaction('0xb0cedc0efd0baf55254296a3c25096ed5e0b4152c7d305d3d3ea33b4c30e8745')
print("Info on a transaction:")
print(w3.to_json(transaction1))
print("-----------------------------------------------------------\n")

# Query the transaction using block number
transaction2 = w3.eth.get_transaction_by_block(randNumber, 0)
print("Get transaction from a block number:")
print(transaction2)
print("-----------------------------------------------------------\n")

# Get the number of transactions for an address in a block ('from/to address', block number)
transactionCount = w3.eth.get_transaction_count('0x6b75d8AF000000e20B7a7DDf000Ba900b4009A80')
print("Number of transaction in a block")
print(transactionCount)
# 299850 0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13
print("-----------------------------------------------------------\n")

# Check if the address(from/to) in transactions is correct
isValid = w3.is_address('0x6b75d8AF000000e20B7a7DDf000Ba900b4009A80')
print("Check if address in transaction is correct")
print(isValid)
print("-----------------------------------------------------------\n")

# balance = w3.eth.get_balance('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')
# print(balance)