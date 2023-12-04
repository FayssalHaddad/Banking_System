# Object-Oriented Programming Project in Python

## Description
This project is a Python-based object-oriented programming exercise that simulates a basic banking system. It allows the creation of bank accounts, handling deposits, withdrawals, and inter-account transactions. The system also demonstrates the dynamic categorization of accounts based on balance and applies specific interest rates.

## Features
- **Account Creation**: Enables the creation of bank accounts with an initial balance and a name.
- **Account Type Management**: Accounts are categorized into different types (Silver, Golden, White) based on their balance.
- **Transactions**: Facilitates transactions between accounts with a transaction fee.
- **Deposits and Withdrawals**: Functions to deposit or withdraw money from an account.
- **Benefits Based on Account Type**: Applies different interest rates based on the account type on a specific date.

## Technologies Used
- Python
- Python's datetime module for date handling

## Notes

This project is a demonstration exercise and should not be used as a real banking system.
No database or data persistence is involved; accounts and transactions are only stored in memory during the program execution.

## Example of Usage for banking transactions
```python
Account1 = BankAccount(15000, "Fayssal")
Account2 = BankAccount(100000, "John")
Account1.withdraw(2000)
Account1.account_type()
Account2.account_type()

