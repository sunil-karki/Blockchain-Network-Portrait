import csv
from web3 import Web3
from datetime import datetime

# Infura API key
API_KEY = "76d2fa7e008240c786855ac5d4b5e85e"
url = f"https://mainnet.infura.io/v3/{API_KEY}"

w3 = Web3(Web3.HTTPProvider(url))
isWeb3Connected = w3.is_connected()
print("isConnected: " + str(isWeb3Connected))

# Define the range of block numbers (you need to find the appropriate range)
start_block = 17140991  # Replace with the block number corresponding to the start date
end_block = 17140996    # Replace with the block number corresponding to the end date

# dt_object = datetime.fromtimestamp(1682640023)
# print(dt_object)

# Create a CSV file to store transactions
csv_file_path = "/home/sunilkarki/Documents/Persn/CProj/bnp/data/transactions.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["Block Number", "Transaction Hash", "From", "To", "Value (ETH)", "Timestamp"])

    # Iterate through the range of blocks
    for block_number in range(start_block, end_block + 1):
        block = w3.eth.get_block(block_number)

        block_transaction_timestamp = block['timestamp']

        # Iterate through transactions in the block
        for tx_hash in block['transactions']:
            tx = w3.eth.get_transaction(tx_hash)

            # value_wei = tx['value']
            value_eth = tx['value']
            if value_eth == 0:
                continue

            from_address = tx['from']
            to_address = tx['to']

            timestamp = datetime.fromtimestamp(block_transaction_timestamp)

            # Write transaction data to CSV file
            writer.writerow([block_number, tx_hash.hex(), from_address, to_address, value_eth, timestamp])

print(f"Transactions archived")