"""
This module provides functions for handling user accounts, such as retrieving account balances and performing transfers.

The module interacts with a SQLite database named 'storage.db' that contains a table named 'accounts' with the following columns:
- id: The unique identifier of the account.
- owner: The owner of the account.
- balance: The current balance of the account.

Note: This module assumes that the 'storage.db' database file exists and is properly configured.
"""

import sqlite3


# It handles user's account such as getting the balance and doing the transfer
# The function gets the balance of logged in user from the database bank of the table named accounts
def get_balance(account_number, owner):
    try:
        con = sqlite3.connect("storage.db")
        cur = con.cursor()
        cur.execute(
            """
            SELECT balance FROM accounts where id=? and owner=?""",
            (account_number, owner),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return row[0]
    finally:
        con.close()


# Transfer the amount from the source account to target account and updates it to the bank database


def do_transfer(source, target, amount):
    """
    Transfer a specified amount from the source account to the target account.

    Args:
        source (int): The ID of the source account.
        target (int): The ID of the target account.
        amount (float): The amount to be transferred.

    Returns:
        bool: True if the transfer is successful, False otherwise.
    """
    try:
        # Connect to the SQLite database
        con = sqlite3.connect("storage.db")
        cur = con.cursor()

        # Check if the target account exists
        cur.execute("SELECT id FROM accounts WHERE id=?", (target,))
        row = cur.fetchone()
        if row is None:
            return False

        # Deduct the amount from the source account
        cur.execute(
            "UPDATE accounts SET balance=balance-? WHERE id=?", (amount, source)
        )

        # Add the amount to the target account
        cur.execute(
            "UPDATE accounts SET balance=balance+? WHERE id=?", (amount, target)
        )

        # Commit the changes to the database
        con.commit()
        return True

    finally:
        # Close the database connection
        con.close()
