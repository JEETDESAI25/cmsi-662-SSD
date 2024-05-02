"""
This module provides functions for user authentication and token generation using Flask and SQLite.

Note: This module requires the Flask, SQLite, passlib, and jwt libraries to be installed.
"""

import sqlite3
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256
from flask import request, g
import jwt

SECRET = "bfg28y7efg238re7r6t32gfo23vfy7237yibdyo238do2v3"


# Gets users credentials (e.g. email and password)
import sqlite3
from passlib.hash import pbkdf2_sha256


def get_user_with_credentials(email, password):
    """
    Retrieves a user from the database based on the provided email and password.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        dict or None: A dictionary containing the user's email, name, and token if the credentials are valid.
                      Returns None if the user is not found or the password is incorrect.
    """
    try:
        con = sqlite3.connect("storage.db")
        cur = con.cursor()

        # Execute a SQL query to retrieve the user with the provided email
        cur.execute(
            """
            SELECT email, name, password FROM users WHERE email=?
            """,
            (email,),
        )
        row = cur.fetchone()

        # If no user is found, return None
        if row is None:
            return None

        # Extract the email, name, and hashed password from the retrieved row
        email, name, hash = row

        # Verify the provided password against the hashed password using pbkdf2_sha256
        if not pbkdf2_sha256.verify(password, hash):
            return None

        # If the password is correct, create a token and return the user's email, name, and token
        return {"email": email, "name": name, "token": create_token(email)}
    finally:
        # Close the database connection
        con.close()


# Authenticate the user's credentials and authenticate the tokens on the cookies. Once verified it is passed on to the flask session
def logged_in():
    token = request.cookies.get("auth_token")
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        g.user = data["sub"]
        return True
    except jwt.InvalidTokenError:
        return False


# After authenticating token for the user using the symetric login algorithm HS256, verifies the user's signature with secret key
def create_token(email):
    now = datetime.utcnow()
    payload = {"sub": email, "iat": now, "exp": now + timedelta(minutes=60)}
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token
