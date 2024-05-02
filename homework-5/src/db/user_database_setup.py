"""
This file, user_database_setup.py, contains a function to set up a user database.

The function `setup_user_database()` creates a table called 'users' in the database and inserts sample data for two users: Alice and Bob.

Usage:
- Import the `setup_user_database` function from this module.
- Call the function to set up the user database.

Example:
    setup_user_database()
"""

import sqlite3
from passlib.hash import pbkdf2_sha256


def setup_user_database():
    """
    This function sets up a user database by creating a table and inserting sample data.

    The table 'users' has three columns: email, name, and password.
    The email column is the primary key.
    The name column stores the user's name.
    The password column stores the hashed password using pbkdf2_sha256 algorithm.

    Sample data is inserted into the table for two users: Alice and Bob.

    Returns:
        None
    """
    con = sqlite3.connect("src/storage.db")
    cur = con.cursor()

    # Create the 'users' table
    cur.execute(
        """
        CREATE TABLE users (
            email text primary key, name text, password text)"""
    )

    # Insert sample data for Alice
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ("alice@example.com", "Alice Xu", pbkdf2_sha256.hash("123456")),
    )

    # Insert sample data for Bob
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ("bob@example.com", "Bobby Tables", pbkdf2_sha256.hash("123456")),
    )
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ("charlie@example.com", "Charlie Brown", pbkdf2_sha256.hash("654321")),
    )
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        ("diana@example.com", "Diana Prince", pbkdf2_sha256.hash("abcdef")),
    )

    con.commit()
    con.close()


# Run the function
setup_user_database()
