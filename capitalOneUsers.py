apiKey = '9f463d7fe410b9f89d60beee49ab831a'
import requests
import json


#USAGES:
"""
CREATE CUSTOMER:
    create_customer("test", "test", "100", "Packard", "Ann Arbor", "MI", "48306"
CREATE ACCOUNT FOR CUSTOMER:
    **digits at the end must be 16 bits long and unique for every user
    create_account("655925c09683f20dd5188988", "Credit Card", "My Card", 0, 0, "1111111111111111"
WITHDRAW MONEY
    create_withdrawal("6559201c9683f20dd518897d", "balance", "2023-11-18", "pending", 10.00, "Withdrawal")
DEPOSIT MONEY
    create_deposit("6559201c9683f20dd518897d", "balance", "2023-11-18", "pending", 10.00, "Deposit")
ACCESS BALANCE
    for account in fetch_accounts("65591dea9683f20dd518897b"):
        print(f"Account ID: {account['_id']}, Balance: {account['balance']}")

-customers can have multipe accounds
"""

# example usage create_customer("test", "test", "100", "Packard", "Ann Arbor", "MI", "48306"
def create_customer(first_name, last_name, street_number, street_name, city, state, zip_code):
    url = "http://api.nessieisreal.com/customers?key=9f463d7fe410b9f89d60beee49ab831a"
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "address": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zip_code
        }
    }
    response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"

# Example usage: print(create_account("655925c09683f20dd5188988", "Credit Card", "My Card", 0, 0, "1111111111111111"))
def create_account(customer_id, account_type, nickname, rewards, balance, account_number):
    url = f"http://api.nessieisreal.com/customers/{customer_id}/accounts?key=9f463d7fe410b9f89d60beee49ab831a"
    payload = {
        "type": account_type,
        "nickname": nickname,
        "rewards": rewards,
        "balance": balance,
        "account_number": account_number
    }

    response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"


# Example usage: print(create_deposit("6559201c9683f20dd518897d", "balance", "2023-11-18", "pending", 10.00, "Deposit"))
def create_deposit(account_id, medium, transaction_date, status, amount, description):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/deposits?key=9f463d7fe410b9f89d60beee49ab831a"
    payload = {
        "medium": medium,
        "transaction_date": transaction_date,
        "status": status,
        "amount": amount,
        "description": description
    }
    response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"

# Example usage: print(create_withdrawal("6559201c9683f20dd518897d", "balance", "2023-11-18", "pending", 10.00, "Withdrawal"))
def create_withdrawal(account_id, medium, transaction_date, status, amount, description):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/withdrawals?key=9f463d7fe410b9f89d60beee49ab831a"
    payload = {
        "medium": medium,
        "transaction_date": transaction_date,
        "status": status,
        "amount": amount,
        "description": description
    }
    response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"


#usage: for account in fetch_accounts("65591dea9683f20dd518897b"):
#           print(f"Account ID: {account['_id']}, Balance: {account['balance']}")
def fetch_accounts(customer_id):
    url = f"http://api.nessieisreal.com/customers/{customer_id}/accounts?key=9f463d7fe410b9f89d60beee49ab831a"
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"



def delete_data():
    url = "http://api.nessieisreal.com/data?type=Customers&key=9f463d7fe410b9f89d60beee49ab831a"
    headers = {
        "Content-Type": "application/json",
        "API-Key": apiKey  # Replace with your actual API key
    }
    params = {
        "type": "Customers"
    }
    response = requests.delete(url, headers=headers, params=params)

    if response.status_code == 204:
        return "Data deleted successfully"
    else:
        return f"Error: {response.status_code}, {response.json()}"
