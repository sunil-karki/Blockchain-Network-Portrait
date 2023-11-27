import csv
from web3 import Web3

# Infura API key
API_KEY = "76d2fa7e008240c786855ac5d4b5e85e"
url = f"https://mainnet.infura.io/v3/{API_KEY}"

w3 = Web3(Web3.HTTPProvider(url))
isWeb3Connected = w3.is_connected()
print("isConnected: " + str(isWeb3Connected))

# Define the range of block numbers (you need to find the appropriate range)
start_block = 17140930  # Replace with the block number corresponding to the start date
end_block = 17140932    # Replace with the block number corresponding to the end date

# Create a CSV file to store transactions
csv_file_path = "/home/sunilkarki/Documents/Persn/CProj/bnp/data/transactions.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["Block Number", "Transaction Hash", "From", "To", "Value (ETH)"])

    # Iterate through the range of blocks
    for block_number in range(start_block, end_block + 1):
        block = w3.eth.get_block(block_number)

        # Iterate through transactions in the block
        for tx_hash in block['transactions']:
            tx = w3.eth.get_transaction(tx_hash)
            from_address = tx['from']
            to_address = tx['to']
            # value_wei = tx['value']
            value_eth = tx['value']

            # Write transaction data to CSV file
            writer.writerow([block_number, tx_hash.hex(), from_address, to_address, value_eth])

print(f"Transactions archived")