import requests

class TransactionTracker:
    def __init__(self, api_url):
        self.api_url = api_url
        self.transactions = []

    def fetch_transaction_data(self, wallet_address):
        # Fetch transaction data from the blockchain explorer API
        url = f"{self.api_url}/transactions/{wallet_address}"
        response = requests.get(url)
        if response.status_code == 200:
            self.transactions = response.json()
        else:
            print("Error fetching transaction data from the API.")

    def filter_transactions(self, start_date=None, end_date=None, minimum_amount=None):
        # Filter transactions based on specified criteria
        filtered_transactions = []

        for transaction in self.transactions:
            # Check transaction date
            if start_date and transaction['date'] < start_date:
                continue
            if end_date and transaction['date'] > end_date:
                continue

            # Check transaction amount
            if minimum_amount and transaction['amount'] < minimum_amount:
                continue

            filtered_transactions.append(transaction)

        self.transactions = filtered_transactions

    def process_transactions(self):
        balances = {}

        for transaction in self.transactions:
            wallet_address = transaction['wallet']
            amount = transaction['amount']

            # Update wallet balance
            if wallet_address not in balances:
                balances[wallet_address] = 0
            balances[wallet_address] += amount

        return balances

    def display_balances(self, balances):
        for wallet_address, balance in balances.items():
            print(f"Wallet: {wallet_address}")
            print(f"Balance: {balance}")
            print("-----------------")

# Example usage:

# Define API URL:
api_url = "https://api.example.com"

# Create an instance of TransactionTracker
tracker = TransactionTracker(api_url)

# Fetch transaction data for a wallet address
wallet_address = "0x1234567890abcdef"
tracker.fetch_transaction_data(wallet_address)

# Filter transactions based on criteria (optional)
start_date = "2022-01-01"
end_date = "2022-12-31"
minimum_amount = 10.0
tracker.filter_transactions(start_date, end_date, minimum_amount)

# Process transactions and calculate balances
balances = tracker.process_transactions()

# Display wallet balances
tracker.display_balances(balances)
