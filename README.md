# Transaction Tracker
A program that tracks and analyzes cryptocurrency transactions to monitor wallet balances and transaction history.

__1. Data Retrieval:__

 - The fetch_transaction_data method fetches transaction data from the blockchain explorer API using the provided wallet address and stores it in the self.transactions list.
   

__2. Transaction Filtering:__

 - The filter_transactions method filters transactions based on optional criteria such as start date, end date, and minimum amount. Transactions that meet the specified criteria are retained, and the filtered transactions are stored in the self.transactions list.
   

__3. Transaction Processing:__

The process_transactions method processes the filtered transactions and calculates wallet balances. It iterates through each transaction, updates the balances dictionary accordingly, and returns the calculated balances.

__4. Displaying Balances:__

The display_balances method displays the calculated wallet balances.
