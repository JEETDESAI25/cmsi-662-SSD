import sqlite3  # Import the sqlite3 module for working with SQLite databases
from passlib.hash import (
    pbkdf2_sha256,
)  # Import the pbkdf2_sha256 module for password hashing


def create_accounts_table():
    """
    This script creates an SQLite database table named "accounts" and inserts data into it.

    The "accounts" table has the following columns:
    - id: Account number (text)
    - owner: User email (text)
    - balance: Account balance (integer)

    The script connects to the SQLite database file named "storage.db", creates the "accounts" table,
    and inserts sample data into it.

    Note: The "accounts" table has a foreign key constraint that references the "users" table on the "owner" column.

    Usage:
    - Run this script to create the "accounts" table and insert data into it.

    Dependencies:
    - sqlite3: Python module for working with SQLite databases
    - passlib.hash: Python module for password hashing

    Returns:
    - None
    """
    # Connect to the SQLite database file named "storage.db"
    con = sqlite3.connect("storage.db")

    con.execute("PRAGMA foreign_keys = ON")

    # Create a cursor object to execute SQL statements
    cur = con.cursor()

    # Execute a SQL statement to create the "accounts" table
    cur.execute(
        """
        CREATE TABLE accounts (
            id text primary key, owner text, balance integer,
            foreign key(owner) references users(email)
        )"""
    )

    # Execute SQL statements to insert data into the "accounts" table
    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)", ("100", "alice@example.com", 7500)
    )
    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)", ("190", "alice@example.com", 200)
    )
    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)", ("998", "bob@example.com", 1000)
    )
    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)", ("500", "charlie@example.com", 101)
    )
    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)", ("502", "diana@example.com", 501)
    )

    # Commit the changes to the database
    con.commit()

    # Close the database connection
    con.close()


# Run the function to create the accounts table and insert data
create_accounts_table()
