# Flask Banking System

Welcome to the Flask Banking System, a simple yet robust web application built with Flask. This system is designed to manage user authentication, account details, balance transfers, and display dashboards for banking operations.

## Features

- **User Authentication**: Secure login and logout capabilities.
- **Account Management**: View details of bank accounts including balances.
- **Balance Transfer**: Transfer funds between accounts securely.
- **Dashboard**: Personalized user dashboard to overview account details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- Flask
- SQLite3

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask-banking-system.git
   cd flask-banking-system
   ```

2. **Set up a virtual environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:

   ```bash
   python app.py
   ```

   Visit `http://127.0.0.1:5000/dashboard` in your web browser.

## Usage

After launching the app, you can interact with the web interface to manage accounts and perform transactions.

- **Login**: Authenticate using a username and password.
- **View Dashboard**: Access personalized account details and recent transaction history.
- **Transfer Funds**: Use the transfer form to move funds between accounts.
